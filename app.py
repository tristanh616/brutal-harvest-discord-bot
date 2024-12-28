import os
import asyncio

import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.messages = True

bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

async def main():
    try:
        await bot.load_extension("cogs.commands")  # Await the load_extension coroutine
        await bot.start(os.getenv("DISCORD_TOKEN"))
    except Exception as e:
        print(f"An error occurred: {e}")



asyncio.run(main())