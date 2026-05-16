🌐 **Idioma / Language:** [Português](README.md) · [English](README.en.md)

📖 **Primeira vez aqui?** Veja o [Tutorial completo para iniciantes](TUTORIAL.md)

❓ **Algo deu errado?** Consulte o [FAQ e solução de problemas](FAQ.md)

---

# 🎮 Discord Connect

Bot Discord que exibe um painel de status de servidor de jogo em tempo real, com botão de conexão automática via Steam.

Compatível com qualquer jogo que use o protocolo **Steam/Source** (CS2, TF2, Garry's Mod, Rust, ARK, etc.).

---

## ✨ Funcionalidades

- 🔄 Painel atualizado automaticamente no canal configurado
- 👥 Mostra nome do servidor, jogadores online e mapa atual
- 🗺️ Imagem do mapa selecionada automaticamente para CS2/CS:GO
- 🖼️ Para outros jogos, usa a imagem de capa do jogo na Steam
- 🔗 Botão de conectar que abre o Steam diretamente

---

## 🚀 Instalação

```bash
git clone https://github.com/seuusuario/DiscordConnect.git
cd DiscordConnect
pip install -r requirements.txt
cp .env.example .env
```

Edite o `.env` com as suas configurações e rode:

```bash
python main.py
```

---

## ⚙️ Configuração do `.env`

| Variável                | Descrição                                                                  |
|-------------------------|----------------------------------------------------------------------------|
| `DISCORD_TOKEN`         | 🔑 Token do bot Discord                                                    |
| `CANAL_ID`              | 📢 ID do canal onde o painel será postado                                  |
| `GUILD_ID`              | 🛡️ ID do servidor autorizado — o bot sai de qualquer outro automaticamente  |
| `SERVER_IP`             | 🌐 IP do servidor de jogo                                                  |
| `SERVER_PORT`           | 🔌 Porta do servidor de jogo                                               |
| `GAME`                  | 🎮 Identificador do jogo (`cs2`, `csgo`, `tf2`, `gmod`, `rust`, `ark`)     |
| `SERVER_NOME_PADRAO`    | 📛 Nome exibido quando o servidor estiver offline                          |
| `ICONE_URL`             | 🖼️ (Opcional) URL de imagem fixa, sobrescreve a seleção automática         |
| `CONNECT_PAGE_URL`      | 🔗 URL da página `connect.html` hospedada (ver abaixo)                     |
| `INTERVALO_ATUALIZACAO` | ⏱️ Intervalo de atualização em segundos (padrão: `300`)                    |
| `EMBED_TITULO`          | 📝 Título do embed (padrão: `🌐 Status`)                                   |
| `EMBED_FOOTER`          | 📄 Texto do rodapé do embed (padrão: `Discord Connect ▹ by Rodopoulos`)    |
| `BOTAO_LABEL`           | 🖱️ Label do botão de conexão — suporta emoji (padrão: `🎮 Conectar-se`)    |
| `EXIBIR_JOGO`           | 👁️ Exibir campo de jogo no embed — `true` ou `false` (padrão: `true`)     |
| `EXIBIR_JOGADORES`      | 👁️ Exibir campo de jogadores no embed — `true` ou `false` (padrão: `true`)|
| `EXIBIR_MAPA`           | 👁️ Exibir campo de mapa no embed — `true` ou `false` (padrão: `true`)     |

---

## 🛡️ Sistema de segurança — whitelist de servidor

O bot só opera no servidor cujo ID estiver em `GUILD_ID`. Se alguém convidar o bot para outro servidor, ele **sai automaticamente**.

Isso previne que pessoas mal-intencionadas usem o bot em ambientes fora do seu controle. É fortemente recomendado preencher essa variável antes de colocar o bot no ar.

Deixe vazio para desativar a restrição.

---

## 🔗 Configurando o botão de conexão (connect.html)

O arquivo `connect.html` incluído neste repositório redireciona o usuário para o servidor via protocolo `steam://`. Para que o botão do bot funcione, você precisa hospedar essa página — a forma mais simples é pelo **GitHub Pages**.

### 📋 Passo a passo

1. Faça um fork deste repositório ou crie o seu próprio no GitHub.
2. Vá em **Settings → Pages** e ative o GitHub Pages na branch `main` (raiz `/`).
3. Após ativar, sua página estará disponível em:
   ```
   https://seuusuario.github.io/DiscordConnect/connect.html
   ```
4. Copie essa URL e cole no `.env`:
   ```
   CONNECT_PAGE_URL=https://seuusuario.github.io/DiscordConnect/connect.html
   ```

O bot vai gerar automaticamente o link com os parâmetros `?ip=...&port=...` e a página faz o redirecionamento para o Steam.

> 💡 Se deixar `CONNECT_PAGE_URL` vazio, o botão usará `steam://connect/ip:porta` diretamente — mas alguns navegadores bloqueiam links `steam://` em embeds do Discord.

---

## 🖼️ Seleção automática de imagem

| Jogo                              | Comportamento                                        |
|-----------------------------------|------------------------------------------------------|
| `cs2` / `csgo`                    | 🗺️ Usa a imagem do mapa atual (via CDN da comunidade)  |
| `tf2`, `gmod`, `rust`, `ark`      | 🎮 Usa a imagem de capa do jogo na Steam             |
| Qualquer outro                    | ❌ Sem imagem (ou use `ICONE_URL` para definir uma)  |

> Para forçar uma imagem específica em qualquer jogo, defina `ICONE_URL` no `.env`.

---

## 💬 Dúvidas

Qualquer dúvida, me chama no Discord: **Rodopoulos**

> Dica: tente incluir sua dúvida já na primeira mensagem — economiza tempo dos dois. ([nohello.net/pt-br](https://nohello.net/pt-br/))
