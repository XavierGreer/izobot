import os
import random
import discord
from discord.ext import commands
import music


token = os.getenv("DISCORD_TOKEN")
my_guild = os.getenv("DISCORD_GUILD")

intents = discord.Intents.all()
# client = discord.Client(intents=intents)
cogs = [music]
prefix = '-'
bot = commands.Bot(command_prefix=prefix, intents=intents)

for i in range(len(cogs)):
    cogs[i].setup(bot)



# @bot.event
# async def on_ready():
#     for guild in bot.guilds:
#         if guild.name == my_guild:
#             break
#
#         print(
#             f"{bot.user} is connected to the following guild:\n"
#             f"{guild.name}(id: {guild.id})"
#         )
#
#
# @bot.command()
# async def join(ctx):
#     channel = ctx.author.voice.channel
#     await channel.connect()
#
#
# @bot.command()
# async def leave(ctx):
#     await ctx.voice_client.disconnect()
#
# @bot.event
# async def on_message(message):
#     if message.author == bot.user:
#         return
#
#     message_content = message.content.lower()
#     if "flip a coin" in message_content:
#         rand_int = random.randint(0, 1)
#         if rand_int == 0:
#             results = "Heads"
#         else:
#             results = "Tails"
#         await message.channel.send(results)

bot.run(token)