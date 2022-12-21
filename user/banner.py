import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import CommandTree


class banner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
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

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(banner(bot))       
    print("banner is loaded")    
    