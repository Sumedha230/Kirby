import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import CommandTree
import requests
import discord.ui
from discord.ui import Button,View
import random

class miss(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["Missing","miss","Miss"])
    async def missing(self,ctx,user:discord.Member=None):
        if user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        randomgifs = [
            "https://media.discordapp.net/attachments/949680123869814794/1045693438982619146/miss-you-shy-bear-wgvvsi8epdvui25t.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1045693439276236810/b5395bd842e048cd00cc021b50c37ba6.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1045693439574024282/missing-you-badly-waiting.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046155561265287188/7fd9ff3c81c5ea8cf317c05794a22363.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046155628684525698/dog-triste.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046155851494326372/i-miss-you-so-much-i-miss-you.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046155978267164692/SjOp.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046156399069102090/i-miss-you-bear-crying-d9eflc3t9immbccm.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047173771200577637/love-you_1.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047173775235489802/sanrio-hello-kitty.gif0",
            "https://media.discordapp.net/attachments/949680123479728146/1047173778838409226/hello-kitty.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047173782168670279/goodnight-miss.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047173918257053797/miss.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047173924800167986/missing-you.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047173927128027156/miss-you.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047174320750874704/cat-i-love-you.gif?width=424&height=606",
            "https://media.discordapp.net/attachments/949680123479728146/1047174325393948732/love-cute.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047174335372218388/love-languages-miss-you.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047174609700659321/i-miss-you.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047174611323846766/miss-you-pikachu.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047174612007530546/missing.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047174617703403660/dino-i-miss-you.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047174629762023494/i-miss-you-anya.gif?width=606&height=606",
            "https://media.discordapp.net/attachments/949680123479728146/1047174904262443098/rascal-miss-you.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047174905260675113/spongebob-patrick-star.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047174906309255188/fatcatzcouple-fluffy.gif"
        ]
        embed=discord.Embed(title=f"{ctx.author.name} is missing {user.name}",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)      
    

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(miss(bot))       
    print("miss is loaded")    
       
        
       
    