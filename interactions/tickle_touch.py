import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import CommandTree
import requests
import discord.ui
from discord.ui import Button,View
import random

class tickle(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["Tickle","Tick"])
    async def tickle(self,ctx,user:discord.Member=None):
        if user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        randomgifs = [
            "https://media.discordapp.net/attachments/1045618240900050954/1046100540821610516/91a686f18ccc56616078a25bb55bfed9.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046100541475930112/tickle-feet.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046100541152964638/giphy_5.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046153500029100043/bae.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046154095213420564/giphy_6.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046154459635527710/6VniMLU.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046154782680813578/aaaaaaaahahahah-tickling-is-awesome.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046154913308221540/371fa72fcc90fc98902266fa258718c3.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046155310815002654/butt-tickles.gif",
            "https://media.discordapp.net/attachments/949680123479728147/1047176779347001374/ticklepickle-tummytickle.gif",
            "https://media.discordapp.net/attachments/949680123479728147/1047176783394517032/free-ikuya-kirishima.gif",
            "https://media.discordapp.net/attachments/949680123479728147/1047176793913827349/date-a-live-date-a-live-iv.gif",
            "https://media.discordapp.net/attachments/949680123479728147/1047176798355603476/elmo-tickle.gif",
            "https://media.discordapp.net/attachments/949680123479728147/1047176799743922297/tickling-feet-tickle.gif",
            "https://media.discordapp.net/attachments/949680123479728147/1047176813962600568/tickle-laugh.gif",
            "https://media.discordapp.net/attachments/949680123479728147/1047176825408864418/emolga-picochilla.gif",
            "https://media.discordapp.net/attachments/949680123479728147/1047177105420591145/aum-animation-studio-andy-pirki.gif",
            "https://media.discordapp.net/attachments/949680123479728147/1047177108968964206/tickle-tickling.gif",
            "https://media.discordapp.net/attachments/949680123479728147/1047177112819355669/minccino-pokemon.gif",
            "https://media.discordapp.net/attachments/949680123479728147/1047177123628060743/peter-griffin-family-guy.gif",
            "https://media.discordapp.net/attachments/949680123479728147/1047177128011108372/xiyo-xiyo-kitty.gif?width=426&height=606",
            "https://media.discordapp.net/attachments/949680123479728147/1047177569381912667/digimon-digimon-adventure02.gif",
            "https://media.discordapp.net/attachments/949680123479728147/1047177570057191465/little-bear.gif",
            "https://media.discordapp.net/attachments/949680123479728147/1047177576180887593/otter-tickle.gif",
            "https://media.discordapp.net/attachments/949680123479728147/1047177577913126953/tickling-tickle.gif",
            "https://media.discordapp.net/attachments/949680123479728147/1047177580148707429/ijiranaide-nagatoro-nagataro.gif",
            "https://media.discordapp.net/attachments/949680123479728147/1047177832146665482/cyndaquil-misty.gif",
            "https://media.discordapp.net/attachments/949680123479728147/1047177837154684968/kiliti-paningning.gif",
            "https://media.discordapp.net/attachments/949680123479728147/1047177842296893440/caturday-crazy.gif?width=341&height=607",
            "https://media.discordapp.net/attachments/949680123479728147/1047177854917562508/ojamajo-doremi-ojamajo.gif",
            "https://media.discordapp.net/attachments/949680123479728147/1047177861422911508/tickle-laugh_1.gif",
            "https://media.discordapp.net/attachments/949680123479728147/1047177874207162388/stop-stop-that.gif"
        ]
        embed=discord.Embed(title=f"{ctx.author.name} is tickling {user.name} ! hehe",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)    

    @commands.command(aliases=["tg","touchg",'tgrass','touch'])
    async def touchgrass(self,ctx,user:discord.Member=None):
        if user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        randomgifs = [
            "https://media.tenor.com/4yx6wK51ezsAAAAd/nathan-touch-some-grass.gif",
            "https://media.tenor.com/XI3gjYioePAAAAAd/h3-h3h3.gif",
            "https://media.tenor.com/qDDKH8ac3ykAAAAd/sushichaeng-grass.gif",
            "https://media.tenor.com/-69FTXitQkkAAAAd/touch-grass.gif",
            "https://media.tenor.com/a9zY_N-GPMkAAAAd/touch-some-grass-grass.gif",
            "https://media.tenor.com/CW-0A0q-6ksAAAAd/touching-grass.gif",
            "https://media.tenor.com/eY1oQbTdtRkAAAAC/touch-grass-klee.gif",
            "https://media.tenor.com/R1Q7Q2cThtIAAAAd/beefboys-andrew-miller.gif",
            "https://media.tenor.com/Pxqxstf2boQAAAAi/touch-grass.gif",
            "https://media.tenor.com/vsSV0xcqvSAAAAAC/mcdonnells-curry.gif"
              ]    
        embed=discord.Embed(title=f"{ctx.author.name} is telling {user.name} to touch grass",color = discord.Colour.purple())    
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)    

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(tickle(bot))       
    print("tickle, touch is loaded")    
       
        
   