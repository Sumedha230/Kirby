import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import CommandTree
import requests
import discord.ui
from discord.ui import Button,View

class warn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(aliases=["Warn",'warning','warns'])
    @commands.has_guild_permissions(kick_members=True)
    @commands.has_guild_permissions(manage_messages=True)
    async def warn(self,ctx,user:discord.Member=None,*,reason:str=None):
        if user.id == ctx.author.id:
            await ctx.send(f" Don't be an idiot, warn yourself in private")
        elif user.guild_permissions.administrator:
            em = discord.Embed(title="Admin can't be warned",description=f"{user.mention} is an admin so don't try again {ctx.author.mention}",color = discord.Colour.purple())
            await ctx.send(embed=em)
        elif ctx.author.guild_permissions.kick_members==False or ctx.author.guild_permissions.manage_messages==False or ctx.author.guild_permissions.administrator==False:
            await ctx.send("You dont have the permission to warn anyone")  
        else:
            if reason != None:
                em = discord.Embed(title="Warned",description=f"{user.mention} wass warned by {ctx.author.mention} {reason}",color = discord.Colour.purple())
            else:
                em = discord.Embed(title="Warned",description=f"{user.mention} was warned by {ctx.author.mention} for no reason",color = discord.Colour.purple())     
            if reason != None:
                await user.send(f" You were warned in {ctx.guild.name} for {reason} by {ctx.author.name}")
            else:
                await user.send(f" You were warned in {ctx.guild.name} by {ctx.author.name}")
            await ctx.send(embed=em)      
    

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(warn(bot))       
    print("warn is loaded")    
    