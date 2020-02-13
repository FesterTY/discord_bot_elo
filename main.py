import discord
import re
from discord.ext import commands

client = commands.Bot(command_prefix = 'e!')

f = open("token.txt", "r")
token = f.read()
f.close()

@client.event
async def on_ready():
    print("Bot is ready.")

@client.command()
async def elo(ctx):
    if (len(ctx.message.mentions) == 1):
        points = re.search(r"(?<=[+])[\w+]+", ctx.message.content)
        if (points is None):
            try:
                points = re.search(r"(?<=[-])[\w+]+", ctx.message.content)
            except:
                await ctx.send(f'Could not add the points as you have not inserted the numbers or there\'s a whitespace')
                return
        if (re.search(r"(\+[0-9]+)", ctx.message.content)):
            await ctx.send(f'<@{ctx.message.author.id}> have given {points.group(0)} points to <@{ctx.message.mentions[0].id}>')
        elif (re.search(r"(\-[0-9]+)", ctx.message.content)):
            await ctx.send(f'<@{ctx.message.author.id}> have subtracted {points.group(0)} points from <@{ctx.message.mentions[0].id}>')
        else:
            await ctx.send(f'Please make sure you put in your symbols (+/-).')
    else:
        await ctx.send(f'<@{ctx.message.author.id}> You may only mention one person at a time!')
        return

client.run(token)