import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import CommandTree


class userinfos(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
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
    

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(userinfos(bot))       
    print("userinfo is loaded")    