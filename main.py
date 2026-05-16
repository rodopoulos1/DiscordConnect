import asyncio
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN    = os.getenv("DISCORD_TOKEN")
GUILD_ID = int(os.getenv("GUILD_ID", "0"))

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    if GUILD_ID:
        for guild in list(bot.guilds):
            if guild.id != GUILD_ID:
                print(f"[DISCORD CONNECT] Saindo do servidor não autorizado: {guild.name} ({guild.id})")
                await guild.leave()


@bot.event
async def on_guild_join(guild: discord.Guild):
    if GUILD_ID and guild.id != GUILD_ID:
        print(f"[DISCORD CONNECT] Saindo do servidor não autorizado: {guild.name} ({guild.id})")
        await guild.leave()


async def main():
    async with bot:
        await bot.load_extension("cogs.connect")
        await bot.start(TOKEN)


asyncio.run(main())
