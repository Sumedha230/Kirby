import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import CommandTree
import requests
import discord.ui
from discord.ui import Button,View

class kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot     
    @commands.hybrid_command(aliases=["Kick",'kicks'])
    @commands.has_guild_permissions(kick_members=True)
    async def kick(self,ctx, user:discord.Member=None,*,reason:str=None):
        if user.guild_permissions.administrator:
            em = discord.Embed(title="Admin can't be kicked",description=f"{user.mention} is an admin so don't try again {ctx.author.mention}",color = discord.Colour.purple())
            await ctx.send(embed=em)
        elif ctx.author.guild_permissions.kick_members==False:
            await ctx.send("You dont have the permission to kick")
        else:
            if reason != None:
                em = discord.Embed(title="Kicked",description=f"{user.mention} was kicked by {ctx.author.mention} {reason}",color = discord.Colour.purple())
            else:
                em = discord.Embed(title="Kicked",description=f"{user.mention} was kicked by {ctx.author.mention}",color = discord.Colour.purple())     
            await user.kick(reason=reason)
            await ctx.send(embed=em)      
    

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(kick(bot))       
    print("kick is loaded")    
        
    