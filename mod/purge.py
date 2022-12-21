import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import CommandTree
import requests
import discord.ui
from discord.ui import Button,View

class purge(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
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
    

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(purge(bot))       
    print("purge is loaded")    