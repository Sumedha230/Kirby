import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import CommandTree

class user(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name="avatars",aliases=['ava','av'])
    async def avatars(self,ctx, *,  avamember : discord.Member=None):
        if avamember == None:
            avamember = ctx.author
        test = discord.Embed(title=f"{avamember.name}'s Avatar",color = discord.Colour.purple())
        test.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        test.set_image(url=avamember.avatar.url)
        await ctx.send(embed=test)   
    
    @commands.hybrid_command(name="banner",aliases=["Banner",'BANNER','ba'])
    async def user_banner(self,ctx, user:discord.Member = None):
        if not user:
            user = ctx.author
        user = await self.bot.fetch_user(user.id)  
        if user.banner:
            embed = discord.Embed(title = f"{user.name}'s Banner",color = discord.Colour.purple())
            embed.set_author(name=user.name,icon_url=user.avatar.url)
            embed.set_image(url = user.banner.url)
            await ctx.send(embed=embed)
        else:
            await ctx.send(f' this user has no banner')
    
    @commands.hybrid_command(name="guild_avatar",aliases=['ga','gava','avag','ag','guildavatar','avatarguild'])
    async def guild_avatar(self,ctx,user:discord.Member=None):
        """gives the guild avatar of a member by typing kga or kavatar_guild"""
        if user == None:
            user = ctx.author
        test = discord.Embed(title=f"{user.name}'s Avatar",color = discord.Colour.purple())
        test.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        test.set_image(url=user.display_avatar.url)
        await ctx.send(embed=test)

    @commands.hybrid_command(name="serverinfo",aliases=['si','serveri','sinfo'])
    async def serverinfo(self,ctx):
        members = len(ctx.guild.members)
        Roles = len(ctx.guild.roles)
        embed=discord.Embed(title=f"***Server Information***",color = discord.Colour.purple() )    
        embed.add_field(name='Name:', value=ctx.guild.name, inline=False)
        embed.add_field(name='ID:', value=ctx.guild.id, inline=False)
        embed.add_field(name='Owner:', value=ctx.guild.owner.mention, inline=False)
        embed.add_field(name='Created At:', value=ctx.guild.created_at.strftime('Day: %d/%m/%Y Hour: %H:%M:%S %p'), inline=False)
        embed.add_field(name='Boost Level:', value=ctx.guild.premium_tier, inline=False)
        gc= 0
        bc = 0
        for member in ctx.guild.members:
            if member.bot == False:
                gc += 1
            else:
                bc+=1    
        embed.add_field(name="Total Member Count",value = f"The total headcount in this server is {ctx.guild.member_count}", inline=False)
        embed.add_field(name="Member Count",value = f"There are a total of {gc} members in this server", inline=False)
        embed.add_field(name="Bot Count",value = f"There are a total of {bc} bots in this server",inline=False)
        embed.set_thumbnail(url=ctx.guild.icon)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name="server_boosters",aliases=['sb','serverb','sboost'])
    async def serverbooster(self,ctx):
        embed = discord.Embed(title = f'{ctx.guild.name}\'s Server Boost Info', description = f' There are a total of {str(ctx.guild.premium_subscription_count)} boosts in this server, the boosters are')
        t = ctx.guild.premium_subscribers
        j=1
        for i in t:
            embed.add_field(name= f"Booster {j}",value=f"{i.mention}",inline=False)
            j+=1
        embed.set_thumbnail(url=ctx.guild.icon)
        await ctx.send(embed = embed)  

    @commands.hybrid_command(name="userinfo",aliases=['ui','uinfo','useri'])
    async def userinfo(self,ctx,member:discord.Member=None):
        if member == None:
            member = ctx.message.author
        roles = [role for role in member.roles]
        embed=discord.Embed(title=f"***User Information***",color = discord.Colour.purple(),timestamp = ctx.message.created_at)   
        embed.add_field(name = "Name",value = member,inline=False) 
        embed.add_field(name = "ID",value = member.id,inline=False) 
        embed.add_field(name = "Nickname",value = member.display_name,inline=False)
        embed.add_field(name = "Status",value = member.status,inline=False)
        embed.add_field(name = "Created At",value = member.created_at.strftime("Day: %d/%m/%Y Hour: %H:%M:%S %p"),inline=False)
        embed.add_field(name = "Joined At",value = member.joined_at.strftime("Day: %d/%m/%Y Hour: %H:%M:%S %p"),inline=False) 
        embed.add_field(name = f" Total Roles ({len(roles)})",value = " ".join([role.mention for role in roles])) 
        embed.set_thumbnail(url = member.avatar.url)
        await ctx.send(embed=embed)      
   
async def setup(bot):
    await bot.add_cog(user(bot))       
    print("avatar , banner , guild avatar , serverinfo , serverbooster , userinfo is loaded")         