import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import CommandTree


class avatar(commands.Cog):
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

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(avatar(bot))       
    print("avatar is loaded")    
    
