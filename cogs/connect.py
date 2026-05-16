import asyncio
import json
import os

import a2s
import discord
from discord.ext import commands

from utils.imagens import obter_imagem

CANAL_ID    = int(os.getenv("CANAL_ID", "0"))
SERVER_IP   = os.getenv("SERVER_IP", "")
SERVER_PORT = int(os.getenv("SERVER_PORT", "27015"))
GAME        = os.getenv("GAME", "").lower()
NOME_PADRAO = os.getenv("SERVER_NOME_PADRAO", "Servidor")
ICONE_URL   = os.getenv("ICONE_URL", "")
CONNECT_URL = os.getenv("CONNECT_PAGE_URL", "")
INTERVALO   = int(os.getenv("INTERVALO_ATUALIZACAO", "300"))

EMBED_TITULO      = os.getenv("EMBED_TITULO", "🌐 Status")
EMBED_FOOTER      = os.getenv("EMBED_FOOTER", "Discord Connect ▹ by Rodopoulos")
BOTAO_LABEL       = os.getenv("BOTAO_LABEL", "🎮 Conectar-se")
EXIBIR_JOGO       = os.getenv("EXIBIR_JOGO", "true").lower() == "true"
EXIBIR_JOGADORES  = os.getenv("EXIBIR_JOGADORES", "true").lower() == "true"
EXIBIR_MAPA       = os.getenv("EXIBIR_MAPA", "true").lower() == "true"

SERVER_ADDRESS = (SERVER_IP, SERVER_PORT)
CAMINHO_MSGID  = "./database/connect/msgid.json"

GAME_LABELS: dict[str, str] = {
    "cs2":       "Counter-Strike 2",
    "csgo":      "CS:GO",
    "tf2":       "Team Fortress 2",
    "gmod":      "Garry's Mod",
    "garrysmod": "Garry's Mod",
    "rust":      "Rust",
    "ark":       "ARK: Survival Evolved",
}


class PainelConnect(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.msg_id: int | None = None
        self._tarefa: asyncio.Task | None = None

    @commands.Cog.listener()
    async def on_ready(self):
        await self._carregar_ou_enviar_msg()
        if self._tarefa is None or self._tarefa.done():
            self._tarefa = asyncio.create_task(self._atualizador_painel())

    async def _atualizador_painel(self):
        await self.bot.wait_until_ready()

        while not self.bot.is_closed():
            await asyncio.sleep(INTERVALO)
            try:
                if self.msg_id is None:
                    continue

                canal = self.bot.get_channel(CANAL_ID)
                if not canal:
                    print("[DISCORD CONNECT] Canal não encontrado para atualização.")
                    continue

                try:
                    msg = await canal.fetch_message(self.msg_id)
                except discord.NotFound:
                    print("[DISCORD CONNECT] Mensagem não existe mais, aguardando próximo ciclo.")
                    self.msg_id = None
                    continue

                embed = await self._criar_embed()
                view = self._criar_botao_conectar()
                await msg.edit(embed=embed, view=view)
                print("[DISCORD CONNECT] Painel atualizado.")
            except Exception as e:
                print(f"[DISCORD CONNECT] Erro ao atualizar painel: {e}")

    async def _carregar_ou_enviar_msg(self):
        os.makedirs(os.path.dirname(CAMINHO_MSGID), exist_ok=True)

        canal = self.bot.get_channel(CANAL_ID)
        if canal is None:
            print(f"[DISCORD CONNECT] Canal {CANAL_ID} não encontrado.")
            return

        if os.path.exists(CAMINHO_MSGID):
            try:
                with open(CAMINHO_MSGID, "r", encoding="utf-8") as f:
                    self.msg_id = json.load(f).get("msg_id")
            except Exception as e:
                print(f"[DISCORD CONNECT] Erro ao ler msgid.json: {e}")

        embed = await self._criar_embed()
        view = self._criar_botao_conectar()

        if self.msg_id:
            try:
                msg = await canal.fetch_message(self.msg_id)
                await msg.edit(embed=embed, view=view)
                print("[DISCORD CONNECT] Mensagem restaurada com sucesso.")
                return
            except discord.NotFound:
                print("[DISCORD CONNECT] Mensagem antiga não encontrada, enviando nova.")

        nova_msg = await canal.send(embed=embed, view=view)
        self.msg_id = nova_msg.id
        with open(CAMINHO_MSGID, "w", encoding="utf-8") as f:
            json.dump({"msg_id": self.msg_id}, f, indent=4)
        print("[DISCORD CONNECT] Mensagem enviada e ID salvo.")

    async def _criar_embed(self) -> discord.Embed:
        mapa: str | None = None
        try:
            info = await asyncio.wait_for(a2s.ainfo(SERVER_ADDRESS), timeout=2.5)
            nome     = info.server_name
            jogadores = f"{info.player_count}/{info.max_players}"
            mapa     = info.map_name
        except Exception:
            nome      = NOME_PADRAO
            jogadores = "Desconhecido"

        game_label = GAME_LABELS.get(GAME, GAME or "Desconhecido")
        imagem = obter_imagem(GAME, mapa, ICONE_URL)

        embed = discord.Embed(
            title=EMBED_TITULO,
            description=f"**{nome}**",
            color=discord.Color.blue(),
        )
        if EXIBIR_JOGO:
            embed.add_field(name="🎮 Jogo",      value=game_label,             inline=True)
        if EXIBIR_JOGADORES:
            embed.add_field(name="👥 Jogadores", value=jogadores,              inline=True)
        if EXIBIR_MAPA:
            embed.add_field(name="🗺️ Mapa",      value=mapa or "Desconhecido", inline=True)
        embed.add_field(
            name="🔗 Conexão",
            value=f"`connect {SERVER_IP}:{SERVER_PORT}`",
            inline=False,
        )
        embed.set_footer(text=EMBED_FOOTER)
        if imagem:
            embed.set_image(url=imagem)
        return embed

    def _criar_botao_conectar(self) -> discord.ui.View:
        if CONNECT_URL:
            url = f"{CONNECT_URL}?ip={SERVER_IP}&port={SERVER_PORT}"
        else:
            url = f"steam://connect/{SERVER_IP}:{SERVER_PORT}"

        class BotaoConectar(discord.ui.View):
            def __init__(self_view, url_connect: str):
                super().__init__(timeout=None)
                self_view.add_item(
                    discord.ui.Button(
                        label=BOTAO_LABEL,
                        style=discord.ButtonStyle.link,
                        url=url_connect,
                    )
                )

        return BotaoConectar(url)


async def setup(bot: commands.Bot):
    await bot.add_cog(PainelConnect(bot))
