import discord
from discord.ext import commands
from colorama import Fore
import datetime

with open('token','r') as file:
    token=str(file.read())

AP='1186667999915159562'

bot = commands.Bot(command_prefix='$', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(Fore.GREEN + f'Bot logged in as', Fore.MAGENTA + str(bot.user), Fore.GREEN + 'with the the ID:', Fore.MAGENTA + str(bot.user.id))
    for guild in bot.guilds:
        print(Fore.GREEN + f'Connected to', Fore.MAGENTA + str(guild), Fore.GREEN + 'ID:', Fore.MAGENTA + str(guild.id))
    embed = discord.Embed(title=f'{bot.user} is now online! With the ID: {bot.user.id}',color=9055202,timestamp=datetime.datetime.now(datetime.timezone.utc))
    embed.set_footer(text='placeholder', icon_url=bot.user.display_avatar)

@bot.command(name='ping',aliases=['p'],help='Check wether the bot is online with a simple command')
async def ping(ctx):
    await ctx.send('Pong!')
    await ctx.message.add_reaction('✅')


bot.run(token)