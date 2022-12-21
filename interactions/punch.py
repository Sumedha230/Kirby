import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import CommandTree
import requests
import discord.ui
from discord.ui import Button,View
import random

class punch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["Punch",'punching'])
    async def punch(self,ctx,user:discord.Member=None):
        if user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        randomgifs = [
            "https://media.discordapp.net/attachments/1045618243013984296/1046657546347364432/punch-punching.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054492842732564481/punch10.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054492843072294982/punch9.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054492843718230096/punch8.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054492844607410206/punch6.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054492845492416622/punch4.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054492845836341348/punch3.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054492846192869443/punch2.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054492846549381172/punch1.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054492950027055145/punch12.gif"
        ]
        
        embed=discord.Embed(title=f"{ctx.author.name} punches {user.name} hard!",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)     

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(punch(bot))       
    print("punch is loaded")    
       
        
   