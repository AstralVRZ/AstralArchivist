import discord
from discord.ext import commands
from colorama import Fore
import random

class misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        return
    
    # Ping command
    @commands.command(name="ping", aliases=["p"], help="Check wether the bot is online with a simple command.")
    async def ping(self, ctx):
        await ctx.send(f"Pong! {round(self.bot.latency*1000)}ms")
        await ctx.message.add_reaction("✅")

    @commands.command(name="random", aliases=["rand","randint","roll","number","randomnumber"], help="Generates a random number between two numbers you give it.")
    async def random(self, ctx, lowint: str = commands.parameter(description="Lowest number"), highint: str = commands.parameter(description="Highest number")):
        try:
            lowint = int(lowint)
            highint = int(highint)
            if lowint > highint:
                await ctx.send(f"Hmmm that didn't work. Did you put the lower number first?")
                await ctx.message.add_reaction("❌")
            else:
                number = random.randint(lowint, highint)
                await ctx.send(f"You rolled **{number}** out of {lowint} and {highint}")
                await ctx.message.add_reaction("✅")
        except ValueError:
            await ctx.send(f"Hmmm that didn't work. Did you put in two numbers?")
            await ctx.message.add_reaction("❌")
    @random.error
    async def random_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Hmmm that didn't work. Did you put in two numbers?")
            await ctx.message.add_reaction("❌")

async def setup(bot):
    await bot.add_cog(misc(bot))