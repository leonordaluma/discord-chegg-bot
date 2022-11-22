import discord
from discord.ext import commands

import json
import validators

import cheinsteinpy

with open("config.json", "r") as f:
    config = json.load(f)

with open("cookie.txt", 'r') as f:
    cookieTxt = f.read()


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.cookie = cookieTxt
        self.userAgent = config['userAgent']

    @commands.command(name='search')
    async def search(self, ctx, url=None):
        if url is not None:
            if validators.url(url) == True:
                answerRaw = cheinsteinpy.answer(url, self.cookie, self.userAgent)

                if answerRaw is None:
                    errorEmbed = discord.Embed(
                        title="Error", description="Something went wrong or there was no solution.", color=0xff4f4f)
                    await ctx.send(embed=errorEmbed)
                    print('No answer found!')
                else:
                    for count, step in enumerate(answerRaw):
                        count+=1
                        stepEmbed = discord.Embed(title=f'Step {str(count)}', color=0xeb7100)
                        description = ""
                        for word in step.split():
                            if validators.url(word):
                                if(len(description) > 0):
                                    await ctx.send(description)
                                await ctx.send(word)
                                description = ""
                            else:
                                description = description + word + " "
                    if (len(description) > 0):
                        await ctx.send(description)



async def setup(bot):
    await bot.add_cog(Commands(bot))
