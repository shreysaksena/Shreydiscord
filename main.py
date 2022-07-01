import discord
from discord.ext import commands
import os
import requests
import json
import random
client = commands.Bot(command_prefix = '!')
@client.event 
async def on_ready():
    print("I am ready {0.user}".format(client))
@client.command()
async def ping(ctx):
    await ctx.send('Pong')
@client.command()
async def join(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()  
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data=json.loads(response.text)
    quote= json_data[0]['q']+ "- " + json_data[0]['a']
    return(quote)
sad_words = ["sad","depressed","depressing","cry"]
encourage = ["Cheer up!","Hang in there, you got this!","You are amazing! Don't be sad!"]
@client.event
async def on_message(message):
    await client.process_commands(message)
    msg = message.content
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hello! {}'.format(message.author.name))
    if message.content.startswith('$inspire'):
        quote=get_quote()
        await message.channel.send(quote)
    if any(word in msg.lower() for word in sad_words):
        await message.channel.send(random.choice(encourage))

client.run(os.getenv('TOKEN'))







