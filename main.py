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
        if (re.search(r"([+\d])", ctx.message.content)):
            await ctx.send(f'<@{ctx.message.author.id}> have added __ points to <@{ctx.message.mentions[0].id}>')
    else:
        await ctx.send(f'<@{ctx.message.author.id}> You may only mention one person at a time!')
        return
    
client.run(token)