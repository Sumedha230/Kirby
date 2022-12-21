import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import CommandTree
import requests
import discord.ui
from discord.ui import Button,View
import datetime
from datetime import timedelta

class mute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command()
    @commands.has_guild_permissions(moderate_members=True)
    async def mute(self,ctx,member:discord.Member,until:int=None,t:str=None,*,reason:str=None):
        if member==None:
            await ctx.send("Please mention the user you want to mute")
            return
        if ctx.author.id == member.id: 
            await ctx.channel.send(":x: You can't mute yourself!")
            return 
        if member.guild_permissions.administrator:
            em = discord.Embed(title="Admin can't be muted",description=f"{member.mention} is an admin so no point {ctx.author.mention}",color = discord.Colour.purple())
            await ctx.send(embed=em)
            return
        elif ctx.author.guild_permissions.moderate_members==False or ctx.author.guild_permissions.administrator==False:
            await ctx.send("You dont have the permission to mute") 
            return      
        if until == None:
            until = 1
        if t==None:
            t = "min"
        if t =='s' or t=='sec':
           duration = datetime.timedelta(seconds=until, minutes=0, hours= 0, days=0)
        elif t=='m' or t=='min':
           duration = datetime.timedelta(seconds=0, minutes=until, hours= 0, days=0)
        elif t=='h' or t=='hr' or t=='hour':
           duration = datetime.timedelta(seconds=0, minutes=0, hours= until, days=0)
        else:
           duration = datetime.timedelta(seconds=0, minutes=0, hours= 0, days=until)
        await member.timeout(duration, reason =reason)
        if reason==None:
           embed = discord.Embed(title=f":white_check_mark: {member.name} has been successfully muted for {until}{t}",color = discord.Colour.purple())
        else:
           embed = discord.Embed(title=f":white_check_mark: {member.name} has been successfully muted for {until}{t}, reason is {reason}",color = discord.Colour.purple())
    
        await ctx.send(embed=embed) 
    @commands.hybrid_command(aliases=['um']) 
    @commands.has_guild_permissions(moderate_members=True)   
    async def unmute(self,ctx,member:discord.Member):
        if member==None:
            await ctx.send("Please mention the user you want to mute")
            return
        if ctx.author.id == member.id: 
            await ctx.channel.send(":x: You can't unmute yourself!")
            return 
        if member.guild_permissions.administrator:
            em = discord.Embed(title="Admin can't be muted",description=f"{member.mention} is an admin so don't try again {ctx.author.mention}",color = discord.Colour.purple())
            await ctx.send(embed=em)
            return
        elif ctx.author.guild_permissions.moderate_members==False:
            await ctx.send("You dont have the permission to unmute") 
            return      
        duration = datetime.timedelta(seconds=0, minutes=0, hours= 0, days=0)
        await member.timeout(duration)
        embed = discord.Embed(title=f":white_check_mark: {member.name} has been successfully unmuted",color = discord.Colour.purple())
        await ctx.send(embed=embed)      
        
async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(mute(bot))       
    print("mute, unmute is loaded")    
       
    
  
