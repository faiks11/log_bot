import discord
from discord.ext import commands
from config import settings
import datetime
from datetime import datetime

bot = commands.Bot(command_prefix=settings["prefix"])
token = settings['token']

@bot.event
async def on_ready():
    print('БОТ ВКЛЮЧЕН')

@bot.event
async def on_message(message):
    date_now = str(datetime.now())
    build_log = '[{0}]'.format(date_now) + '[Category: {0}]'.format(message.channel.name) + '[NSFW channel: {0}]'.format(message.channel.nsfw) + ' Сообщение {0.author}: {0.content}'.format(message)
    if message.attachments != []:
        build_log = build_log + " !!<<ПОЛЬЗОВАТЕЛЬ ПРИСЛАЛ КАРТИНКУ(И) - ФАЙЛ(Ы), URL: {0} >>!!".format(message.attachments)

    print(build_log)
    with open("LOG.txt", "a") as file:
        file.write(build_log + "\n")



bot.run(token)