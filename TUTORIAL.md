# 📖 Tutorial completo — Discord Connect

Este guia cobre tudo do zero: desde criar o bot no Discord até deixá-lo rodando 24 horas por dia.

> Algo deu errado? Consulte o [FAQ e solução de problemas](FAQ.md).

---

## 📋 Índice

0. [💻 Abrindo o terminal](#0-abrindo-o-terminal)
1. [🐍 Instalando o Python](#1-instalando-o-python)
2. [🌿 Instalando o Git](#2-instalando-o-git)
3. [📥 Clonando o repositório](#3-clonando-o-repositório)
4. [🖥️ Instalando o VS Code](#4-instalando-o-vs-code)
5. [📦 Instalando as dependências](#5-instalando-as-dependências)
6. [🤖 Criando o bot no Discord](#6-criando-o-bot-no-discord)
7. [📨 Convidando o bot para o servidor](#7-convidando-o-bot-para-o-servidor)
8. [🌐 Ativando o GitHub Pages](#8-ativando-o-github-pages)
9. [⚙️ Configurando o .env](#9-configurando-o-env)
10. [🛡️ Sistema de segurança — whitelist de servidores](#10-sistema-de-segurança--whitelist-de-servidores)
11. [🚀 Rodando o bot](#11-rodando-o-bot)
12. [☁️ Hospedando o bot 24/7](#12-hospedando-o-bot-247)
13. [✅ Considerações finais](#considerações-finais)

---

<a id="0-abrindo-o-terminal"></a>
## 💻 0. Abrindo o terminal

O terminal é onde você digita comandos para instalar e rodar o bot. Veja como abrir em cada sistema:

### 🖥️ Windows

**Opção 1 — Prompt de Comando:**
1. Pressione `Windows + R`
2. Digite `cmd` e pressione Enter

**Opção 2 — PowerShell (recomendado):**
1. Clique no menu Iniciar
2. Busque por `PowerShell`
3. Clique em **Windows PowerShell**

**Opção 3 — Pelo VS Code (mais prático, após a seção 4):**
1. Abra o VS Code na pasta do projeto
2. Pressione `` Ctrl+` `` (acento grave) para abrir o terminal integrado

### 🍎 macOS

1. Pressione `Command + Espaço` para abrir o Spotlight
2. Digite `Terminal` e pressione Enter

### 🐧 Linux

Pressione `Ctrl+Alt+T` — funciona na maioria das distribuições.

---

<a id="1-instalando-o-python"></a>
## 🐍 1. Instalando o Python

O bot é escrito em Python, então você precisa instalá-lo antes de tudo.

1. Acesse **https://www.python.org/downloads/release/python-3119/**
2. Baixe o instalador da versão **Python 3.11** (recomendada para este projeto)
3. Execute o instalador
4. **IMPORTANTE:** na primeira tela do instalador, marque a opção **"Add Python to PATH"** antes de clicar em Install Now

Para verificar se deu certo, abra o terminal e rode:
```bash
python --version
```
Deve aparecer algo como `Python 3.11.x`.

---

<a id="2-instalando-o-git"></a>
## 🌿 2. Instalando o Git

O Git é necessário para baixar o projeto do GitHub.

1. Acesse **https://git-scm.com/downloads**
2. Baixe a versão para seu sistema operacional
3. Execute o instalador com as opções padrão

Para verificar se deu certo:
```bash
git --version
```

---

<a id="3-clonando-o-repositório"></a>
## 📥 3. Clonando o repositório

Agora que o Git está instalado, baixe o projeto. Abra o terminal, navegue até a pasta onde quer salvar e rode:

```bash
git clone https://github.com/rodopoulos1/DiscordConnect.git
cd DiscordConnect
```

> Se você fez fork do repositório, substitua pelo link do seu fork.

---

<a id="4-instalando-o-vs-code"></a>
## 🖥️ 4. Instalando o VS Code

O VS Code é o editor recomendado para editar o `.env` e acompanhar o projeto.

1. Acesse **https://code.visualstudio.com/**
2. Clique em **Download for Windows** (ou seu sistema operacional)
3. Execute o instalador com as opções padrão

**Extensões recomendadas após instalar:**
- **Python** (Microsoft) — suporte completo a Python no VS Code
- **Python Indent** — indentação automática correta

Para instalar extensões: pressione `Ctrl+Shift+X`, busque pelo nome e clique em **Install**.

**Abrindo o projeto no VS Code:**
```bash
code .
```
Rode esse comando dentro da pasta `DiscordConnect` para abrir o projeto diretamente.

---

<a id="5-instalando-as-dependências"></a>
## 📦 5. Instalando as dependências

Com o projeto aberto, instale as bibliotecas necessárias:

```bash
pip install -r requirements.txt
```

> **O que é pip?** É o gerenciador de pacotes do Python — ele baixa e instala bibliotecas automaticamente. O arquivo `requirements.txt` lista tudo que o projeto precisa; esse comando instala tudo de uma vez.

---

<a id="6-criando-o-bot-no-discord"></a>
## 🤖 6. Criando o bot no Discord

### 📁 6.1 Criando a aplicação

1. Acesse **https://discord.com/developers/applications**
2. Faça login com sua conta Discord
3. Clique em **New Application** (canto superior direito)
4. Dê um nome para a sua aplicação (ex: `Connect Bot`) e clique em **Create**

### 🤖 6.2 Criando o bot

1. No menu lateral esquerdo, clique em **Bot**
2. Clique em **Add Bot** e confirme clicando em **Yes, do it!**

### 🔑 6.3 Copiando o token

O token é a senha do seu bot — **nunca compartilhe com ninguém**.

1. Na página do Bot, clique em **Reset Token**
2. Confirme a ação
3. Copie o token gerado — você vai precisar dele na seção 9

> ⚠️ Se alguém tiver o token do seu bot, ele tem controle total sobre ele. Nunca suba o `.env` para o GitHub.

### ⚙️ 6.4 Ativando os Intents

Os Intents são permissões que o bot precisa para funcionar corretamente.

1. Ainda na página **Bot**, desça até **Privileged Gateway Intents**
2. Ative as três opções:
   - **Presence Intent**
   - **Server Members Intent**
   - **Message Content Intent**
3. Clique em **Save Changes**

---

<a id="7-convidando-o-bot-para-o-servidor"></a>
## 📨 7. Convidando o bot para o servidor

A forma mais fácil de gerar o link de convite é usando a calculadora de permissões do Discord:

1. Acesse **https://discordapi.com/permissions.html**
2. No campo **Client ID**, cole o ID da sua aplicação
   - Para pegar o Client ID: no [Portal de Desenvolvedores](https://discord.com/developers/applications), abra sua aplicação e copie o **Application ID** na aba **General Information**
3. Marque a permissão **Administrator**
4. O link de convite vai aparecer automaticamente na parte de baixo da página
5. Acesse o link, selecione seu servidor e clique em **Autorizar**

Aproveite agora para pegar o **ID do canal** e o **ID do servidor** — você vai precisar de ambos na seção 9:
1. No Discord, vá em **Configurações → Avançado** e ative o **Modo de Desenvolvedor**
2. Clique com o botão direito no canal desejado
3. Clique em **Copiar ID do canal**
4. Para pegar o ID do servidor: clique com o botão direito no **ícone do servidor** (no painel lateral esquerdo)
5. Clique em **Copiar ID do servidor**

> **Para que serve o ID do servidor?** O bot tem um sistema de segurança: se alguém convidar o bot para outro servidor, ele vai sair automaticamente. Preenchendo `GUILD_ID`, só o seu servidor é autorizado.

---

<a id="8-ativando-o-github-pages"></a>
## 🌐 8. Ativando o GitHub Pages

O botão de conexão precisa de uma página hospedada para funcionar. O GitHub Pages é gratuito e faz isso automaticamente.

1. Faça um fork deste repositório no GitHub (ou use o seu próprio)
2. No seu repositório, vá em **Settings → Pages**
3. Em **Source**, selecione:
   - Branch: `main`
   - Pasta: `/ (root)`
4. Clique em **Save**
5. Aguarde alguns minutos — o GitHub vai ativar o Pages no endereço:
   ```
   https://seuusuario.github.io/DiscordConnect/
   ```

Anote a URL completa do `connect.html` — você vai precisar dela na próxima seção:
```
https://seuusuario.github.io/DiscordConnect/connect.html
```

---

<a id="9-configurando-o-env"></a>
## ⚙️ 9. Configurando o .env

Agora você tem tudo que precisa: token do bot, ID do canal e URL do Pages. Vamos configurar o arquivo `.env`.

Copie o arquivo de exemplo:

- **Windows:** `copy .env.example .env`
- **Linux/Mac:** `cp .env.example .env`

Abra o `.env` no VS Code e preencha as variáveis:

```env
DISCORD_TOKEN=token_copiado_na_secao_6
CANAL_ID=id_do_canal_copiado_na_secao_7
GUILD_ID=id_do_servidor_copiado_na_secao_7
SERVER_IP=ip_do_servidor_de_jogo
SERVER_PORT=porta_do_servidor
GAME=cs2
SERVER_NOME_PADRAO=Nome do Servidor
CONNECT_PAGE_URL=https://seuusuario.github.io/DiscordConnect/connect.html
```

---

<a id="10-sistema-de-segurança--whitelist-de-servidores"></a>
## 🛡️ 10. Sistema de segurança — whitelist de servidores

O bot inclui um sistema de segurança simples e eficaz: **whitelist de servidor**.

### 🤔 Por que usar?

É possível que alguém mal-intencionado convide o seu bot para o servidor dele sem você saber. Com o token ativo em um servidor fora do seu controle, a pessoa poderia monitorar atividades ou tentar explorar o bot de formas indesejadas.

Com a whitelist ativada, **o bot sai automaticamente de qualquer servidor que não seja o seu** assim que entrar nele.

> É fortemente recomendado ativar essa proteção. Preencha `GUILD_ID` antes de colocar o bot no ar.

### ✅ Como ativar

Basta preencher `GUILD_ID` no `.env` com o ID do seu servidor (veja como pegar na seção 7):

```env
GUILD_ID=1167254207833841686
```

Deixe vazio para desativar — o bot funcionará em qualquer servidor normalmente.

### 🔧 Como funciona internamente

O bot verifica a whitelist em dois momentos:

1. **Ao iniciar o bot** — percorre todos os servidores em que já está e sai de qualquer um que não seja o autorizado.
2. **Ao entrar em um servidor novo** — sai imediatamente se não for o servidor autorizado.

Você não precisa entender o código para usar, mas caso tenha curiosidade, é isso que acontece por baixo dos panos:

```python
@bot.event
async def on_ready():
    if GUILD_ID:
        for guild in list(bot.guilds):
            if guild.id != GUILD_ID:
                await guild.leave()

@bot.event
async def on_guild_join(guild):
    if GUILD_ID and guild.id != GUILD_ID:
        await guild.leave()
```

Simples, silencioso e eficaz.

### 🥚 Easter egg — mensagem de despedida

Se quiser deixar uma surpresa para quem convidar seu bot sem permissão, dá para fazer o bot mandar 5 mensagens num canal qualquer antes de sair. Não está no código por padrão — mas se quiser adicionar, é só substituir os dois eventos no `main.py` por isso aqui:

```python
async def _despedir(guild: discord.Guild):
    canal = next(
        (c for c in guild.text_channels if c.permissions_for(guild.me).send_messages),
        None
    )
    if canal:
        for _ in range(5):
            await canal.send("O dono desse servidor é um idiota 👋")
    await guild.leave()

@bot.event
async def on_ready():
    if GUILD_ID:
        for guild in list(bot.guilds):
            if guild.id != GUILD_ID:
                print(f"[DISCORD CONNECT] Saindo do servidor não autorizado: {guild.name} ({guild.id})")
                await _despedir(guild)

@bot.event
async def on_guild_join(guild: discord.Guild):
    if GUILD_ID and guild.id != GUILD_ID:
        print(f"[DISCORD CONNECT] Saindo do servidor não autorizado: {guild.name} ({guild.id})")
        await _despedir(guild)
```

O bot procura qualquer canal de texto onde ele tenha permissão para escrever, manda 5 mensagens e vai embora. Silenciosamente. Sem apelação.

> Por que um canal aleatório? Porque o bot acabou de entrar em um servidor desconhecido — ele não tem nenhuma configuração para aquele lugar, não sabe o nome dos canais, nada. Então ele pega o primeiro canal onde consegue escrever e usa esse. Pode cair no geral, pode cair num canal de regras, pode cair em qualquer lugar.

---

<a id="11-rodando-o-bot"></a>
## 🚀 11. Rodando o bot

Com tudo configurado, abra o terminal na pasta do projeto e rode:

```bash
python main.py
```

Se tudo estiver certo, o bot vai conectar e enviar (ou atualizar) o painel no canal configurado.

**Mensagens esperadas no terminal:**
```
[DISCORD CONNECT] Mensagem enviada e ID salvo.
[DISCORD CONNECT] Painel atualizado.
```

> Se aparecer algum erro, verifique se o token está correto, se o bot está no servidor e se o ID do canal está certo.

---

<a id="12-hospedando-o-bot-247"></a>
## ☁️ 12. Hospedando o bot 24/7

Rodar o bot no seu computador pessoal significa que ele para quando você desliga a máquina. Para deixá-lo online o tempo todo, você precisa de um servidor.

### 🖥️ MJSV Host (R$5/mês) — recomendado

A MJSV é uma hospedagem brasileira que oferece planos para bots Discord e servidores de jogos com ótimo custo-benefício.

- Suporta bots Discord
- Suporta servidores de jogos
- A partir de **R$5/mês**

Para contratar, entre em contato via Discord: **ascp**

---

<a id="considerações-finais"></a>
## ✅ Considerações finais

Se você chegou até aqui, parabéns — o bot está no ar!

Algumas dicas para manter tudo funcionando bem:

- **Nunca suba o `.env` para o GitHub.** Ele está no `.gitignore` por padrão, mas fique atento. Se o token vazar, acesse o [Portal de Desenvolvedores](https://discord.com/developers/applications) imediatamente e gere um novo em **Bot → Reset Token**.

- **O bot edita a mesma mensagem para sempre.** O ID da mensagem fica salvo em `database/connect/msgid.json`. Se você deletar a mensagem no Discord, o bot vai criar uma nova automaticamente no próximo ciclo.

- **Quer mudar o servidor de jogo?** Basta editar o `.env` e reiniciar o bot — nenhuma linha de código precisa ser alterada.

- **O painel atualiza a cada 5 minutos por padrão.** Para mudar, ajuste `INTERVALO_ATUALIZACAO` no `.env` (valor em segundos).

- **Imagem não apareceu?** Verifique se o `GAME` no `.env` está escrito corretamente (`cs2`, `tf2`, etc.) ou defina uma URL fixa em `ICONE_URL`.

- **Botão de conectar não funciona?** Confirme que o GitHub Pages está ativo e que a `CONNECT_PAGE_URL` está preenchida corretamente no `.env`.

---

💬 Dúvidas? Me chama no Discord: **Rodopoulos**

> Dica: tente incluir sua dúvida já na primeira mensagem — economiza tempo dos dois. ([nohello.net/pt-br](https://nohello.net/pt-br/))

🤝 Tem algum projeto em mente, independente do tamanho? Me chame no Discord: **Rodopoulos**

