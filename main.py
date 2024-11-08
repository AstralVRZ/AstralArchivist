import discord
from discord.ext import commands
from colorama import Fore
import datetime
import os
import asyncio

with open("token", "r") as file:
    token = str(file.read())

bot = commands.Bot(command_prefix="$", intents=discord.Intents.all(), case_insensitive=True)
embedColor = 16765404
embedTime = datetime.datetime.now(datetime.timezone.utc)

# Info embed on run + cogs
@bot.event
async def on_ready():
    # Info + embed
    print(Fore.GREEN + f"Bot logged in as", Fore.MAGENTA + str(bot.user), Fore.GREEN + "with the the ID:", Fore.MAGENTA + str(bot.user.id))
    for guild in bot.guilds:
        print(Fore.GREEN + f"Connected to", Fore.MAGENTA + str(guild), Fore.GREEN + "ID:", Fore.MAGENTA + str(guild.id))
    embed = discord.Embed(title=f"{bot.user.name} is now online!", description=f"With the ID: {bot.user.id}", color=embedColor, timestamp=embedTime)
    embed.set_footer(text="AstralArchivist", icon_url=bot.user.display_avatar)
    channel = bot.get_channel(1239535111314210887)
    await channel.send(embed=embed)

    # Load cogs
    print(Fore.GREEN + "Loading cogs:")
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")
            print(f"    - Loaded {Fore.MAGENTA + filename[:-3] + Fore.GREEN} cog")
    print(Fore.GREEN + "Cogs loaded successfully.")  

# Send embed on user join
@bot.event
async def on_member_join(member):
    # Fetch the role by its ID
    role = discord.utils.get(member.guild.roles, id=987314405937152125)
    await member.add_roles(role)
    embed = discord.Embed(title=f"{member} has entered The Dreamscape!", description=f"Welcome to The Dreamscape Be sure to read our [TOS](https://astralvrz.github.io/TOS/)!", color=embedColor, timestamp=embedTime)
    embed.set_footer(text="AstralArchivist", icon_url=member.display_avatar)
    channel = bot.get_channel(987314407170265123)
    await channel.send(embed=embed)

async def main():
    async with bot:
        await bot.start(token)

asyncio.run(main())
