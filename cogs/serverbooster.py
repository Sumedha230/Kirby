import discord
from discord.ext import commands
from discord import app_commands

class serverboost(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
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

   
async def setup(bot):
    await bot.add_cog(serverboost(bot))       
    print("serverboost is loaded")         

    
   
