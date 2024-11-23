import discord
from discord.ext import commands
from colorama import Fore
import requests
import datetime
from pathlib import Path
import json

filePath= Path('.')
embedTime = datetime.datetime.now(datetime.timezone.utc)
api_user = "https://users.roblox.com/v1/"
api_thumbnail = "https://thumbnails.roblox.com/v1/users/avatar-bust"
embedColor = 1645341

class roblox(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        return
    
    @commands.command(name="nameLookup", aliases=["NLU"],  help="Gets the info from a roblox profile from the provided username.")
    async def nameLookup(sel, ctx, name: str = commands.parameter(description="Roblox username")):
        request_body = {'usernames': [name],'excludeBannedUsers': False}
        headers = {'Content-Type': 'application/json','Accept': 'application/json'}
        json_data = json.dumps(request_body)
        response = requests.post(api_user+"usernames/users", headers=headers, data=json_data)
        response_user = json.loads(response.text)
        if len(response_user['data']) > 0:
            id = str(response_user['data'][0]['id'])
            request_user = requests.get(api_user + "users/" + id)
            response_user = request_user.json()
            request_thumbnail = requests.get(f"{api_thumbnail}?userIds={id}&size=352x352&format=Png&isCircular=false")
            response_thumbnail = request_thumbnail.json()

            if response_user["hasVerifiedBadge"] == True:
                verified = f"{response_user["name"]} is **verified**! <:RBLXverified:1308913820835643493>"
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
            embed.set_footer(text="Name lookup", icon_url="attachment://roblox.png")
            await ctx.send(file=file,embed=embed)
            await ctx.message.add_reaction("✅")
        else:
            embed = discord.Embed(
                title="No account found.",
                description=f"No account with the name `{name}` could be found on Roblox",
                color=embedColor,
                timestamp=embedTime,
            )
            icon = discord.File(f"{filePath}/img/roblox.png", filename="roblox.png")
            embed.set_footer(text="Name lookup", icon_url="attachment://roblox.png")
            na = discord.File(f"{filePath}/img/na.png", filename="na.png")
            embed.set_thumbnail(url="attachment://na.png")
            await ctx.send(files=[icon, na], embed=embed)
            await ctx.message.add_reaction("❌")

    @commands.command(name="IDLookUp", aliases=["IDLU"], help="Gets the info from a Roblox profile from the provided ID.")
    async def IDLookUp(self, ctx, id: str = commands.parameter(description="Roblox ID")):
        try:
            id = int(id)
            id = str(id)
            request_user = requests.get(api_user + "users/" + id)
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
                    embed.set_footer(text="ID lookup", icon_url="attachment://roblox.png")
                    await ctx.send(file=file, embed=embed)
                    await ctx.message.add_reaction("❌")
            else:
                request_thumbnail = requests.get(f"{api_thumbnail}?userIds={id}&size=352x352&format=Png&isCircular=false")
                response_thumbnail = request_thumbnail.json()

                if response_user["hasVerifiedBadge"] == True:
                    verified = f"{response_user["name"]} is **verified**! <:RBLXverified:1308913820835643493>"
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
                embed.set_footer(text="ID Lookup", icon_url="attachment://roblox.png")
                await ctx.send(file=file,embed=embed)
                await ctx.message.add_reaction("✅")

        except ValueError:
            embed = discord.Embed(
                title="A Roblox ID should only contain numbers.",
                description=f"The ID: `{id}` is not a valid Roblox account ID.",
                color=embedColor,
                timestamp=embedTime,
            )
            icon = discord.File(f"{filePath}/img/roblox.png", filename="roblox.png")
            embed.set_footer(text="ID lookup", icon_url="attachment://roblox.png")
            na = discord.File(f"{filePath}/img/na.png", filename="na.png")
            embed.set_thumbnail(url="attachment://na.png")
            await ctx.send(files=[icon, na], embed=embed)
            await ctx.message.add_reaction("❌")

async def setup(bot):
    await bot.add_cog(roblox(bot))