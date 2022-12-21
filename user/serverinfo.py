import discord
from discord.ext import commands
from discord import app_commands

class serverinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.hybrid_command(name="serverinfo",aliases=['si','serveri','sinfo'])
    async def serverinfo(self,ctx):
        members = len(ctx.guild.members)
        Roles = len(ctx.guild.roles)
        embed=discord.Embed(title=f"***Server Information***",color = discord.Colour.purple() )    
        embed.add_field(name='Name:', value=ctx.guild.name, inline=False)
        embed.add_field(name='ID:', value=ctx.guild.id, inline=False)
        embed.add_field(name='Owner:', value=ctx.guild.owner.mention, inline=False)
        embed.add_field(name='Created At:', value=ctx.guild.created_at.strftime('Day: %d/%m/%Y Hour: %H:%M:%S %p'), inline=False)
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
   
async def setup(bot):
    await bot.add_cog(serverinfo(bot))       
    print("serverinfo is loaded")         