# ❓ FAQ — Perguntas frequentes e solução de problemas

---

## Índice

- [⚠️ Erros no console e reconexões automáticas](#erros-no-console-e-reconexões-automáticas)
- [🐍 Python / pip](#python--pip)
- [❌ Bot não conecta](#bot-não-conecta)
- [📭 Bot conecta mas não envia a mensagem](#bot-conecta-mas-não-envia-a-mensagem)
- [🚪 Bot entrou no servidor e saiu imediatamente](#bot-entrou-no-servidor-e-saiu-imediatamente)
- [🔄 Painel não atualiza](#painel-não-atualiza)
- [📩 Mensagem duplicada no canal](#mensagem-duplicada-no-canal)
- [🖼️ Imagem não aparece no embed](#imagem-não-aparece-no-embed)
- [🔗 Botão de conectar não funciona](#botão-de-conectar-não-funciona)
- [📡 Status do servidor aparece como offline](#status-do-servidor-aparece-como-offline)
- [💻 Bot para quando fecho o terminal](#bot-para-quando-fecho-o-terminal)

---

<a id="erros-no-console-e-reconexões-automáticas"></a>
## ⚠️ Erros no console e reconexões automáticas

### ❓ Vejo vários erros no console, devo me preocupar?

Não necessariamente. O discord.py exibe avisos e mensagens de reconexão com frequência — isso é completamente normal.

### 🔄 O bot cai e se reconecta várias vezes por hora — é normal?

Sim. O Discord fecha conexões periodicamente e o discord.py se reconecta automaticamente. Você pode ver mensagens como:

```
Shard ID None has successfully RESUMED session...
Attempting a reconnect in X.X seconds...
```

O painel do servidor **não é perdido nessa reconexão** — quando o bot volta, ele edita a mesma mensagem no canal. Nada precisa ser feito da sua parte.

### ⚠️ Quando devo me preocupar de verdade?

Se o bot **parar de vez** e não se reconectar mais:
- Token invalidado (vazou ou você gerou um novo sem atualizar o `.env`)
- Servidor de hospedagem sem conexão com a internet
- Atualização quebrada no discord.py — rode `pip install --upgrade discord.py`

---

<a id="python--pip"></a>
## 🐍 Python / pip

### ❌ "python não é reconhecido como um comando interno"

Você instalou o Python mas esqueceu de marcar **"Add Python to PATH"** durante a instalação. Opções:

- **Opção 1 (mais fácil):** Desinstale o Python pelo Painel de Controle e reinstale marcando essa opção.
- **Opção 2:** Tente o comando `py` no lugar de `python`:
  ```bash
  py --version
  py -m pip install -r requirements.txt
  ```

### ❌ "pip não é reconhecido como um comando interno"

Mesma causa: Python não está no PATH. Use `py -m pip` no lugar de `pip`:
```bash
py -m pip install -r requirements.txt
```

### ❌ "ModuleNotFoundError: No module named 'discord'"

As dependências não foram instaladas. Rode dentro da pasta do projeto:
```bash
pip install -r requirements.txt
```
Se o erro persistir, tente:
```bash
py -m pip install -r requirements.txt
```

### ❌ "ModuleNotFoundError: No module named 'dotenv'"

Mesma solução — instale as dependências. O pacote correto é `python-dotenv`, não `dotenv`:
```bash
pip install python-dotenv
```

---

<a id="bot-não-conecta"></a>
## ❌ Bot não conecta

### 🔑 "discord.errors.LoginFailure: Improper token has been passed"

O token no `.env` está errado. Causas comuns:
- Copiou o token errado (pegou o Client Secret em vez do Bot Token)
- Tem espaço antes ou depois do token
- O token foi invalidado (você clicou em "Reset Token" depois de copiar)

Para gerar um novo token: acesse o [Portal de Desenvolvedores](https://discord.com/developers/applications) → sua aplicação → **Bot** → **Reset Token**.

### 🔌 O bot não aparece online no servidor

Verifique:
1. O token no `.env` está correto
2. O bot foi convidado para o servidor (seção 7 do TUTORIAL.md)
3. Não há erro sendo exibido no terminal ao rodar `python main.py`

---

<a id="bot-conecta-mas-não-envia-a-mensagem"></a>
## 📭 Bot conecta mas não envia a mensagem

### 📭 Nada acontece no canal após rodar o bot

Verifique o `CANAL_ID` no `.env`:
- O valor precisa ser **apenas números**, sem espaços ou aspas: `CANAL_ID=1234567890123456789`
- Para pegar o ID correto: no Discord, ative o Modo de Desenvolvedor em **Configurações → Avançado**, depois clique com o botão direito no canal e escolha **Copiar ID do canal**

### 🔒 "discord.errors.Forbidden" no terminal

O bot não tem permissão para enviar mensagens no canal. Verifique:
- O bot foi convidado com a permissão **Administrator**, ou ao menos **Enviar Mensagens** e **Incorporar Links** no canal
- O canal não tem restrições que bloqueiem o bot

---

<a id="bot-entrou-no-servidor-e-saiu-imediatamente"></a>
## 🚪 Bot entrou no servidor e saiu imediatamente

Você preencheu `GUILD_ID` no `.env` com o ID de um servidor diferente do que o bot está sendo adicionado, ou preencheu errado.

> Isso também pode acontecer ao **reiniciar o bot**: se ele já estava em um servidor não autorizado antes de `GUILD_ID` ser configurado, ele vai sair assim que subir.

Verifique:
- O `GUILD_ID` é o ID do **servidor** (guild), não do canal
- Para pegar: clique com o botão direito no **ícone do servidor** no Discord → **Copiar ID do servidor**
- Confirme que o valor no `.env` é exatamente esse número

Se não quiser usar a whitelist por enquanto, deixe `GUILD_ID=` vazio.

---

<a id="painel-não-atualiza"></a>
## 🔄 Painel não atualiza

### ⏱️ O embed ficou desatualizado e não muda mais

O bot atualiza o painel a cada intervalo configurado em `INTERVALO_ATUALIZACAO` (padrão: 300 segundos = 5 minutos). Se parece travado:
- Verifique se o bot ainda está rodando no terminal
- Reinicie o bot com `Ctrl+C` e `python main.py` novamente

### 📩 O bot criou uma segunda mensagem no canal

O arquivo `database/connect/msgid.json` foi deletado ou está corrompido. O bot não encontrou o ID da mensagem antiga e criou uma nova. Isso é esperado — delete a mensagem antiga manualmente no Discord se quiser deixar limpo.

---

<a id="mensagem-duplicada-no-canal"></a>
## 📩 Mensagem duplicada no canal

Se o bot está enviando uma nova mensagem toda vez que reinicia, o `msgid.json` provavelmente foi deletado junto com a pasta `database/`. O bot cria esse arquivo automaticamente ao enviar a primeira mensagem. A partir daí, sempre edita a mesma mensagem. Não delete a pasta `database/` enquanto o bot estiver em uso.

---

<a id="imagem-não-aparece-no-embed"></a>
## 🖼️ Imagem não aparece no embed

### 🖼️ O embed aparece sem imagem

Possíveis causas:

- **`GAME` não reconhecido:** certifique-se de que o valor é um dos suportados: `cs2`, `csgo`, `tf2`, `gmod`, `rust`, `ark`. Valores como `Counter-Strike 2` não funcionam — use `cs2`.
- **Mapa não encontrado:** para CS2/CSGO, a imagem é buscada automaticamente pelo nome do mapa (ex: `de_dust2`). Se o mapa for personalizado ou incomum, pode não existir na base de imagens.
- **Solução manual:** defina uma URL de imagem fixa em `ICONE_URL` no `.env` — ela sempre terá prioridade sobre a automática.

---

<a id="botão-de-conectar-não-funciona"></a>
## 🔗 Botão de conectar não funciona

### 🎮 O botão aparece mas não abre o jogo

O link `steam://connect/...` só funciona com o Steam instalado e aberto na máquina de quem clica. Não é um problema do bot.

### 🔗 O botão não aparece ou dá erro ao clicar

Verifique `CONNECT_PAGE_URL` no `.env`:
- Deve apontar para o `connect.html` do seu GitHub Pages, não para o repositório em si
- Formato correto: `https://seuusuario.github.io/DiscordConnect/connect.html`
- O GitHub Pages precisa estar ativado (seção 8 do TUTORIAL.md) — pode levar alguns minutos para ficar disponível após ativar

---

<a id="status-do-servidor-aparece-como-offline"></a>
## 📡 Status do servidor aparece como offline

### 📡 O servidor está online mas o bot mostra offline

Possíveis causas:
- O IP ou porta no `.env` estão errados — confirme com o painel da sua hospedagem
- O servidor de jogo usa um protocolo diferente do Steam/Source — o bot usa `python-a2s` que suporta jogos Source (CS2, TF2, Gmod, Rust, etc.)
- O firewall do servidor bloqueia consultas externas na porta do jogo

### 📛 O bot mostra nome padrão em vez do nome real do servidor

O nome exibido é o `SERVER_NOME_PADRAO` do `.env` quando o servidor está offline ou inacessível. Quando online, o nome real do servidor (retornado pela query) é usado automaticamente.

---

<a id="bot-para-quando-fecho-o-terminal"></a>
## 💻 Bot para quando fecho o terminal

Isso é esperado — o processo Python roda enquanto o terminal estiver aberto. Para manter o bot 24/7, você precisa de uma hospedagem. Veja a seção 12 do TUTORIAL.md.

Se quiser rodar em segundo plano temporariamente no Windows:
```bash
pythonw main.py
```
> Atenção: com `pythonw` você não vai ver erros no terminal. Use apenas se souber que o bot está funcionando corretamente.

---

💬 Ainda com dúvidas? Me chama no Discord: **Rodopoulos**

> Dica: tente incluir sua dúvida já na primeira mensagem — economiza tempo dos dois. ([nohello.net/pt-br](https://nohello.net/pt-br/))
