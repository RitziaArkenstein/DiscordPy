#Import Discord Package

from logging import info
import discord
from discord import voice_client
from discord.channel import VoiceChannel
import youtube_dl
import os
from discord import guild
from discord.ext import commands, tasks
from itertools import cycle
from discord import FFmpegPCMAudio
from discord.utils import get

from discord.ext.commands.bot import AutoShardedBot

#clients
client = discord.Client()

players = {}

status = cycle(['Patting Ruina', 'Ruina Simulator'])

bad = ["fuck" , "shit", "asshole", "bitch", "whore"]

#no no words
@client.event
@commands.has_permissions(manage_messages = False)
async def on_message(message):
    if message.author.id == client.user.id:
      return
    if(message.author.guild_permissions.manage_messages):
        return
    print(message.content)
    if message.guild is not None:
        
        for word in bad:
            # print(word)
            if message.content.lower().find(word)!=-1:
                await message.delete()
                await message.author.send("Hey! Please restrain from using that word from now on ! \n\n Try to be a better person by trying not to be rude ok?")

#Tasks
@tasks.loop(hours = 12)
async def ruina_status():
    await client.change_presence(activity = discord.Game(next(status)))

#events
@client.event
async def on_ready():
    ruina_status.start()
    print("RuinaBot is Alive!")




client.run('OTczOTMyMDA3NTg5NTc2NzE0.GT3bJr.t3YpTrkTDFaQEAFqFdf2aoaK4pJeAmxSrNy_qs')