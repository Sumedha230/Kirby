import os
import asyncio
import discord
from dotenv.main import load_dotenv
from discord.ext import commands
from discord.ext.commands import Bot
from discord import app_commands
import random
from random import choice
from discord.ext.commands import has_permissions,bot_has_guild_permissions,CheckFailure,BadArgument
import requests
from discord import app_commands
from typing import List
import googletrans
from googletrans import Translator
import discord.ui
from discord.ui import Button,View
import aiohttp
from io import BytesIO
from discord.utils import get
import sys, traceback
from discord.ext import commands, tasks
from discord.app_commands import CommandTree
import datetime
from datetime import timedelta

class MyBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        intents.members = True
        super().__init__(intents= intents, command_prefix= ["k!","K!",">"] , description='Cute Kirby!',activity = discord.Game(name="Super Smash Bros"))
        self.initial_extensions = [
            'cogs.basic',
            'cogs.dice',
            'user.serverinfo',
            'cogs.say',
            'user.avatar',
            'cogs.serverbooster',
            'user.userinfo',
            'translator.translate',
            'translator.translation',
            'user.guildavatar',
            'user.banner',
            'games.truthordare',
            'games.wouldyourather',
            'games.paranoia',
            'games.neverhaveiever',
            'games.repeat',
            'mod.purge',
            'mod.ban',
            'mod.warn',
            'mod.kick',
            'interactions.kiss',
            'interactions.slap',
            'nsfw.realkiss_lick',
            'interactions.hug_boop',
            'interactions.fuck',
            'interactions.miss',
            'interactions.tickle_touch',
            'interactions.spit',
            'interactions.eat_blush',
            'interactions.laugh',
            'interactions.pinch',
            'interactions.pat',
            'interactions.block_bonk_cheer_choke_cope_cry',
            'interactions.sit',
            'interactions.punch',
            'interactions.pillowfight',
            'interactions.kill',
            'interactions.nom',
            'interactions.marry_love',
            'interactions.wave_highfive',
            'interactions.threaten_fight_judge',
            'interactions.spank',
            'interactions.shut',
            'interactions.lie',
            'interactions.sip',
            'interactions.pray',
            'interactions.yawn_vibe',
            'interactions.smirk_cuddle',
            'interactions.salute',
            'mod.steal',
            'mod.create_role',
            'mod.mute_unmute',
            'help'
        ]

    async def setup_hook(self): 
        self.session = aiohttp.ClientSession()
        for ext in self.initial_extensions:
            await self.load_extension(ext)
            await bot.tree.sync()

    async def on_ready(self):
        print(f"{bot.user.name} has Connected")  
        try:
            synced = await bot.tree.sync()
            print(f"Synced {len(synced)} commands")
            count = len(bot.guilds)
            print(f'Logged on as {count}, your bot {bot.user} !')
        except Exception as e:
            print(e)        
          
load_dotenv() 
bot = MyBot()
        

   

    #await member.timed_out_until(datetime.timedelta(seconds=30))            
# async def timeout_user(*, user_id: int, guild_id: int, until):
#     headers = {"Authorization": f"Bot {bot.http.token}"}
#     url = f"https://discord.com/api/v9/guilds/{guild_id}/members/{user_id}"
    
#     timeout = (datetime.datetime.utcnow() + datetime.timedelta(minutes=until)).isoformat()
    
#     json = {'communication_disabled_until': timeout}
#     async with bot.session.patch(url, json=json, headers=headers) as session:
#         if session.status in range(200, 299):
#            return True
#         return False


# @bot.command()
# async def timeout(ctx: commands.Context, member: discord.Member, until: int):
#     handshake = await timeout_user(user_id=member.id, guild_id=ctx.guild.id, until=until)
#     if handshake:
#          return await ctx.send(f"Successfully timed out user for {until}")
#     await ctx.send("Something went wrong")

bot.remove_command("help")        

bot.run('MTA0Mzg1ODk0MDk5MzIyODgwMA.Gm_EjW.NqIKfa5fplbIlTHi1PPzOPHL3xWudW6sroqW5s')


