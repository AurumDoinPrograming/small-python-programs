import discord 
import os
from discord.ext import commands

#cfgfile = open(config.txt, "r")
client = discord.Client()
bot = commands.Bot(command_prefix="!")


@bot.command(name="hello")
async def hello_world(ctx: commands.Context):
    await ctx.send("Hello, world!" )
    print('hello command was used by')

@bot.command(name="ping")
async def ping(ctx: commands.Context):
    await ctx.send(f"ping is ``{round(bot.latency * 1000)}ms" '``')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('test'):
        await message.channel.send('Test confirmed!')
        message.channel.send
        print('hello command was used')

    elif message.content.startswith('hjelp'):
      await message.channel.send("Dette er Norges hjelp komando ")
      message.channel.send
      print('help command was used')

@bot.command(name="123")
async def on_message(message):
    if message.content.startswith('best'):
        user_id = "201909896357216256"
        await message.channel.send.ctx(f"<@{user_id}> is the best")

@client.event() #Replace 'client' with whatever neccesary
async def on_command_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArguments):
    # Replace MissingRequiredArguments with your error
    ctx.send("Please pass all required arguments")

print('bot is running')
bot.run("TOKEN")
