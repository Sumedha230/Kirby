import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import CommandTree
import requests
import discord.ui
from discord.ui import Button,View

class ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(aliases=["Ban",'bans'])
    @commands.has_guild_permissions(ban_members=True)
    @commands.has_guild_permissions(administrator=True)
    async def ban(self,ctx,user:discord.Member=None,*,reason:str=None):
        if user.guild_permissions.administrator:
            em = discord.Embed(title="Admin can't be banned",description=f"{user.mention} is an admin so don't try again {ctx.author.mention}",color = discord.Colour.purple())
            await ctx.send(embed=em)
        elif ctx.author.guild_permissions.ban_members==False:
            await ctx.send("You dont have the permission to ban")
        else:
            if reason != None:
                em = discord.Embed(title="Banned",description=f"{user.mention} was banned by {ctx.author.mention} {reason}",color = discord.Colour.purple())
            else:
                em = discord.Embed(title="Banned",description=f"{user.mention} was banned by {ctx.author.mention}",color = discord.Colour.purple())     
            await user.ban(reason=reason)
            await ctx.send(embed=em)      
    

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(ban(bot))       
    print("ban is loaded")    
       
    
