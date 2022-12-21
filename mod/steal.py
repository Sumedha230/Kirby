import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import CommandTree
import requests
import discord.ui
from discord.ui import Button,View
import aiohttp
from io import BytesIO

class steal(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    
    @commands.hybrid_command(aliases=["steal",'eadd'])
    async def emoji_add(self,ctx,emoji: discord.PartialEmoji,name:str=None):
        if ctx.author.guild_permissions.administrator==True:
            guild = ctx.guild
            async with aiohttp.ClientSession() as ses:
                async with ses.get(emoji.url) as r:
                    try:
                        img = BytesIO(await r.read())
                        bValue = img.getvalue()
                        if r.status in range(200,320):
                            if name==None:
                                emoji = await guild.create_custom_emoji(image=bValue,name=emoji.name)
                                await ctx.send("emoji added")
                                await ses.close()
                            else:
                                emoji = await guild.create_custom_emoji(image=bValue,name=name)
                                await ctx.send(f"emoji added with the name {name}")
                                await ses.close()

                    except:
                        await ctx.send("Not possible")
        else:
            await ctx.send("You don't have the required administrator permissions")                            
    

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(steal(bot))       
    print("steal is loaded")    
       
    