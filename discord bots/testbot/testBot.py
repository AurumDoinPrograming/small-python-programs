import discord
from discord.ext import commands

client = commands.Bot(command_prefix=commands.when_mentioned_or("!r "), case_insensitive=True)
#client.remove_command('help')

guild = 676319495127564288
role = 699527624208285777
channel = 676319927870947330

def check_team(ctx):
    return client.get_guild(guild).get_role(role) in ctx.author.roles 

#exec(open('OnStart.py'))

@client.event
async def on_ready():
    activity = discord.Game(name="N00B")
    await client.change_presence(status=discord.Status.online, activity=activity)
    print ('bot is ready')
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author.id == client.user.id:
        return
    
    if message.author != message.author.bot:
        if not message.guild:
            await client.get_guild(guild).get_channel(channel).send(f"User meniton {message.author.mention}\nUsername: {message.author}\nUser-ID: {message.author.id}\n\n__**User Message:**__\n{message.content}")
    await client.process_commands(message)

@client.command()
@commands.check(check_team)
async def dm(ctx, member: discord.Member, *, text):
    await member.send(text)
    print('message sent')

@client.event
async def on_resumed():
    print('reconnected')

    

client.run(('TOKEN'), reconnect=True)
