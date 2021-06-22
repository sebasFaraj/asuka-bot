import os
import discord
from discord.ext import commands
import random
import youtube_dl
import os
import nacl
import time
from keep_alive import keep_alive


#Bot Cleint
client = commands.Bot(command_prefix="$")


@client.event
async def on_ready():
    print('Logged on as {0}!'.format(client.user))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.author.name == "Hernan":
      rand_num = random.randint(1,3)
      if rand_num == 2:
        responses_h = ["stfu", ":billed_cap:","get good at siege", "Your PhD isn't real","Your hairline, that is all","NattyDDV lover","shut up mr. chess"]

        random_response_h = random.choice(responses_h)
        await message.channel.send(random_response_h)
    
    if message.author.name == "faringa":
        rand_num = random.randint(1,7)
        if rand_num == 2:
          responses = ["no crecistes tanto man", "i care for you {.author.nick}".format(message), "based and redpilled", "i want to marry you"]
          random_response= random.choice(responses)        
          await message.channel.send(random_response)
      
        

    if message.content.startswith('hello asuka'):
        await message.channel.send('Fuck you {.author.nick}'.format(message))
    
    if message.content.startswith("do you love me?"):
        await message.channel.send("Of course I do {.author.nick} :)".format(message))

    if message.content.startswith("img"):

        images = ["asuka pro pic.jpg", "asuka 2.jpg", "asuka 3.jpg"]

        random_img = random.choice(images) 

        await message.channel.send (file=discord.File(random_img))
    
    await client.process_commands(message)


    


@client.command()
async def come_here(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()

@client.command()
async def baka(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio("Asuka - Anta Baka.mp3"))

@client.command()
async def bakas(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio("Asuka - Anta Baka.mp3"))
    time.sleep(3)
    voice.play(discord.FFmpegPCMAudio("Asuka - Anta Baka.mp3"))
    time.sleep(3)
    voice.play(discord.FFmpegPCMAudio("Asuka - Anta Baka.mp3"))

@client.command()
async def sdl(ctx):
    await ctx.send("sdl, sdl, sdl")

@client.command()
async def begone_thot(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")

@client.command()
async def a(ctx, url : str):
  song_there = os.path.isfile("song.mp3")
  try:
      if song_there:
         os.remove("song.mp3")
  except PermissionError:
      await ctx.send("Wait for the current playing music to end or use the 'stop' command")
      return
  
  voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

  ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

  with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

  for file in os.listdir("./"):
      if file.endswith(".mp3") and not file.startswith("Asuka - Anta Baka.mp3"):
        os.rename(file, "song.mp3")

  voice.play(discord.FFmpegPCMAudio("song.mp3"))
@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently no audio is playing.")


@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("The audio is not paused.")

@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()



keep_alive()
client.run(os.getenv('TOKEN'))
my_secret = os.environ['TOKEN']
