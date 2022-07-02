import discord
from discord.ext import commands
import os
import requests
import json
import random
import time
import asyncio
from urllib import request, parse
import giphy_client
from giphy_client.rest import ApiException
from discord import Member
client = commands.Bot(command_prefix = '!')
@client.event 
async def on_ready():
    print("I am ready {0.user}".format(client))
@client.command()
async def ping(ctx):
   await ctx.send(f'Pong = {round(client.latency * 1000)}ms')
@client.command()
async def mystatus(ctx,member:Member):
    await client.say(str(member.status))
    
@client.command()
async def join(ctx):
    if(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
@client.command()
async def leave(ctx,member):
    if(ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
@client.command()
async def image(ctx):
    api_call = "https://picsum.photos/1920/1080"
    request.urlretrieve(api_call,"img.png")
    await ctx.channel.send(file=discord.File('img.png'))
    time.sleep(2)
@client.command()
async def gif(ctx,*,q="Beautiful"):
    api_key = '6JyT980VxutVdk3hN2jLA5A2NzxN5xZW'
    api_call = giphy_client.DefaultApi()
    try:
        api_response = api_call.gifs_search_get(api_key,q,limit=15)
        lst = list(api_response.data)
        gifff = random.choice(lst)
        await ctx.channel.send(gifff.embed_url)
        time.sleep(2)
    except ApiException as e:
        print("Exception when calling api")
@client.command()
async def sticker(ctx,*,q="Beautiful"):
    api_key = '6JyT980VxutVdk3hN2jLA5A2NzxN5xZW'
    api_call = giphy_client.DefaultApi()
    try:
        api_response = api_call.stickers_search_get(api_key,q,limit=15)
        lst = list(api_response.data)
        gifff = random.choice(lst)
        await ctx.channel.send(gifff.embed_url)
        time.sleep(2)
    except ApiException as e:
        print("Exception when calling api")
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data=json.loads(response.text)
    quote= json_data[0]['q']+ "- " + json_data[0]['a']
    return(quote)
@client.command()
async def inspire(ctx):
    quote=get_quote()
    await ctx.channel.send(quote)
@client.command()
async def hello(ctx):
    await ctx.channel.send('Hello {}!'.format(ctx.message.author.mention))
sad_words = ["sad","depressed","depressing","cry"]
encourage = ["Cheer up!","Hang in there, you got this!","You are amazing! Don't be sad!"]
@client.event
async def on_message(message):
    await client.process_commands(message)
    msg = message.content
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hello {}!'.format(message.author.name))
    if message.content.startswith('$inspire'):
        quote=get_quote()
        await message.channel.send(quote)
    if any(word in msg.lower() for word in sad_words):
        await message.channel.send(random.choice(encourage))
    

client.run(os.getenv('TOKEN'))









