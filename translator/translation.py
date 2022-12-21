import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import CommandTree
import googletrans
from googletrans import Translator

class translating(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.hybrid_command(name="translating",aliases=['translation','trion','tri','tli'])
    async def translation(self,ctx,to_language:str,*,sentence):
        translator = Translator()
        translation = translator.translate(sentence, dest=to_language)
        embed = discord.Embed(title="Translation", color = discord.Colour.purple())
        embed.add_field(name="Text",value = f"{sentence}",inline=False)
        embed.add_field(name="Translated Text",value = f"{translation.text}",inline=False)
        await ctx.send(embed=embed)

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(translating(bot))       
    print("translating is loaded")    
    