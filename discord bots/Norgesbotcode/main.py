import discord
from discord.ext import commands

TOKEN = "OTMzMzkyMzgxNDYwNDgwMDYw.Yeg3ZQ.SAI_aXL4ync-jSa3EPO0g0coWME" 

client = commands.Bot(command_prefix=commands.when_mentioned_or("!r "), case_insensitive=True)
#client.remove_command('help')

def check_team(ctx):
    return client.get_guild(931669806959173702).get_role(931670266097049700) in ctx.author.roles 

@client.event
async def on_ready():
    activity = discord.Game(name=":help  for commands")
    await client.change_presence(status=discord.Status.online, activity=activity)
    print ('bot is ready')
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author.id == client.user.id:
        return
    
    if message.author != message.author.bot:
        if not message.guild:
            await client.get_guild(931669806959173702).get_channel(933049111878467605).send(f"User meniton {message.author.mention}\nUsername: {message.author}\nUser-ID: {message.author.id}\n\n__**User Message:**__\n{message.content}")
    
    await client.process_commands(message)

@client.command()
@commands.check(check_team)
async def dm(ctx, member: discord.Member, *, text):
    await member.send(text)
    print('message sent')

@client.event
async def on_resumed():
    print('reconnected')
    

client.run(('OTMzMzkyMzgxNDYwNDgwMDYw.Yeg3ZQ.SAI_aXL4ync-jSa3EPO0g0coWME'), reconnect=True)