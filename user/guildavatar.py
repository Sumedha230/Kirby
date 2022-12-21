import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import CommandTree


class guild_avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.hybrid_command(name="guild_avatar",aliases=['ga','gava','avag','ag','guildavatar','avatarguild'])
    async def guild_avatar(self,ctx,user:discord.Member=None):
        """gives the guild avatar of a member by typing kga or kavatar_guild"""
        if user == None:
            user = ctx.author
        test = discord.Embed(title=f"{user.name}'s Avatar",color = discord.Colour.purple())
        test.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        test.set_image(url=user.display_avatar.url)
        await ctx.send(embed=test)

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(guild_avatar(bot))       
    print("guild avatar is loaded")    
    