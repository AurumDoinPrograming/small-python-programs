import discord
from discord.ext import commands

TOKEN = "OTQyMTMyMTY4OTIxMDg4MDcw.YggC9Q.7ZBrrmuNtDhMW7Bayjz_LDsHKSQ" 

client = commands.Bot(command_prefix=commands.when_mentioned_or("!r "), case_insensitive=True)
#client.remove_command('help')

def check_team(ctx):
    return client.get_guild(888399141686894612).get_role(888403456765861888) in ctx.author.roles 

@client.event
async def on_ready():
    activity = discord.Game(name=":help  for commands")
    await client.change_presence(status=discord.Status.online, activity=activity)
    print ('bot is ready')
    print('We have logged in as {0.user}'.format(client))
    print('f21 is now Online')


@client.event
async def on_message(message):
    if message.author.id == client.user.id:
        return
    
    if message.author != message.author.bot:
        if not message.guild:
            await client.get_guild(888399141686894612).get_channel(942134260733710397).send(f"User meniton {message.author.mention}\nUsername: {message.author}\nUser-ID: {message.author.id}\n\n__**User Message:**__\n{message.content}")
    
    await client.process_commands(message)

@client.command()
@commands.check(check_team)
async def dm(ctx, member: discord.Member, *, text):
    await member.send(text)
    print('message sent')

@client.event # Bot reconnect
async def on_resumed():
    print('reconnected')
    
@client.command()
async def embed(ctx):
    embed=discord.Embed(title="Sample Embed", url="https://realdrewdata.medium.com/", description="This is an embed that will show how to build an embed and the different components", color=0xFF5733)
    await ctx.send(embed=embed)
    
##replace "DiscordBot_Token" with your bot token
client.run(('OTQyMTMyMTY4OTIxMDg4MDcw.YggC9Q.7ZBrrmuNtDhMW7Bayjz_LDsHKSQ'), reconnect=True) # Bot reconnect