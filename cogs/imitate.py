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


class imitate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(aliases=["Say"])
    async def say(self, member: discord.Member, *, message=None):
        if message == None:
            await self.send('provide a message with that!')
            return
        webhook = await self.channel.create_webhook(name=member.name)
        await webhook.send(str(message), username=member.name, avatar_url=member.avatar.url)
        webhooks = await self.channel.webhooks()
        for webhook in webhooks:
            await webhook.delete() 
async def setup(bot):
    await bot.add_cog(imitate(bot))       
    print("imitate is loaded")    
    
