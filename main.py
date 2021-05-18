import os
import discord
import requests
import json

client=discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

async def on_message(message):
    if msg.startswith('$hello'):
        await message.channel.send("Hello Hippo")

client.run(os.environ['TOKEN'])
