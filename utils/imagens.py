STEAM_APP_HEADER = "https://cdn.cloudflare.steamstatic.com/steam/apps/{app_id}/header.jpg"
CS2_MAP_CDN = "https://raw.githubusercontent.com/ghostcap-gaming/cs2-map-images/main/cs2/{mapa}.png"

GAME_APP_IDS: dict[str, int] = {
    "cs2": 730,
    "csgo": 730,
    "tf2": 440,
    "gmod": 4000,
    "rust": 252490,
    "ark": 346110,
    "garrysmod": 4000,
}

GAMES_COM_MAPA_CDN = {"cs2", "csgo"}


def obter_imagem(game: str, mapa: str | None, icone_env: str) -> str | None:
    if icone_env:
        return icone_env

    if game in GAMES_COM_MAPA_CDN and mapa:
        return CS2_MAP_CDN.format(mapa=mapa)

    app_id = GAME_APP_IDS.get(game)
    if app_id:
        return STEAM_APP_HEADER.format(app_id=app_id)

    return None
