import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import CommandTree
import requests
import discord.ui
from discord.ui import Button,View
import random

class marry(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    @commands.command(aliases=["Marry","MARRY"])
    async def marry(self,ctx,user:discord.Member=None):
        if user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        randomgifs = [
            "https://media.discordapp.net/attachments/949680123869814794/1046885786601136138/sportsmanias-just-married.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046885794087960626/anineogray-wedding.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046885802166206564/marriage-marry.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046885806226276432/TerribleRemorsefulCottontail-size_restricted.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046885979367165962/804a7b8872de5db7d3dee11a94a89449.gif?width=606&height=606",
            "https://media.discordapp.net/attachments/949680123869814794/1046885984442269758/tumblr_mllx0atPDj1r1r3hjo1_500.gif"
            ]
        
        embed=discord.Embed(title=f"{ctx.author.name} married {user.name} !! Congratulations to the newly weds",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)    

    @commands.command(aliases=["Love"])
    async def love(self,ctx,user:discord.Member=None):
        if user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        randomgifs = [
            "https://media.discordapp.net/attachments/1045618240900050954/1045664205388398643/love-kirby.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046156748983124050/love-gif.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046156765412200528/icegif-876.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046156775352713326/icegif-592.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046156785515495504/icegif-581.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046157241130156102/DarlingRectangularIsabellinewheatear-max-1mb.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046157205617004594/cute-love.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046157189548609546/WindingShorttermAfricanharrierhawk-size_restricted.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046157176118456441/bunny-rabbit.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046363448302379068/Muddu_Love_Sticker_-_Muddu_Love_Heart_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047171901522456576/love-kiss.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047171906714996836/mocha-mucha.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047171906840830043/milk-and-mocha-bears.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047171912603799653/love-hug.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047171919474069645/good-night-love-you.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047171931113271356/relajamiento-y-amor-love.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047172271678169138/love-you.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047172280960155699/love.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047172283376087150/emote.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047172288031752232/milk-and-mocha-bears_1.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047172307036160000/love-rabbit.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047172384316198943/donald-love.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047172387264811099/animated-cute.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047172392352493609/cartoon-heart.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047172395561140266/feelings-love.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047172402955702423/duck-cute.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047174325544943637/sending-love.gif"
        ]
        embed=discord.Embed(title=f"{ctx.author.name} sends love to {user.name}",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)      

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(marry(bot))       
    print("marry, love is loaded")    
       
        
   