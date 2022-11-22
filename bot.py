import asyncio
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Initialize Bot
prefix = commands.when_mentioned_or('')
intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(
    command_prefix=prefix,
    intents=intents
)

async def load():
    for file in os.listdir('./cogs'):
        if file.endswith('.py'):
            await bot.load_extension(f'cogs.{file[:-3]}')

async def main():
    await load()
    try:
        await bot.start(TOKEN)
    except Exception as err:
        print(f'Error: {err}')

asyncio.run(main())
