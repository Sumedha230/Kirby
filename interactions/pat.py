import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import CommandTree
import requests
import discord.ui
from discord.ui import Button,View
import random

class pat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["Pat,'patting"])
    async def pat(self,ctx,user:discord.Member=None):
        if user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        randomgifs = [
            "https://media.discordapp.net/attachments/1045618243013984296/1046400910332530698/mala-mishra-jha-pat-head.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046400915663503440/giphy.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046400927076188190/678116d6e7fdbb5275c2d1ca8c938099.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046401319113601125/giphy_1.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046401320745177139/cute-anime-umaru-head-pat-rabcmvfkpeuteckt.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046401334095659068/bunny-cute.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046401338688409630/cd77c5cab311d773ac3846079e483d67_w200.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046401349014802552/pat-cat.gif"
        ]
        embed=discord.Embed(title=f"{ctx.author.name} is patting {user.name} because they are cute!",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)        

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(pat(bot))       
    print("pat is loaded")    
       
        
   