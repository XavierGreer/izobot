import discord
from datetime import datetime
from discord.ext import commands
import youtube_dl
from discord import Embed

class music(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def join(self,ctx):
        if ctx.author.voice is None:
            await ctx.send("No one is in the voice channel.")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)

    @commands.command()
    async def disconnect(self,ctx):
        await ctx.send("Goodbye!")
        await ctx.voice_client.disconnect()

    @commands.command()
    async def play(self, ctx, url):
        # ctx.voice_client.stop()
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        YDL_OPTIONS = {'format': "bestaudio"}
        vc = ctx.voice_client

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)

            embed = Embed(title=url2, description="Description goes here.", colour=0xFF0000,
                          timestamp=datetime.utcnow())
            fields = [("Name", "Value", True),
                      ("Another Field", "This Field is next to the other one.", True),
                      ("Non-inline field", "This field will appear on its own row.", False)]
            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)
            embed.set_author(name="IzoBot")
            embed.set_footer(text="This is a footer!")
            # embed.set_thumbnail(url=bot.guild.icon_url)
            # embed.set_image(url=bot.guild.icon_url)
            await ctx.send(embed=embed)
            vc.play(source)

    @commands.command()
    async def pause(self,ctx):
        await ctx.send('Paused ⏸️')
        await ctx.voice_client.pause()

    @commands.command()
    async def resume(self, ctx):
        await ctx.send('Resuming ▶️')
        await ctx.voice_client.resume()


def setup(client):
    client.add_cog(music(client))