import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import CommandTree
import requests
import discord.ui
from discord.ui import Button,View
import random

class yawn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=["yawning","yawns"])
    async def yawn(self,ctx,user:discord.Member=None):
        if user == None:
            embed=discord.Embed(title=f"{ctx.author.name} is yawning ",color = discord.Colour.purple())
        else:
            embed=discord.Embed(title=f"{ctx.author.name} is yawning because of {user.name}",color = discord.Colour.purple())    
        if user!=None and user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return 
        randomgifs = [
            "https://media.tenor.com/S96iCeYOWCcAAAAd/yawngirl-yawnkid.gif",
            "https://media.tenor.com/XVRTqgVzAQQAAAAC/yawn-yawning.gif",
            "https://media.tenor.com/HMhYjZY3Oa0AAAAd/bugs-bunny-yawn.gif",
            "https://media.tenor.com/oNaCRbvHu3oAAAAd/johnny-english-rowan-atkinson.gif",
            "https://media.tenor.com/zYw6FpUqW7MAAAAd/monkey-yawn.gif",
            "https://media.tenor.com/hclnFXnLhQ0AAAAC/pikachu-yawn.gif",
            "https://media.tenor.com/LoOKUaCO-04AAAAC/yawn-tom-and-jerry.gif",
            "https://media.tenor.com/GUGZujRyUXYAAAAC/boring-yawn.gif",
            "https://media.tenor.com/6L5o7Ov-__sAAAAC/kitaro-yawn.gif",
            "https://media.tenor.com/4hZZgLvA7W0AAAAd/cat-yawn.gif",
            "https://media.tenor.com/40263d2eyREAAAAd/cat-waking-up.gif",
            "https://media.tenor.com/2Dzbry2XP_sAAAAd/cat-meow.gif",
            "https://media.tenor.com/TEWbYOiUSiEAAAAd/time-for-bed-bedtime.gif",
            "https://media.tenor.com/TV6ckPX9EcAAAAAd/cute-cat-yawning.gif",
            "https://media.tenor.com/OgdDRulZx-UAAAAd/wembley-yawn.gif",
            "https://media.tenor.com/iRAIQjbzYOAAAAAd/otter-yawn.gif",
            "https://media.tenor.com/32f48oSEHMgAAAAC/sleepy-anime.gif",
            "https://media.tenor.com/8KkpLp3zkQwAAAAd/yawn-yawning.gif",
            "https://media.tenor.com/OgdDRulZx-UAAAAd/wembley-yawn.gif"
           ]
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)  

    @commands.command(aliases=["vibing","Vibe","Vibing"])
    async def vibe(self,ctx,user:discord.Member=None):
        if user == None:
            embed=discord.Embed(title=f"{ctx.author.name} is vibing",color = discord.Colour.purple())
        else:
            embed=discord.Embed(title=f"{user.name} and {ctx.author.name} are vibing",color = discord.Colour.purple())    
        if user!=None and user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return 
        randomgifs = [
           "https://media.discordapp.net/attachments/949680123869814794/1046845051109658684/vibe-rabbit.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046845066347548723/teo-cat.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046845070235664465/tumblr_7d502f156e5b5458e8d05495f5936e44_008adab0_500.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046845075684073492/giphy_4.gif",
            "https://media.discordapp.net/attachments/1033808352133783595/1047090652002930758/adventure-time-jake.gif"
        ]
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)       

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(yawn(bot))       
    print("yawn, vibe is loaded")    
       
        
   