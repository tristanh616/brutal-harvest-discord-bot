import discord
from discord.ext import commands
from discord.ext.commands import Context

import aiohttp
import random

class BrutalCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def Example(self, ctx):
        """Example Command"""
        example = "This is an example command" 
        embed = discord.Embed(title="Example", description=example)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(BrutalCommands(bot))