import discord
from discord.ext import commands

import json
import validators

import cheinsteinpy
import re
from jinja2 import Environment, FileSystemLoader, BaseLoader


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
                    print("Searching....")
                    env = Environment(loader=FileSystemLoader('templates/'))
                    temp = env.get_template('chapterQuestion.html')
                    results_filename = "answers.html"

                    total = len(answerRaw)
                    print(f'total steps: {total}')
                    reg = '(https?://+)'
                    steps = {step + 1: str(re.subn('png', 'png">', str(re.sub(
                        reg, '<img src="https://', answerRaw[step]))))[2:-5] for step in range(0, total)}
                    print(steps)
                    context = {
                        'problemTitle': questionRaw,
                        'steps': steps,
                        'totalSteps': total,
                    }
                    with open(results_filename, mode="w", encoding="utf-8") as results:
                        results.write(temp.render(context))
                        print(f'... wrote {results_filename}')


                    await ctx.reply(file=discord.File('answers.html'))




async def setup(bot):
    await bot.add_cog(Commands(bot))
