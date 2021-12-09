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

client = commands.Bot(command_prefix = '[')

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



#events
@client.event
async def on_ready():
    ruina_status.start()
    print("RuinaBot is Alive!")



#make the bot join voice channel
@client.command(pass_context = True)
async def join_voice(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()
    await ctx.send('RuinaBot has joined the voice Channel!')


#make the bot leave voice channel
@client.command(pass_context = True)
async def leave_voice(ctx):
    await ctx.guild.voice_client.disconnect()
    await ctx.send('RuinaBot has left the voice channel')
    

#musics play
@client.command(pass_context = True)
async def play(ctx,url):
    guild = ctx.message.guild
    voice_client = guild.voice_client
    player = await voice_client.create_ytdl_player(url)
    players[guild.id] = player
    player.start()

#Tasks
@tasks.loop(hours = 12)
async def ruina_status():
    await client.change_presence(activity = discord.Game(next(status)))


#delete message command
@client.command()
@commands.has_permissions(manage_messages=True)
async def clean(ctx, amount = 100):
    if amount == None:
        await ctx.channel.send('Error desu`~ Please type correctly u baka`~!')
    else :
        await ctx.channel.purge(limit=amount)

#kick command
@client.command()
@commands.has_permissions(administrator = True)
async def kick(ctx, member : discord.Member, * , reason = 'For violating the server rules you have been kicked from the server'):
    await member.kick(reason=reason)


#ban command
@client.command()
async def ban(ctx, member : discord.Member, * , reason = 'For violating the server rules you have been banned from the server'):
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} have been banned for violating the server rules')

#unban command
@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if(user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'{user.mention} Have been unbanned')
            return

# cogs
# @client.command()
# async def load(ctx, extension):
#     client.load_extension(f'cogs.{extension}')

# @client.command()
# async def unload(ctx, extension):
#     client.unload_extension(f'cogs.{extension}')

# for filename in os.listdir('./cogs'):
#     if filename.endswith('.py'):
#         client.load_extension(f'cogs.{filename[:-3]}')

#Run the client on the server
client.run('OTE0MTcyMzQ3Mzc4OTg3MDY4.YaJLWA.LkEQUv0Z1heuebEPf_6vWrRKurM')