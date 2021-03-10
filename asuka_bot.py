#imports
import discord
from discord.ext import commands
import random
import time

#Bot Cleint
client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print('Logged on as {0}!'.format(client.user))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.author.name == "Flex":
        await message.channel.send('Fuck you, Babyman piece of shit. kys')

    if message.content.startswith('hello asuka'):
        await message.channel.send('Fuck you {.author.nick}'.format(message))
        
    if message.content.startswith("peg"):
        await message.channel.send("I'm going to peg you {.author.nick}".format(message))

    if message.content.startswith("img"):

        images = ["asuka pro pic.jpg", "asuka 2.jpg", "asuka 3.jpg"]

        random_img = random.choice(images) 

        await message.channel.send (file=discord.File(random_img))
    
    await client.process_commands(message)


    


@client.command()
async def come_here(ctx):
    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name= "General")
    await voiceChannel.connect()

@client.command()
async def baka(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio("Asuka - Anta Baka.mp3"))


@client.command()
async def begone_thot(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")

 
    


client.run('ODE4ODkyODYyNDA0OTUyMDk0.YEeraA.Rp10wti_GRkg9aSRSeMtR7pRJL8')