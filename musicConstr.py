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
      await ctx.send("No estás en un canal de voz ome bobotroilo")

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
      await ctx.send("Le faltó mandarme un link ome lacra :juanDeformao:")
      return
  
    #joining:
    if ctx.author.voice is None:
      await ctx.send("No estás en un canal de voz ome bobotroilo")
      return

    voice_channel = ctx.author.voice.channel

    if ctx.voice_client is None:
      await voice_channel.connect()
    else:
      await ctx.voice_client.move_to(voice_channel)
    #joining done
    
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    YDL_OPTIONS = {'format': "bestaudio"}
    vc = ctx.voice_client

    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
      info = ydl.extract_info(url, download = False)
      url2 = info['formats'][0]['url']
      source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
      vc.play(source)


  @commands.command()
  async def p(self, ctx, url):

    if ctx.voice_client is not None:
      ctx.voice_client.stop()

    if url is None:
      await ctx.send("Le faltó mandarme un link ome lacra :juanDeformao:")
      return
  
    #joining:
    if ctx.author.voice is None:
      await ctx.send("No estás en un canal de voz ome bobotroilo")
      return

    voice_channel = ctx.author.voice.channel

    if ctx.voice_client is None:
      await voice_channel.connect()
    else:
      await ctx.voice_client.move_to(voice_channel)
    #joining done
    
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    YDL_OPTIONS = {'format': "bestaudio"}
    vc = ctx.voice_client

    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
      info = ydl.extract_info(url, download = False)
      url2 = info['formats'][0]['url']
      source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
      vc.play(source)



  @commands.command()
  async def pause(self, ctx):
    if ctx.voice_client is not None:
      await ctx.voice_client.pause()
      await ctx.send("Qué me pausás ome laringorido")

  @commands.command()
  async def resume(self, ctx):
    if ctx.voice_client is not None:
      await ctx.voice_client.resume()
      await ctx.send("Eso eso asi es que es :juanDeformao:")

  @commands.command()
  async def stop(self, ctx):
    if ctx.voice_client is not None:
      await ctx.voice_client.disconnect()
      await ctx.send("Chino tan aburrido")
  
  @commands.command()
  async def skip(self, ctx):
    if  ctx.voice_client.is_playing():
      ctx.voice_client.stop()
      await ctx.send(":zorroDeformao:")
      await ctx.send("Skipeao")
  


    #no funciona por ahora
  @commands.command()
  async def queue(ctx, url):
    global queue

    queue.append(url)
    await ctx.send(f'`{url}` added to queue!')


    #no funciona por ahora
  @commands.command()
  async def remove(ctx, number):
    global queue

    try:
      del(queue[int(number)])
      await ctx.send(f'Cola de reproduccion: `{queue}`')
    
    except:
      await ctx.send('La cola de reproduccion está vacía o no existe tal indice en la cola de canciones')


    #no funciona por ahora
  @commands.command()
  async def repeat(self, ctx):
    if  ctx.voice_client.is_playing():
      #ctx.voice_client.stop()
      await ctx.send("Skipeao :juanDeformao:")



#================================================================================
    #no funciona por ahora

  @commands.command()
  async def playsearchtest(self, ctx, search):
    global queue

    if ctx.voice_client is not None:
      #ctx.voice_client.stop()
      global search_results
    
      query_string = parse.urlencode({'search_query': search})
      html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
      search_results = re.findall('watch\?v=(.{11})',html_content.read().decode('utf-8'))
      await ctx.send(':zorroDeformao:')
      await ctx.send('RESULTADOS DE BUSQUEDA:')
      for i in range(0,4):
        await ctx.send('**'+str(i)+'.**' + 'https://www.youtube.com/watch?v=' + search_results[i])
      
@commands.command(name = '1')
async def optOne(self, ctx):
  global url
  queue.append('https://www.youtube.com/watch?v='+search_results[0])
  url = 'https://www.youtube.com/watch?v='+search_results[0]
  await ctx.send('Añadido **(1)** a la cola')
  await doStuffWithUrl(ctx, url)
@commands.command(name = '2')
async def optTwo(self, ctx):
  global url        
  queue.append('https://www.youtube.com/watch?v='+search_results[1])
  url = 'https://www.youtube.com/watch?v='+search_results[1]
  await ctx.send('Añadido **(2)** a la cola')
  doStuffWithUrl(ctx, url)
@commands.command(name = '3')
async def optThree(self, ctx):
  global url
  queue.append('https://www.youtube.com/watch?v='+search_results[2])
  url = 'https://www.youtube.com/watch?v='+search_results[2]
  await ctx.send('Añadido **(3)** a la cola')
  doStuffWithUrl(ctx, url)
  
#queue.append(url)
#await ctx.send(f'`{url}` added to queue!')

  
    

#================================================================================
    
    #no funciona por ahora
async def doStuffWithUrl(ctx, url):
#joining:
    if ctx.author.voice is None:
      await ctx.send("No estás en un canal de voz ome bobotroilo")

    voice_channel = ctx.author.voice.channel

    if ctx.voice_client is None:
      await voice_channel.connect()
    else:
      await ctx.voice_client.move_to(voice_channel)
    #joining done
      
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
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
      info = ydl.extract_info(url, download = False)
      url2 = info['formats'][0]['url']
      source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
      vc.play(source)

    #await ctx.send('**Now playing:** {}'.format(player.title))
    del(queue[0])

#================================================================================

def setup(client):
  client.add_cog(music(client))