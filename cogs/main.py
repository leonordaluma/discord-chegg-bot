import discord
from discord.ext import commands

import json
import validators

import cheinsteinpy
from core.utils import sendDefer
from core.renderSteps import format_steps, write_to_template


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
                questionRaw = cheinsteinpy.question(url, self.cookie, self.userAgent)
                searchingEmbed = discord.Embed(title="Searching...", color=0xeb7100)
                searchingEmbed.set_footer(text="This may take up to 10 seconds.")
                searchingMessage = await ctx.reply(embed=searchingEmbed)

                if answerRaw is None:
                    errorEmbed = discord.Embed(
                        title="Error", description="Something went wrong or there was no solution.", color=0xff4f4f)
                    print('No answer found!')
                else:
                    total = len(answerRaw)
                    steps = format_steps(answerRaw, total)
                    print(steps)
                    context = {
                        'problemTitle': questionRaw,
                        'steps': steps,
                        'totalSteps': total,
                    }
                    write_to_template(context)
                    await ctx.reply(file=discord.File('answers.html'))




async def setup(bot):
    await bot.add_cog(Commands(bot))
