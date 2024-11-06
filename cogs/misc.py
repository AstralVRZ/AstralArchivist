import discord
from discord.ext import commands
from colorama import Fore

class misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        return
    
    # Ping command
    @commands.command(name="ping",aliases=["p"],help="Check wether the bot is online with a simple command.")
    async def ping(self, ctx):
        await ctx.send(f"Pong! {round(self.bot.latency*1000)}ms")
        await ctx.message.add_reaction("✅")

async def setup(bot):
    await bot.add_cog(misc(bot))