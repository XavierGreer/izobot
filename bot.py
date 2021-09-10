import os
from datetime import datetime
import random
import discord
from discord.ext import commands
from discord import Embed
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


@bot.event
async def on_ready():
    channel = bot.get_channel(885557849126744114)

    bot.ready = True
    bot.guild = bot.get_guild(407625054894030848)

    for guild in bot.guilds:
        if guild.name == my_guild:
            break

        print(
            f"{bot.user} is connected to the following guild:\n"
            f"{guild.name}(id: {guild.id})"
        )

    # embed = Embed(title="Now Online!", description="Description goes here.", colour=0xFF0000, timestamp=datetime.utcnow())
    # fields = [("Name", "Value", True),
    #           ("Another Field", "This Field is next to the other one.", True),
    #           ("Non-inline field", "This field will appear on its own row.", False)]
    # for name, value, inline in fields:
    #     embed.add_field(name=name,value=value,inline=inline)
    # embed.set_author(name="IzoBot")
    # embed.set_footer(text="This is a footer!")
    # #embed.set_thumbnail(url=bot.guild.icon_url)
    # #embed.set_image(url=bot.guild.icon_url)
    # await channel.send(embed=embed)
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