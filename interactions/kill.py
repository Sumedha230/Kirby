import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import CommandTree
import requests
import discord.ui
from discord.ui import Button,View
import random

class kill(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["Kill","KILL",'killing'])
    async def kill(self,ctx,user:discord.Member=None):
        if user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        randomgifs = [
            "https://media.discordapp.net/attachments/949680123869814794/1046847843597549608/l55gmjfacebook.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046847850849513543/74c150a96ce7654c2131c7095dbfcc52.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046847852615303178/kill-me.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046847859510759494/kill-you-kill.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046847860165066833/giphy_6.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046847872529874944/kill-stab.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046848106035154964/cc87656cf72979fb8ee01c3eebc5cdff.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046848112565694534/among-us-kill-icegif.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046848114419581008/duck-mad.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046848121952542781/69649.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046848137723117618/804e237839129b79dd956eb9c2ec1803.gif"
            ]
        
        embed=discord.Embed(title=f"{ctx.author.name} killed {user.name} ! They definitely won't be able to type again",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)  

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(kill(bot))       
    print("kill is loaded")    
       
        
   