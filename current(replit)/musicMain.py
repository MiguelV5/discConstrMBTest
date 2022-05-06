import os
import discord
from discord.ext import commands
import musicHandler

cogs = [musicHandler]

client = commands.Bot(command_prefix='?', intents=discord.Intents.all(
), description='Bot chancludo de miguel')

for i in range(len(cogs)):
    cogs[i].setup(client)


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="Bot chancludo que pone musica"))
    print('Bot is ready to work.')

# @client.event
# async def on_voice_state_update():
#  await client.change_presence(activity = discord.Game(name="Bot chancludo que pone musica"))
#  print('Bot is ready to work.')

client.run(os.environ['TOKEN'])
