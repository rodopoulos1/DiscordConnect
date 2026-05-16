🌐 **Language / Idioma:** [English](README.en.md) · [Português](README.md)

📖 **First time here?** Check the [Complete beginner's tutorial](TUTORIAL.md) (Portuguese)

❓ **Something went wrong?** Check the [FAQ and troubleshooting guide](FAQ.md) (Portuguese)

---

# 🎮 Discord Connect

Discord bot that displays a real-time game server status panel with an automatic Steam connection button.

Compatible with any game using the **Steam/Source** protocol (CS2, TF2, Garry's Mod, Rust, ARK, etc.).

---

## ✨ Features

- 🔄 Panel automatically updated in the configured channel
- 👥 Shows server name, online players and current map
- 🗺️ Map image automatically selected for CS2/CS:GO
- 🖼️ For other games, uses the game's Steam store header image
- 🔗 Connect button that opens Steam directly

---

## 🚀 Installation

```bash
git clone https://github.com/yourusername/DiscordConnect.git
cd DiscordConnect
pip install -r requirements.txt
cp .env.example .env
```

Edit `.env` with your settings and run:

```bash
python main.py
```

---

## ⚙️ `.env` Configuration

| Variable                | Description                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| `DISCORD_TOKEN`         | 🔑 Your Discord bot token                                                   |
| `CANAL_ID`              | 📢 ID of the channel where the panel will be posted                         |
| `GUILD_ID`              | 🛡️ ID of the authorized server — bot auto-leaves any other server            |
| `SERVER_IP`             | 🌐 Game server IP address                                                   |
| `SERVER_PORT`           | 🔌 Game server port                                                         |
| `GAME`                  | 🎮 Game identifier (`cs2`, `csgo`, `tf2`, `gmod`, `rust`, `ark`)            |
| `SERVER_NOME_PADRAO`    | 📛 Name shown when the server is offline                                    |
| `ICONE_URL`             | 🖼️ (Optional) Fixed image URL, overrides automatic selection                |
| `CONNECT_PAGE_URL`      | 🔗 URL of the hosted `connect.html` page (see below)                        |
| `INTERVALO_ATUALIZACAO` | ⏱️ Update interval in seconds (default: `300`)                              |
| `EMBED_TITULO`          | 📝 Embed title (default: `🌐 Status`)                                       |
| `EMBED_FOOTER`          | 📄 Embed footer text (default: `Discord Connect ▹ by Rodopoulos`)           |
| `BOTAO_LABEL`           | 🖱️ Connect button label — supports emoji (default: `🎮 Conectar-se`)        |
| `EXIBIR_JOGO`           | 👁️ Show game field in embed — `true` or `false` (default: `true`)          |
| `EXIBIR_JOGADORES`      | 👁️ Show players field in embed — `true` or `false` (default: `true`)       |
| `EXIBIR_MAPA`           | 👁️ Show map field in embed — `true` or `false` (default: `true`)           |

---

## 🛡️ Security system — server whitelist

The bot only operates in the server whose ID is set in `GUILD_ID`. If someone invites the bot to another server, it **automatically leaves**.

This prevents unauthorized use of the bot in environments outside your control. It is strongly recommended to fill in this variable before going live.

Leave empty to disable the restriction.

---

## 🔗 Setting up the connect button (connect.html)

The `connect.html` file included in this repository redirects the user to the server using the `steam://` protocol. To make the bot button work, you need to host this page — the easiest way is via **GitHub Pages**.

### 📋 Step by step

1. Fork this repository or create your own on GitHub.
2. Go to **Settings → Pages** and enable GitHub Pages on the `main` branch (root `/`).
3. After enabling, your page will be available at:
   ```
   https://yourusername.github.io/DiscordConnect/connect.html
   ```
4. Copy that URL and paste it in your `.env`:
   ```
   CONNECT_PAGE_URL=https://yourusername.github.io/DiscordConnect/connect.html
   ```

The bot will automatically generate the link with `?ip=...&port=...` parameters and the page handles the Steam redirect.

> 💡 If you leave `CONNECT_PAGE_URL` empty, the button will use `steam://connect/ip:port` directly — but some browsers block `steam://` links inside Discord embeds.

---

## 🖼️ Automatic image selection

| Game                              | Behavior                                                   |
|-----------------------------------|------------------------------------------------------------|
| `cs2` / `csgo`                    | 🗺️ Uses the current map image (community CDN)           |
| `tf2`, `gmod`, `rust`, `ark`      | 🎮 Uses the game's Steam store header image               |
| Any other                         | ❌ No image (or set `ICONE_URL` to define one)             |

> To force a specific image for any game, set `ICONE_URL` in your `.env`.

---

## 💬 Questions

Feel free to reach out on Discord: **Rodopoulos**

> Tip: try to include your question in the first message — saves time for both of us. ([nohello.net](https://nohello.net/en/))
