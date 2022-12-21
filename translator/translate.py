import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import CommandTree
import googletrans
from googletrans import Translator

class translates(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.hybrid_command(name="translate",aliases=['tl','tr','tral'])
    async def translate(self,ctx,*, thing):
        translator = Translator()
        translation = translator.translate(thing, dest="english")
        embed = discord.Embed(title="Translation", color = discord.Colour.purple())
        embed.add_field(name="Text",value = f"{thing}",inline=False)
        embed.add_field(name="Translated Text",value = f"{translation.text}",inline=False)
        await ctx.send(embed=embed)   

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(translates(bot))       
    print("translates is loaded")    
    
