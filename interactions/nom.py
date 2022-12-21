import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import CommandTree
import requests
import discord.ui
from discord.ui import Button,View
import random

class nom(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["Nom","NOM"])
    async def nom(self,ctx,user:discord.Member=None):
        if user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        randomgifs = [
            "https://media.discordapp.net/attachments/949680123869814794/1046876009003225158/sMP.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046876014762008646/45ba063ad9212afec9fed28e79fbfe09.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046876072601456681/PaltryMadKusimanse-max-1mb.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046876072991543408/fe8f2a77e1f3b100e81ee0f1f454542a.gif"
            ]
        
        embed=discord.Embed(title=f"{ctx.author.name} noms on {user.name} !!",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)      

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(nom(bot))       
    print("nom is loaded")    
       
        
   