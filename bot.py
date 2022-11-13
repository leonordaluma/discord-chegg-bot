import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#Initialize Bot
intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(
    command_prefix='',
    intents = intents
)


@bot.event
async def on_ready():
    print(f'Bot is online!')
    await bot.change_presence(activity=discord.Game(name="Death Stranding"))



try:
    bot.run(TOKEN)
except Exception as err:
    print(f"Error: {err}")