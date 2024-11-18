import discord
from discord.ext import commands
from colorama import Fore
import requests
import datetime
from pathlib import Path

filePath= Path('.')
embedTime = datetime.datetime.now(datetime.timezone.utc)
req_user = "https://users.roblox.com/v1/users/"
req_thumbnail = "https://thumbnails.roblox.com/v1/users/avatar-bust"
embedColor = 1645341

class roblox(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        return
    
    @commands.command(name="IDLookUp", aliases=["IDLU"], help="Gets the info from a Roblox profile from the provided ID.")
    async def IDLookUp(self, ctx, id: str = commands.parameter(description="Roblox ID")):
        try:
            id = int(id)
            id = str(id)
            request_user = requests.get(req_user + id)
            response_user = request_user.json()

            if "errors" in response_user:
                if response_user["errors"][0]["code"] == 3:
                    embed = discord.Embed(
                        title="The given ID was not found.",
                        description=f"The ID: `{id}` is not a valid Roblox account ID.",
                        color=embedColor,
                        timestamp=embedTime,
                    )
                    file = discord.File(f"{filePath}/img/roblox.png", filename="roblox.png")
                    embed.set_footer(text="ID Look Up", icon_url="attachment://roblox.png")
                    await ctx.send(file=file, embed=embed)
                    await ctx.message.add_reaction("❌")
            else:
                request_thumbnail = requests.get(f"{req_thumbnail}?userIds={id}&size=352x352&format=Png&isCircular=false")
                response_thumbnail = request_thumbnail.json()

                if response_user["hasVerifiedBadge"] == True:
                    verified = f"{response_user["name"]} is **verified**!"
                if response_user["hasVerifiedBadge"] == False:
                    verified = f"{response_user["name"]} is **not verified**."
                if response_user["isBanned"] == True:
                    banned = f"{response_user["name"]} is **banned**."
                if response_user["isBanned"] == False:
                    banned = f"{response_user["name"]} is **not banned**."
                
                created = response_user["created"]
                created = created[:-4]
                date_time_parts = created.split("T")
                date_parts = date_time_parts[0].split("-")
                rearranged_date = "-".join(date_parts[1:] + date_parts[:1])
                created = f"{rearranged_date}** at **{date_time_parts[1]}"

                embed = discord.Embed(
                    title=f"Roblox: {response_user["displayName"]} (@{response_user["name"]})",
                    description=f"Name: **{response_user["name"]}**\nDisplay name: **{response_user["displayName"]}**\nUser description: {response_user["description"]}\n{verified}\n{banned}\nAccount created on: **{created}**\nUser ID: `{response_user["id"]}`", 
                    color=embedColor,
                    timestamp=embedTime,
                    url=f"https://www.roblox.com/users/{id}/profile"
                )
                embed.set_thumbnail(url=response_thumbnail["data"][0]["imageUrl"])
                file = discord.File(f"{filePath}/img/roblox.png", filename="roblox.png")
                embed.set_footer(text="ID Look Up", icon_url="attachment://roblox.png")
                await ctx.send(file=file,embed=embed)
                await ctx.message.add_reaction("✅")

        except ValueError:
            embed = discord.Embed(
                title="A Roblox ID should only contain numbers.",
                description=f"The ID: `{id}` is not a valid Roblox account ID.",
                color=embedColor,
                timestamp=embedTime,
            )
            file = discord.File(f"{filePath}/img/roblox.png", filename="roblox.png")
            embed.set_footer(text="ID Look Up", icon_url="attachment://roblox.png")
            await ctx.send(file=file, embed=embed)
            await ctx.message.add_reaction("❌")

async def setup(bot):
    await bot.add_cog(roblox(bot))