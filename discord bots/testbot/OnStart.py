import discord
from discord.ext import commands

@client.event
async def on_ready():
    activity = discord.Game(name=":help  for commands")
    await client.change_presence(status=discord.Status.online, activity=activity)
    print ('bot is ready')
    print('We have logged in as {0.user}'.format(client))

TOKEN = "OTQyNDU1NDEwMDM4ODIwODY0.Ygkv_w.wWc7Ula-MzNKNw41xdGH9-Mo28c"
client.run((TOKEN), reconnect=True)
