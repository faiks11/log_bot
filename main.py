import discord
from discord.ext import commands
from config import settings
import datetime
from datetime import datetime

client = discord.Client()
bot = commands.Bot(command_prefix=settings["prefix"])
bot_name = "Faiks#3970"
token = settings['token']


@bot.event
async def on_ready():
    print('Я ГОТОВ ЕБАТЬ ГУСЕЙ')


@bot.command()
async def hello(ctx):
    author = ctx.message.author
    await ctx.send(f"Hello, {author.mention}!")

@bot.command
async def menu(ctx):
    embed = discord.Embed(color=0xff9900, title='Help menu')
    embed.add_field(name='hello', value='bot say you hi!', inline=True)
    await ctx.send(embed=embed)

"""@bot.event
async def on_message(message):
    name_author = message.author.name + '#' + message.author.discriminator
    if message.channel.name == "основной" and name_author != bot_name:
        embed = discord.Embed(color=0xff9911, title='ХУЭЛП')
        embed.add_field(name='ПОШЁЛ НАХУЙ', value='ПОШЁЛ НАХУЙ ХУИЛА', inline=True)
        await message.channel.send(embed=embed)"""

bot.run(token)