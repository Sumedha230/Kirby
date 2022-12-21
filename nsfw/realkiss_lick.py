import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import CommandTree
import requests
import discord.ui
from discord.ui import Button,View
import random

class realkiss(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["Realkiss",'rk','rkiss','realk'])
    async def realkiss(self,ctx,user:discord.Member=None):
        if ctx.channel.is_nsfw():
            if user == None:
                humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
                user = random.choice(humans)
            if user.id == ctx.author.id:
                await ctx.send("Bro atleast find someone to do an interaction with ")
                return
            randomgifs = [
            "https://media.discordapp.net/attachments/1005851300195487875/1045660381525331978/IMG_9526.gif",
            "https://media.discordapp.net/attachments/1005851300195487875/1045660805510742076/IMG_9529.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046362820914188328/Black_And_White_GIF_-_Find__Share_on_GIPHY.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046362821295886367/File_Stefan-Elena-stefan-and-elena-32515768-500-265-1-_gif.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046362821627224094/Kiss_Couple_GIF_-_Kiss_Couple_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046362822088593409/Kisses_Stupid_Love_GIF_-_Kisses_Kiss_Stupid_Love_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046362822503845909/Kiss_Couple_GIF_-_Kiss_Couple_Romance_-_Discover__Share_GIFs.gif"
             ]
            embed=discord.Embed(title=f"{ctx.author.name} has kissed {user.name} hard",color = discord.Colour.purple())
            randomgif = random.choice(randomgifs)
            embed.set_image(url = randomgif)
            await ctx.send(embed=embed)
        else:
            await ctx.send("Do this in an NSFW Channel")  

    @commands.command(aliases=["dl","lick"])
    async def dirtylick(self,ctx,user:discord.Member=None):
        if ctx.channel.is_nsfw():
            if user == None:
                humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
                user = random.choice(humans)
            if user.id == ctx.author.id:
                await ctx.send("Bro atleast find someone to do an interaction with ")
                return
            randomgifs = [
                "https://media.tenor.com/CpyaloXKvuMAAAAC/deep-kiss-passionate-kiss.gif",
                "https://media.tenor.com/S5pfE5MxqOgAAAAd/indirect-kiss-relationship-goals.gif",
                "https://media.tenor.com/dGv9AneldUgAAAAd/lick-neck-hot.gif"
              ]    
            embed=discord.Embed(title=f"{user.name} is get licked by {ctx.author.name} Yum!",color = discord.Colour.purple())    
            randomgif = random.choice(randomgifs)
            embed.set_image(url = randomgif)
            await ctx.send(embed=embed) 
        else:
            await ctx.send("Do this in a NSFW channel")           
    
async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(realkiss(bot))       
    print("realkiss, dirty lick is loaded")    
       
    
