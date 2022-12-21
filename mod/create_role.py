import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import CommandTree
import requests
import discord.ui
from discord.ui import Button,View
import aiohttp
from io import BytesIO
from discord.utils import get


class create(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    
    @commands.hybrid_command(aliases=["cr","create"])
    @commands.has_guild_permissions(manage_roles=True)
    @commands.has_guild_permissions(administrator=True)
    async def createrole(self,ctx,*,name:str,emoji:discord.PartialEmoji=None):
        if ctx.author.guild_permissions.manage_roles == False or ctx.author.guild_permissions.administrator == False:
            await ctx.send("You don't have the required permissions")
        else:
            if emoji==None:
                await ctx.guild.create_role(name=name)
                await ctx.send(f"Role {name} has been created")
            else:
                guild = ctx.guild
                async with aiohttp.ClientSession() as ses:
                    async with ses.get(emoji.url) as r:
                        try:
                            img = BytesIO(await r.read())
                            bValue = img.getvalue()
                        except:
                            await ctx.send("Not possible") 
                await ctx.guild.create_role(name=name,display_icon=bValue)
                await ctx.send(f"Role {name} has been created")

    @commands.command(aliases=["ar","add"])
    @commands.has_guild_permissions(manage_roles=True)
    @commands.has_guild_permissions(administrator=True)
    async def addrole(self,ctx,user:discord.Member,*,roles:str):
        role = get(ctx.guild.roles,name=roles)
        if not role:
            await ctx.send("Role does not exist")
        if ctx.author.guild_permissions.manage_roles == False or ctx.author.guild_permissions.administrator == False:
            await ctx.send("You don't have the required permissions")
        else:
            if role in user.roles:
                await ctx.send(f"{user.mention} already has the role")
                return
            await user.add_roles(role)  
            await ctx.send(f"Added {role} to {user.mention}")         

    @commands.command(aliases=["rr","remove"])
    @commands.has_guild_permissions(manage_roles=True)
    @commands.has_guild_permissions(administrator=True)
    async def removerole(self,ctx,user:discord.Member,*,roles:str):
        role = get(ctx.guild.roles,name=roles)
        if not role:
            await ctx.send("Role does not exist")
        if ctx.author.guild_permissions.manage_roles == False or ctx.author.guild_permissions.administrator == False:
            await ctx.send("You don't have the required permissions")
        else:
            if role in user.roles:
                await user.remove_roles(role)
                await ctx.send(f"Successfully removed {role} from {user.mention}")
            else:
                await ctx.send(f"{user.mention} does not have the role")                  
                             
    

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(create(bot))       
    print("create role is loaded")    
       
    