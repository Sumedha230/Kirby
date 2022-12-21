import discord
from discord.ext import commands
import random
from discord import app_commands
from discord.app_commands import CommandTree
import googletrans
from googletrans import Translator

class dice(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.hybrid_command(name="dice",aliases=['dices','Dice','DICE'])
    async def dice(self,ctx:commands.Context,num:int):
        if num==6 or num==12:
            await ctx.send(f"{random.randint(1,int(num))}")       
        else:
            await ctx.send("Invalid Choice = Choose between 6 or 12")
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'pong! {round(self.bot.latency*1000)}ms')  

    @commands.hybrid_command(name="say",aliases=['imitate'])
    async def imitate(self,ctx, member: discord.Member, *, message=None):
        if message == None:
            await ctx.send('provide a message with that!')
            return
        webhook = await ctx.channel.create_webhook(name=member.name)
        await webhook.send(str(message), username=member.name, avatar_url=member.avatar.url)
        webhooks = await ctx.channel.webhooks()
        for webhook in webhooks:
            await webhook.delete()          

    @commands.hybrid_command(name="translate",aliases=['tl','tr','tral'])
    async def translate(self,ctx,*, thing):
        translator = Translator()
        translation = translator.translate(thing, dest="english")
        embed = discord.Embed(title="Translation", color = discord.Colour.purple())
        embed.add_field(name="Text",value = f"{thing}",inline=False)
        embed.add_field(name="Translated Text",value = f"{translation.text}",inline=False)
        await ctx.send(embed=embed)     

    @commands.hybrid_command(name="translating",aliases=['translation','trion','tri','tli'])
    async def translation(self,ctx,to_language:str,*,sentence):
        translator = Translator()
        translation = translator.translate(sentence, dest=to_language)
        embed = discord.Embed(title="Translation", color = discord.Colour.purple())
        embed.add_field(name="Text",value = f"{sentence}",inline=False)
        embed.add_field(name="Translated Text",value = f"{translation.text}",inline=False)
        await ctx.send(embed=embed)          
         
async def setup(bot):
    await bot.add_cog(dice(bot))       
    print("dice , ping , say , translator , translation is loaded")    

       