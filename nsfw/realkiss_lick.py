import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import CommandTree
import requests
import discord.ui
from discord.ui import Button,View
import random
import json

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
            embed=discord.Embed(title=f"{ctx.author.name} has kissed {user.name} hard",color = discord.Colour.purple())
            KEY = "AIzaSyCQMOmwOsr0cu8ZBc3WLWrKXyZmWFp7NRA"  # click to set to your apikey
            lmt = 50
            ckey = "test" 
            searchTerm = "real kiss"  
            r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
            data = r.json()
            randomgif = random.randint(0,49)
            url = data['results'][randomgif]["media_formats"]['gif']['url']
            embed.set_image(url = url)
            await ctx.send(embed=embed)
        else:
            await ctx.send("Do this in an NSFW Channel")  

    @commands.command(aliases=["dl"])
    async def dirtylick(self,ctx,user:discord.Member=None):
        if ctx.channel.is_nsfw():
            if user == None:
                humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
                user = random.choice(humans)
            if user.id == ctx.author.id:
                await ctx.send("Bro atleast find someone to do an interaction with ")
                return
             
            embed=discord.Embed(title=f"{user.name} is getting licked by {ctx.author.name} Yum!",color = discord.Colour.purple())    
            KEY = "AIzaSyCQMOmwOsr0cu8ZBc3WLWrKXyZmWFp7NRA"  # click to set to your apikey
            lmt = 50
            ckey = "test" 
            searchTerm = "real lick"  
            r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
            data = r.json()
            randomgif = random.randint(0,49)
            url = data['results'][randomgif]["media_formats"]['gif']['url']
            embed.set_image(url = url)
            await ctx.send(embed=embed) 
        else:
            await ctx.send("Do this in a NSFW channel")           
    
async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(realkiss(bot))       
    print("realkiss, dirty lick is loaded")    
       
    
