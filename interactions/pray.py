import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import CommandTree
import requests
import discord.ui
from discord.ui import Button,View
import random

class pray(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["praying","prays"])
    async def pray(self,ctx,user:discord.Member=None):
        if user == None:
            embed=discord.Embed(title=f"{ctx.author.name} is praying",color = discord.Colour.purple())
        else:
            embed=discord.Embed(title=f"{ctx.author.name} is praying for {user.name}",color = discord.Colour.purple())    
        if user!=None and user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return 
        randomgifs = [
            "https://media.tenor.com/KTp9sgkLjzoAAAAC/jerry-the-mouse-tom-and-jerry.gif",
            "https://media.tenor.com/4IckGuTqWeYAAAAC/spongebob-squarepants-begging.gif",
            "https://media.tenor.com/TX04b7YAOl8AAAAd/please-please-god.gif",
            "https://media.tenor.com/DmOiqA-m5nAAAAAC/mushoku-tensei-rudeus.gif",
            "https://media.tenor.com/Yt5E0AQEPX8AAAAd/shirley-temple-praying.gif",
            "https://media.tenor.com/rwGUhTSCrL8AAAAd/takagi-san-takagi.gif",
            "https://media.tenor.com/qz1oO99DcK0AAAAd/wendy-praying-son-seungwan-praying.gif",
            "https://media.tenor.com/0FRabKRmgjAAAAAd/seungwan-youngstreet-son-seungwan-praying.gif",
            "https://media.tenor.com/GUV6HplSs7MAAAAC/loeya-pray.gif",
            "https://media.tenor.com/q--Ww86G0MoAAAAd/genshin-genshin-impact.gif",
            "https://media.tenor.com/g15Z-NkoKjsAAAAC/praying-prayer.gif",
            "https://media.tenor.com/K20UM-dZC4oAAAAd/lets-pray-pray.gif",
            "https://media.tenor.com/iZ6u-jpcKDIAAAAC/marie-mai-mariemai-news.gif",
            "https://media.tenor.com/tMtfOLuBZDUAAAAC/praying-hands-gucci-mane.gif",
            "https://media.tenor.com/1JJngkJOI3IAAAAC/hangouts-pray.gif",
            "https://media.tenor.com/js1RCj9wG1cAAAAC/ic0niclisa-praying.gif",
            "https://media.tenor.com/XsW48MrsCpwAAAAd/praying-prayers.gif",
            "https://media.tenor.com/WhgPx2O1I-QAAAAd/pray-praying.gif",
            "https://media.tenor.com/CyK_xV5Q3lkAAAAC/jiminjimin-jimin.gif",
            "https://media.tenor.com/YEwRtiurLiwAAAAd/yurina-yurina-meme.gif",
            "https://media.tenor.com/uI-iiI3Wnh8AAAAC/kejsi-pray.gif",
            "https://media.tenor.com/14pcWHa4-S4AAAAC/ryujin-cat.gif",
            "https://media.tenor.com/_E3TnFTI8ZkAAAAC/porfa-porfa-remix.gif"
           
        ]
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)       
      

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(pray(bot))       
    print("pray is loaded")    
       
        
   