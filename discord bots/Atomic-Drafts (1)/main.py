import discord
from discord.ext import commands

TOKEN = "token" 

client = commands.Bot(command_prefix=commands.when_mentioned_or("!r "), case_insensitive=True)

def check_team(ctx):
    return client.get_guild(939933394240929877).get_role(939935843597025400) in ctx.author.roles 

@client.event
async def on_connect():
    print('We have logged in as {0.user}'.format(client))
    print('Atomic Drafts is now Online')

@client.event
async def on_message(message):
    if message.author.id == client.user.id:
        return
    
    if message.author != message.author.bot:
        if not message.guild:
            await client.get_guild(939933394240929877).get_channel(942056388992061511).send(f"User meniton {message.author.mention}\nUsername: {message.author}\nUser-ID: {message.author.id}\n\n__**User Message:**__\n{message.content}")
    
    await client.process_commands(message)

@client.command()
@commands.check(check_team)
async def dm(ctx, member: discord.Member, *, text):
    await member.send(text)
    print('message sent')

@client.command()
async def ping(ctx):
    print('ping used')
    await ctx.send(f'Ping is `{round(client.latency * 1000)}` ms ')

@client.event 
async def on_resumed():
    print('reconnected')
client.run(('Token'), reconnect=True) # Bot reconnect
