import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import CommandTree


class basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'pong! {round(self.bot.latency*1000)}ms')        

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(basic(bot))       
    print("basic is loaded")    
