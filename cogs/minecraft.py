import discord
from discord.ext import commands
from colorama import Fore
import requests
import datetime

embedTime = datetime.datetime.now(datetime.timezone.utc)
embedColor = 5416245
api_player = "https://playerdb.co/api/player/minecraft/"

class minecraft(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        return

    @commands.command(name="minecraftLookup", aliases=["MCNLU","MCLU","MinecraftName"], help="Looks up the minecraft account with the name you give it.")
    async def minecraftLookup(self,ctx, name: str = commands.parameter(description="Minecraft player name.")):
        request_player = requests.get(api_player+name)
        response_player = request_player.json()
        if response_player["success"] == True:
            name = response_player["data"]["player"]["username"]
            UUID = response_player["data"]["player"]["id"]
            embed = discord.Embed(
                title=f"Found minecraft account {name}",
                description=f"Name: {name}\nUUID: {UUID}",
                color=embedColor,
                timestamp=embedTime,
                url=f"https://namemc.com/profile/{name}"
            )
            embed.set_thumbnail(url=f"https://crafthead.net/armor/body/{name}")
            embed.set_footer(text="Minecraft account lookup", icon_url=f"https://crafthead.net/helm/{name}")
            await ctx.send(embed=embed)

        if response_player["success"] == False:
            embed = discord.Embed(
                title="Player not found",
                description=f"No minecraft account with the name `{name}` exists.",
                color=embedColor,
                timestamp=embedTime,
            )
            embed.set_footer(text="Minecraft name lookup")
            await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(minecraft(bot))