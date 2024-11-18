import discord
from discord.ext import commands
from colorama import Fore
import random
from pathlib import Path
filePath= Path('.')
delay = int(2)

class dice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        return

    @commands.command(name="D4", help="Four sided dice, rolls a number between 1 and 4.")
    async def D4(self,ctx):
        roll = random.randint(1,4)
        with open(rf'{filePath}/img/dice.gif', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture, delete_after=delay)
        await ctx.send(f"{ctx.author.display_name} rolled a {roll}")
        await ctx.message.add_reaction("✅")

    @commands.command(name="D6", help="Normal dice, rolls a number between 1 and 6.")
    async def D6(self,ctx):
        roll = random.randint(1,6)
        with open(rf'{filePath}/img/dice.gif', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture, delete_after=delay)
        await ctx.send(f"{ctx.author.display_name} rolled a {roll}")
        await ctx.message.add_reaction("✅")

    @commands.command(name="D10", help="Ten sided dice, rolls a number between 1 and 10.")
    async def D10(self,ctx):
        roll = random.randint(1,10)
        with open(rf'{filePath}/img/dice.gif', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture, delete_after=delay)
        await ctx.send(f"{ctx.author.display_name} rolled a {roll}")
        await ctx.message.add_reaction("✅")
    
    @commands.command(name="D20", help="Twenty sided dice, rolls a number between 1 and 20.")
    async def D20(self,ctx):
        roll = random.randint(1,20)
        with open(rf'{filePath}/img/dice.gif', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture, delete_after=delay)
        await ctx.send(f"{ctx.author.display_name} rolled a {roll}")
        await ctx.message.add_reaction("✅")

async def setup(bot):
    await bot.add_cog(dice(bot))