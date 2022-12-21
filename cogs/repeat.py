import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import CommandTree


class repeating(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.hybrid_command(name="repeater")
    async def repeat(self,ctx, times: int, *content:str):
        """Repeats whatever the user has typed 
        k!repeat 2 hi"""
        if 0<times<=5:
            for i in range(times):
                await ctx.send(" ".join(content)) 
        else:
            embed = discord.Embed(color = discord.Colour.purple(),description="Kirby is not a fool and won't spam the chat")
            embed.set_image(url ="https://media.discordapp.net/attachments/1042790120652275853/1045611042228666408/kirby-mad.gif")
            await ctx.send(embed=embed)

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(repeating(bot))       
    print("repeating is loaded")    
    
