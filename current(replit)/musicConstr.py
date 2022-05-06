import discord
from discord.ext import commands
import youtube_dl

from urllib import parse, request
import re

queue = []
search_results = []
url = ''


class music(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("Not in a vc")  # hidden str: 1

        voice_channel = ctx.author.voice.channel

        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)

    @commands.command()
    async def play(self, ctx, url):

        if ctx.voice_client is not None:
            ctx.voice_client.stop()

        if url is None:
            await ctx.send("no link provided")  # hidden str: 2
            return

        # joining:
        if ctx.author.voice is None:
            await ctx.send("Not in a vc")  # hidden str: 3
            return

        voice_channel = ctx.author.voice.channel

        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)
        # joining done

        FFMPEG_OPTIONS = {
            'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        YDL_OPTIONS = {'format': "bestaudio"}
        vc = ctx.voice_client

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            vc.play(source)

    @commands.command()
    async def p(self, ctx, url):

        if ctx.voice_client is not None:
            ctx.voice_client.stop()

        if url is None:
            await ctx.send("No link provided")  # hidden str: 4
            return

        # joining:
        if ctx.author.voice is None:
            await ctx.send("Not in a vc")  # hidden str: 5
            return

        voice_channel = ctx.author.voice.channel

        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)
        # joining done

        FFMPEG_OPTIONS = {
            'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        YDL_OPTIONS = {'format': "bestaudio"}
        vc = ctx.voice_client

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            vc.play(source)

    @commands.command()
    async def pause(self, ctx):
        if ctx.voice_client is not None:
            await ctx.voice_client.pause()
            await ctx.send("paused")  # hidden str: 6

    @commands.command()
    async def resume(self, ctx):
        if ctx.voice_client is not None:
            await ctx.voice_client.resume()
            # hidden str: 7
            await ctx.send("Well done")

    @commands.command()
    async def stop(self, ctx):
        if ctx.voice_client is not None:
            await ctx.voice_client.disconnect()
            await ctx.send("Boring")  # hidden str: 8

    @commands.command()
    async def skip(self, ctx):
        if ctx.voice_client.is_playing():
            ctx.voice_client.stop()
            await ctx.send("emote")  # hidden str: 9
            await ctx.send("Skipped")  # hidden str: 10

        # no funciona por ahora

    @commands.command()
    async def queue(ctx, url):
        global queue

        queue.append(url)
        await ctx.send(f'`{url}` added to queue!')

        # no funciona por ahora

    @commands.command()
    async def remove(ctx, number):
        global queue

        try:
            del(queue[int(number)])
            await ctx.send(f'Cola de reproduccion: `{queue}`')

        except:
            await ctx.send('La cola de reproduccion está vacía o no existe tal indice en la cola de canciones')

        # no funciona por ahora

    @commands.command()
    async def repeat(self, ctx):
        if ctx.voice_client.is_playing():
            # ctx.voice_client.stop()
            await ctx.send("Skipped")  # hidden str: 11


# ================================================================================
        # no funciona por ahora

    @commands.command()
    async def playsearchtest(self, ctx, search):
        global queue

        if ctx.voice_client is not None:
            # ctx.voice_client.stop()
            global search_results

            query_string = parse.urlencode({'search_query': search})
            html_content = request.urlopen(
                'http://www.youtube.com/results?' + query_string)
            search_results = re.findall(
                'watch\?v=(.{11})', html_content.read().decode('utf-8'))
            await ctx.send('emote')  # hidden str: 12
            await ctx.send('RESULTADOS DE BUSQUEDA:')
            for i in range(0, 4):
                await ctx.send('**'+str(i)+'.**' + 'https://www.youtube.com/watch?v=' + search_results[i])


@commands.command(name='1')
async def optOne(self, ctx):
    global url
    queue.append('https://www.youtube.com/watch?v='+search_results[0])
    url = 'https://www.youtube.com/watch?v='+search_results[0]
    await ctx.send('Añadido **(1)** a la cola')
    await doStuffWithUrl(ctx, url)


@commands.command(name='2')
async def optTwo(self, ctx):
    global url
    queue.append('https://www.youtube.com/watch?v='+search_results[1])
    url = 'https://www.youtube.com/watch?v='+search_results[1]
    await ctx.send('Añadido **(2)** a la cola')
    doStuffWithUrl(ctx, url)


@commands.command(name='3')
async def optThree(self, ctx):
    global url
    queue.append('https://www.youtube.com/watch?v='+search_results[2])
    url = 'https://www.youtube.com/watch?v='+search_results[2]
    await ctx.send('Añadido **(3)** a la cola')
    doStuffWithUrl(ctx, url)

# queue.append(url)
# await ctx.send(f'`{url}` added to queue!')


# ================================================================================

    # no funciona por ahora
async def doStuffWithUrl(ctx, url):
    # joining:
    if ctx.author.voice is None:
        await ctx.send("Not in a vc")  # hidden str: 13

    voice_channel = ctx.author.voice.channel

    if ctx.voice_client is None:
        await voice_channel.connect()
    else:
        await ctx.voice_client.move_to(voice_channel)
    # joining done

    FFMPEG_OPTIONS = {
        'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    YDL_OPTIONS = {'format': 'bestaudio/best',
                   'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
                   'restrictfilenames': True,
                   'noplaylist': True,
                   'nocheckcertificate': True,
                   'ignoreerrors': False,
                   'logtostderr': False,
                   'quiet': True,
                   'no_warnings': True}

    vc = ctx.voice_client

    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(url, download=False)
        url2 = info['formats'][0]['url']
        source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
        vc.play(source)

    # await ctx.send('**Now playing:** {}'.format(player.title))
    del(queue[0])

# ================================================================================


def setup(client):
    client.add_cog(music(client))
