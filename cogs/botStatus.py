import discord
from discord.ext import commands

class BotStatus(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Bot is online!')
        await self.bot.change_presence(activity=discord.Game(name="Death Stranding"))
    
    

    


async def setup(bot):
    await bot.add_cog(BotStatus(bot))
        

