import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import CommandTree
import requests
import discord.ui
from discord.ui import Button,View
import random

class pillowfight(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["PillowFight","Pillowfight","pf","PF",'pillowf','pfight'])
    async def pillowfight(self,ctx,user:discord.Member=None):
        if user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        randomgifs = [
            "https://media.discordapp.net/attachments/949680123869814794/1046846733818269836/grandparents-day-insomnia.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046846742060081332/pow-pillow-fight.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046846743398072400/edac8fd3339d460f5d609cb738c4d1c5.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046846745943998564/OptimisticPlaintiveAidi-size_restricted.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046846752013164584/733898f1a9d33a3db97fcebbf49dbb82.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046846813648465990/giphy_5.gif"
            ]
        
        embed=discord.Embed(title=f"{ctx.author.name} and {user.name} are pillowfighting !",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)     

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(pillowfight(bot))       
    print("pillowfight is loaded")    
       
        
   