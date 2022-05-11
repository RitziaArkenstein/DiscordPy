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

chegg = ["chegg" , "cheggs", "Cheggs", "cheg", "Cheg"]
bart = ["bartleby", "Bartleby", "bartlebys", "Barlebys"]
solutioninn = ["solutioninn", "solutionin", "Solutioninn", "Solutioninn", "solution inn","Solution inn", "Solution in", "solution in"]
scribd = ["scribd", "Scribd"]
numerade = ["numerade", "Numerade"]
hero = ["Coursehero", "coursehero", "Course hero","Course Hero","course hero", "course Hero"]
slideshare = ["Slideshare", "slideshare", "Slide share", "Slide Share", "slide share", "slide Share", "slideshares", "slide shares", "Slide shares", "Slide Shares", "slide Shares"]
tutor = ["transtutor", "Transtutor", "transtutors", "Transtutors", "Trans tutor", "Trans Tutor", "Trans tutors", "Trans Tutors", "trans Tutor", "trans Tutors"]
wolfram = ["wolfram", "Wolfram", "wolframs", "Wolframs", "Wolf Ram", "Wolf ram", "Wolf rams", "Wolf Rams", "wolf ram", "wolf Rams", "wolf Ram"]

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
        
        for word in chegg:
            # print(word)
            if message.content.lower().find(word)!=-1:
                await message.delete()
                await message.author.send("If you want help for Chegg solutions please go to the #manual-unlock  or #auto-unlock channel and wait for the admin/helpers there to answer your questions :)\n\n If you dont see the #manual-unlock/#auto-unlock channel or its locked, that means the admin/helper for unlocking ur answer is not available so please wait until they are available :)\n\n Please do read the #faq for more info Thanks")

                # await client.process_commands(message)

        for word in bart:
            if message.content.lower().find(word)!=-1:
                await message.delete()
                await message.author.send("If you want help for Bartlebys solutions please go to the #bartleby channel and wait for the bot to answer your questions :)\n\n If the bot doesnt work as intended please DM one of the admins and they will help you if they are available :)")

        for word in solutioninn:
            if message.content.lower().find(word)!=-1:
                await message.delete()
                await message.author.send("If you want help for Solutioninn solutions please go to the #solutioninn channel and wait for the bot to answer your questions :)\n\n If the bot doesnt work as intended please DM one of the admins and they will help you if they are available :)")

        for word in scribd:
            if message.content.lower().find(word)!=-1:
                await message.delete()
                await message.author.send("If you want help for Scribd solutions please go to the #scribd channel and wait for the bot to answer your questions :)\n\n If the bot doesnt work as intended please DM one of the admins and they will help you if they are available :)")

        for word in numerade:
            if message.content.lower().find(word)!=-1:
                await message.delete()
                await message.author.send("If you want help for Numerade solutions please go to the #numerade channel and wait for the bot to answer your questions :)\n\n If the bot doesnt work as intended please DM one of the admins and they will help you if they are available :)")

        for word in hero:
            if message.content.lower().find(word)!=-1:
                await message.delete()
                await message.author.send("If you want help for Coursehero solutions please go to the #coursehero channel and wait for the bot to answer your questions :)\n\n If the bot doesnt work as intended please DM one of the admins and they will help you if they are available :)")

        for word in slideshare:
            if message.content.lower().find(word)!=-1:
                await message.delete()
                await message.author.send("If you want help for Slideshare solutions please go to the #slideshare channel and wait for the bot to answer your questions :)\n\n If the bot doesnt work as intended please DM one of the admins and they will help you if they are available :)")

        for word in tutor:
            if message.content.lower().find(word)!=-1:
                await message.delete()
                await message.author.send("If you want help for Transtutor solutions please go to the #transtutor channel and wait for the bot to answer your questions :)\n\n If the bot doesnt work as intended please DM one of the admins and they will help you if they are available :)")

        for word in wolfram:
            if message.content.lower().find(word)!=-1:
                await message.delete()
                await message.author.send("If you want help for Wolfram solutions please go to the #wolfram channel and wait for the bot to answer your questions :)\n\n If the bot doesnt work as intended please DM one of the admins and they will help you if they are available :)")




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