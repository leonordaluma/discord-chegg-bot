import asyncio
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

import cheinsteinpy
import json


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

with open("config.json", "r") as f:
    config = json.load(f)

with open("cookie.txt", 'r') as f:
    cookie = f.read()

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

# url = "https://www.chegg.com/homework-help/a-brief-introduction-to-criminal-law-2nd-edition-chapter-2-problem-19pt-solution-9781284056112"
# isChapter = cheinsteinpy.checkLink(url)
# questionRaw = cheinsteinpy.question(url, cookie, config['userAgent'])
# answerRaw = cheinsteinpy.answer(url, cookie, config['userAgent'])
# print(isChapter)
# print(questionRaw)
# print(answerRaw)
