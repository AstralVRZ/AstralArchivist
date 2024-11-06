import discord
from discord.ext import commands
from colorama import Fore

# REPLACE THE PLACEHOLDER WITH THE NAME OF THE COG FOR BEST PRACTICE
class PLACEHOLDER(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        return

async def setup(bot):
    await bot.add_cog(PLACEHOLDER(bot))