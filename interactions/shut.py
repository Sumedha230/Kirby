import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import CommandTree
import requests
import discord.ui
from discord.ui import Button,View
import random

class shut(commands.Cog):
    def __init__(self, bot):
        self.bot = bot  
    
    @commands.command(aliases=["STFU","shut","shutup","Shut"])
    async def stfu(self,ctx,user:discord.Member=None):
        if user.id==530824411759116288:
            randomgifs = [
            "https://media.tenor.com/mBFdHahC7SwAAAAd/lmao-stfu.gif",
            "https://media.tenor.com/8HCiYkHSLWgAAAAd/stfu.gif",
            "https://media.tenor.com/jmEeIVgFhjQAAAAC/stfu-shut-up.gif",
            "https://media.tenor.com/2pgy64Sh5wYAAAAd/stfu-punching-stfu-gif.gif",
            "https://media.tenor.com/KKS3hJ33_sUAAAAC/stfu.gif",
            "https://media.tenor.com/QDuyGHlwjr4AAAAd/stfu.gif",
            "https://media.tenor.com/P_hk6dBzWUcAAAAC/stfu-can-you-stfu.gif",
            "https://media.tenor.com/_vBlPe9UqrEAAAAC/plastic-chair-plastic-knife.gif",
            "https://media.tenor.com/4__-628PgsUAAAAd/snoop-dogg-rapper.gif",
            "https://media.tenor.com/rqY-hzlUJokAAAAC/shut-up.gif",
            "https://media.tenor.com/kE818ge-WMcAAAAd/stfulmfao.gif",
            "https://media.tenor.com/TIvSjriG5k8AAAAC/stfu-discord.gif",
            "https://media.tenor.com/9XOxc5bL3ikAAAAC/stfu-pls.gif",
            "https://media.tenor.com/_c-tBlx1g0sAAAAd/nobody-care.gif",
            "https://media.tenor.com/6GhnldRykacAAAAd/charley3-stfu.gif",
            "https://media.tenor.com/DNsCIM3ExTkAAAAC/stfu-shut-up.gif",
            "https://media.tenor.com/br56Ph5l_moAAAAd/idc-stfu.gif",
            "https://media.tenor.com/wGYP0T-roIoAAAAC/grackles-shut-the-fuck-up.gif",
            "https://media.tenor.com/b69Hw9iU3IgAAAAC/chemmanna-chemmanna-stfu.gif",
            "https://media.tenor.com/dzYLz0zrtrgAAAAC/shut-up-just.gif",
            "https://media.tenor.com/I2x1XSezVDcAAAAC/chandler-bing-shut-up.gif",
            "https://media.tenor.com/82m9RQSFWboAAAAd/shutupangry.gif",
            "https://media.tenor.com/pHJlCcfg3LQAAAAC/penny-how-bout-you-stfu.gif",
            "https://media.tenor.com/JUpxZb-3DiAAAAAC/shut-up.gif",
            "https://media.tenor.com/edyHKYbvAiAAAAAC/ronald-mcdonald.gif"
            ]
            embed=discord.Embed(title=f"{ctx.author.name} How about you STFU instead !",color = discord.Colour.purple())
            randomgif = random.choice(randomgifs)
            embed.set_image(url = randomgif)
            await ctx.send(embed=embed)                    

        if user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot and m.id != 530824411759116288]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        randomgifs = [
            "https://media.tenor.com/mBFdHahC7SwAAAAd/lmao-stfu.gif",
            "https://media.tenor.com/8HCiYkHSLWgAAAAd/stfu.gif",
            "https://media.tenor.com/jmEeIVgFhjQAAAAC/stfu-shut-up.gif",
            "https://media.tenor.com/2pgy64Sh5wYAAAAd/stfu-punching-stfu-gif.gif",
            "https://media.tenor.com/KKS3hJ33_sUAAAAC/stfu.gif",
            "https://media.tenor.com/QDuyGHlwjr4AAAAd/stfu.gif",
            "https://media.tenor.com/P_hk6dBzWUcAAAAC/stfu-can-you-stfu.gif",
            "https://media.tenor.com/_vBlPe9UqrEAAAAC/plastic-chair-plastic-knife.gif",
            "https://media.tenor.com/4__-628PgsUAAAAd/snoop-dogg-rapper.gif",
            "https://media.tenor.com/rqY-hzlUJokAAAAC/shut-up.gif",
            "https://media.tenor.com/kE818ge-WMcAAAAd/stfulmfao.gif",
            "https://media.tenor.com/TIvSjriG5k8AAAAC/stfu-discord.gif",
            "https://media.tenor.com/9XOxc5bL3ikAAAAC/stfu-pls.gif",
            "https://media.tenor.com/_c-tBlx1g0sAAAAd/nobody-care.gif",
            "https://media.tenor.com/6GhnldRykacAAAAd/charley3-stfu.gif",
            "https://media.tenor.com/DNsCIM3ExTkAAAAC/stfu-shut-up.gif",
            "https://media.tenor.com/br56Ph5l_moAAAAd/idc-stfu.gif",
            "https://media.tenor.com/wGYP0T-roIoAAAAC/grackles-shut-the-fuck-up.gif",
            "https://media.tenor.com/b69Hw9iU3IgAAAAC/chemmanna-chemmanna-stfu.gif",
            "https://media.tenor.com/dzYLz0zrtrgAAAAC/shut-up-just.gif",
            "https://media.tenor.com/I2x1XSezVDcAAAAC/chandler-bing-shut-up.gif",
            "https://media.tenor.com/82m9RQSFWboAAAAd/shutupangry.gif",
            "https://media.tenor.com/pHJlCcfg3LQAAAAC/penny-how-bout-you-stfu.gif",
            "https://media.tenor.com/JUpxZb-3DiAAAAAC/shut-up.gif",
            "https://media.tenor.com/edyHKYbvAiAAAAAC/ronald-mcdonald.gif"

            ]
        
        embed=discord.Embed(title=f"{ctx.author.name} is telling {user.name} to STFU !",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)  
   

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(shut(bot))       
    print("shut is loaded")    
       
        
   