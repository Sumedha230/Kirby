import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import CommandTree
import requests
import discord.ui
from discord.ui import Button,View
import random

class sip(commands.Cog):
    def __init__(self, bot):
        self.bot = bot  
    
    @commands.command(aliases=["sipping","slurp","sips","Sip"])
    async def sip(self,ctx):
        randomgifs = [
            'https://media.discordapp.net/attachments/1035565430422642718/1054479077593067580/sip3.gif',
            "https://media.discordapp.net/attachments/1035565430422642718/1054479078083792927/sip4.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054479078469673040/sip5.gif?width=606&height=606",
            "https://media.discordapp.net/attachments/1035565430422642718/1054479078821998592/sip6.gif?width=521&height=607",
            "https://media.discordapp.net/attachments/1035565430422642718/1054479079207866518/sip7.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054479079711191040/sip8.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054479080080281661/sip9.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054479080466161674/sip10.gif?width=606&height=606",
            "https://media.discordapp.net/attachments/1035565430422642718/1054479080860430426/sips.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054479081187577916/sips2.gif",
            "https://media.tenor.com/nmv_0Z6axwoAAAAi/sip-sipping-tea-gif.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054482139216871424/sip16.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054482139636310046/sip17.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054482139984433232/sip18.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054482140328362115/sip19.gif?width=606&height=606",
            "https://media.discordapp.net/attachments/1035565430422642718/1054482140676493312/sip20.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054482141053976748/sip21.gif?width=604&height=606",
            "https://media.discordapp.net/attachments/1035565430422642718/1054482141402107924/sip22.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054482141741842522/sip23.gif?width=606&height=606",
            "https://media.discordapp.net/attachments/1035565430422642718/1054482142199029821/sip24.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054482142517792878/sip25.gif?width=606&height=606",
            "https://media.discordapp.net/attachments/1035565430422642718/1054482231755821174/sip26.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054482232347197530/sip27.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054482232728887306/sip28.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054482233102192650/sip29.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054482233437716490/sip30.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054482234515652720/sips.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054483474716827748/sip32.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054483475106893884/sip33.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054483475450822706/sip34.gif?width=606&height=606"

            ]
        
        embed=discord.Embed(title=f" {ctx.author.name} is slurping their drink",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)  
   

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(sip(bot))       
    print("sip is loaded")    
       
        
   