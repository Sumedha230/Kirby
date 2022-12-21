import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import CommandTree
import requests
import discord.ui
from discord.ui import Button,View
import random

class wave(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=["waving","Wave","Waving"])
    async def wave(self,ctx,user:discord.Member=None):
        if user == None:
            embed=discord.Embed(title=f"{ctx.author.name} is waving",color = discord.Colour.purple())
        else:
            embed=discord.Embed(title=f"{ctx.author.name} waves at {user.name}",color = discord.Colour.purple())    
        if user!=None and user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return 
        randomgifs = [
            "https://media.discordapp.net/attachments/949680123869814794/1046891679770230835/monkey-waving.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046891680093188298/kung-fu-panda-po-waving-ub3ic92611g1yvxk.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046891680407756821/d7i06j2-209054b9-be1e-46b0-aa61-ffbe4dc1ebda.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046891681255006328/hello-there-waving.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046891681640890398/200w.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046891682018369606/garfield-waving.gif"   
        ]
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)  

    @commands.command(aliases=["hf","Hf","highfiving",'highf','hfive'])
    async def highfive(self,ctx,user:discord.Member=None):
        if user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        randomgifs=[
            "https://media.tenor.com/KX6_14fSo0YAAAAi/akirambow-smile-person.gif",
            "https://media.tenor.com/TRSYCx4GnGoAAAAi/budding-pop-friends.gif",
            "https://media.tenor.com/D4geDkAW9jgAAAAi/cat-paw.gif",
            "https://media.tenor.com/zRQPetULV5kAAAAi/rascal-high-five.gif",
            "https://media.tenor.com/PDom-Pt-DYAAAAAi/high-five-yay.gif",
            "https://media.tenor.com/r322btJKK7EAAAAC/high-five-amy-santiago.gif",
            "https://media.tenor.com/qy_WcGdRzfgAAAAC/xluna-high-five.gif",
            "https://media.tenor.com/OR2z4Pkg45kAAAAC/high-five.gif",
            "https://media.tenor.com/7skQ3peC1mEAAAAC/high-five.gif",
            "https://media.tenor.com/5uzrkK8Pps0AAAAC/love-anniversary.gif",
            "https://media.tenor.com/uHSWiu1Jk2MAAAAC/base-high-five.gif",
            "https://media.tenor.com/EcTTHD9dnMUAAAAC/evan-and-katelyn-extreme-high-five.gif",
            "https://media.tenor.com/UtMb32NBztEAAAAC/neil-patrick-harris-high-five.gif",
            "https://media.tenor.com/gI49p3ZeN2AAAAAi/cool-blue-high-five.gif",
            "https://media.tenor.com/x_Z1QD8mQecAAAAi/shi-ngao.gif",
            "https://media.tenor.com/XlAB-tE7tMYAAAAi/hi5-high-five.gif",
            "https://media.tenor.com/7nDIBPMdjSoAAAAC/gts-good-time-society.gif",
            "https://media.tenor.com/fmDOIOVxfVoAAAAC/seth-meyers-late-night-seth.gif",
            "https://media.tenor.com/mpCnVpX0xIYAAAAC/high-five-spongebob.gif",
            "https://media.tenor.com/_KGWqG2EBdIAAAAC/anime-girls.gif",
            "https://media.tenor.com/JsCGv-NM-w0AAAAC/cat-high.gif",
            "https://media.tenor.com/K4dK6z75fQUAAAAC/high-five-slow-motion.gif",
            "https://media.tenor.com/BD-trsxTZPoAAAAC/barney-stinson-high-five.gif",
            "https://media.tenor.com/9vnJU85-7GwAAAAC/yeah-high.gif",
            "https://media.tenor.com/RXYUxZdBaUcAAAAd/stukk-high-five.gif",
            "https://media.tenor.com/Rs5Gyiw0OysAAAAC/high-five-high-five-cat.gif",
            "https://media.tenor.com/2NgSVoaOwtMAAAAC/high-five.gif",
            "https://media.tenor.com/MDTYbqilAxgAAAAC/ogvhs-high-five.gif",
            "https://media.tenor.com/sQzOqyKfGv4AAAAd/pokemon-scorbunny.gif",
            "https://media.tenor.com/zuGJiqsnkPIAAAAC/eevee-pikachu.gif",
            "https://media.tenor.com/RusIdB6WS-IAAAAC/cat-high-five.gif",
            "https://media.tenor.com/cfBsYK73HLkAAAAC/puppy-dog.gif",
            "https://media.tenor.com/umyVoo90A_sAAAAd/high-five-dog-high-five-xiteb.gif",
            "https://media.tenor.com/r0sUDFfn6o0AAAAC/high-five-awesome.gif",
            "https://media.tenor.com/EFVbyCW4ITEAAAAd/dogs-high-five.gif",
            "https://media.tenor.com/ZVyre2PZC4EAAAAd/dog-high-five.gif",
            "https://media.tenor.com/MZuZ9C_3_ZkAAAAC/dog-high-five.gif",
            "https://media.tenor.com/SUQuOYlPZU4AAAAd/high-five-the-pack.gif",
            "https://media.tenor.com/8hFGXTck6usAAAAC/pawfive-dogfive.gif",
            "https://media.tenor.com/JrV7r-u405wAAAAd/hanzo-husky-hanzo-the-husky.gif",
            "https://media.tenor.com/-Xe4wBdy7f4AAAAC/paws-cat.gif",
            "https://media.tenor.com/qVun4U93OiYAAAAC/meomoc-high-five.gif",
            "https://media.tenor.com/nUPVAKITU0YAAAAd/high-five-cat.gif",
            "https://media.tenor.com/a2GGLtACrqsAAAAC/bakabaka7-adventure-time.gif",
            "https://media.tenor.com/CQn2tIIADEcAAAAC/monkey-high-five.gif"
        ]
        embed=discord.Embed(title=f"{ctx.author.name} is high fiving {user.name} !",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)     

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(wave(bot))       
    print("wave, highfive is loaded")    
       
        
   