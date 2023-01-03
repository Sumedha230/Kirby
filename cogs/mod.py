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
import datetime
from datetime import timedelta

class mod(commands.Cog):
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
    @ban.error
    async def ban_error(self,ctx, error):
        if isinstance(error,commands.CheckFailure):
            await ctx.send(f'{error}')  

    @commands.hybrid_command()
    @commands.has_guild_permissions(ban_members=True)
    @commands.has_guild_permissions(administrator=True)
    async def unban(self,ctx,member:discord.User): 
        if ctx.guild.ban(member):
            await ctx.guild.unban(member)
            await ctx.send(f"{member.mention} has been **unbanned**")
        else:
            await ctx.send(f"{member.mention} is not banned")    
    @unban.error
    async def unban_error(self,ctx, error):
        if isinstance(error,commands.CheckFailure):
            await ctx.send(f'{error}')          

    @commands.hybrid_command(aliases=["cr","create"])
    @commands.has_guild_permissions(manage_roles=True)
    @commands.has_guild_permissions(administrator=True)
    async def createrole(self,ctx,name:str,*,emoji:discord.PartialEmoji=None):
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

    @commands.hybrid_command(name="purge",aliases=['clear','Clear','Purge','clr','Clr','CLR'])
    @commands.has_guild_permissions(manage_messages=True)
    async def clear(self,ctx,amt=1):
        try:
            if ctx.author.guild_permissions.manage_messages == False or ctx.author.guild_permissions.administrator == False:
                await ctx.send("You don't have the required permissions")
                return
            amt +=1
            if amt > 50:
                await ctx.send("Can't delete more than 50")
                return
            else:
                await ctx.channel.purge(limit=amt)
                await ctx.send("Cleared Messages")
                await ctx.channel.purge(limit=1)   
        except:
            await ctx.send("Bot does not have the permission for this command")  

    @commands.hybrid_command(aliases=["steal",'eadd'])
    async def emoji_add(self,ctx,emoji: discord.PartialEmoji,name:str=None):
        if ctx.author.guild_permissions.administrator==True:
            guild = ctx.guild
            async with aiohttp.ClientSession() as ses:
                async with ses.get(emoji.url) as r:
                    try:
                        img = BytesIO(await r.read())
                        bValue = img.getvalue()
                        if r.status in range(200,320):
                            if name==None:
                                emoji = await guild.create_custom_emoji(image=bValue,name=emoji.name)
                                await ctx.send("emoji added")
                                await ses.close()
                            else:
                                emoji = await guild.create_custom_emoji(image=bValue,name=name)
                                await ctx.send(f"emoji added with the name {name}")
                                await ses.close()

                    except:
                        await ctx.send("Not possible")
        else:
            await ctx.send("You don't have the required administrator permissions")               

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
                em = discord.Embed(title="Warned",description=f"{user.mention} was warned by {ctx.author.mention} {reason}",color = discord.Colour.purple())
            else:
                em = discord.Embed(title="Warned",description=f"{user.mention} was warned by {ctx.author.mention} for no reason",color = discord.Colour.purple())     
            if reason != None:
                await user.send(f" You were warned in {ctx.guild.name} for {reason} by {ctx.author.name}")
            else:
                await user.send(f" You were warned in {ctx.guild.name} by {ctx.author.name}")
            await ctx.send(embed=em)    
    
    @commands.hybrid_command()
    @commands.has_guild_permissions(manage_channels=True)
    async def lock(self,ctx,channel:discord.TextChannel=None):
        if ctx.author.guild_permissions.administrator==False or ctx.author.guild_permissions.manage_channels == False:
            await ctx.send("You don't have the required permissions to lock a channel")
        else:
            channel = channel or ctx.channel
            overwrite = channel.overwrites_for(ctx.guild.default_role)
            overwrite.send_messages = False
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
            if channel:
                await ctx.send(f'Channel {channel} locked.')
            else:
                await ctx.send(f"Channel {ctx.channel} locked.")    
    @lock.error
    async def lock_error(self,ctx, error):
        if isinstance(error,commands.CheckFailure):
            await ctx.send(f'{error}')        

    @commands.hybrid_command()
    @commands.has_guild_permissions(manage_channels=True)
    async def unlock(self,ctx,channel:discord.TextChannel=None):
        if ctx.author.guild_permissions.manage_channels == False or ctx.author.guild_permissions.administrator==False:
            await ctx.send("You don't have the required permissions to unlock a channel")
        else:
            channel = channel or ctx.channel
            overwrite = channel.overwrites_for(ctx.guild.default_role)
            
            overwrite.send_messages = True
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
            await ctx.send(f'Channel {channel} unlocked.')
                  
    @unlock.error
    async def unlock_error(self,ctx, error):
        if isinstance(error,commands.CheckFailure):
            await ctx.send(f'{error}')  

                                       
    

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(mod(bot))       
    print("ban , role , kick, mute, purge, steal, warn, lock, unlock is loaded")    
       
    
