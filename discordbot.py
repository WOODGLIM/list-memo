from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']





@bot.command()
async def ping(ctx):
    #絶対パスじゃないやつにする↓
    path = os.path.dirname(__file__)
    file = path + "/list.txt"

    f = open(file, 'r', encoding='UTF-8')
    for data in f:
        text = data.rstrip('\n')
        await ctx.send(text)

    f.close()


bot.run(token)
