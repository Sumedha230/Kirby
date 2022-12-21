import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import CommandTree
import requests
import discord.ui
from discord.ui import Button,View
import random

class spit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["Spit"])
    async def spit(self,ctx,user:discord.Member=None):
        if user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        randomgifs = [
            "https://media.discordapp.net/attachments/1045618240900050954/1046353978193084426/18s1.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046353997621108806/OnlyDisloyalHare-size_restricted.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046354474748362762/GrouchyCleverGreatdane-size_restricted.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046354573641658418/hasbulla-magomedov-hasbulla.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046354595431067648/giphy.gif",
            "https://media.discordapp.net/attachments/949680123479728147/1047180140267970621/tom-and-jerry-spit.gif",
            "https://media.discordapp.net/attachments/949680123479728147/1047180142608404510/hasbulla-magomedov-hasbulla.gif",
            "https://media.discordapp.net/attachments/949680123479728147/1047180149214433300/spit-anime.gif",
            "https://media.discordapp.net/attachments/949680123479728147/1047180153681358868/spit-water-mavis.gif",
            "https://media.discordapp.net/attachments/949680123479728147/1047180157326209094/spit.gif",
            "https://media.discordapp.net/attachments/949680123479728147/1047180159196864592/magicriddle-themagicriddle.gif",
            "https://media.discordapp.net/attachments/949680123479728147/1047180513430995014/clayton-osterhues-reegan-layer.gif?width=606&height=606",
            "https://media.discordapp.net/attachments/949680123479728147/1047180516287332402/the-rock-spit.gif",
            "https://media.discordapp.net/attachments/949680123479728147/1047180517394632734/blowing-jp.gif",
            "https://media.discordapp.net/attachments/949680123479728147/1047180524449443910/spit-spitting.gif",
            "https://media.discordapp.net/attachments/949680123479728147/1047180525158285463/peepo-spit.gif?width=626&height=607",
            "https://media.discordapp.net/attachments/949680123479728147/1047180525967790151/funny-smile.gif?width=341&height=607",
            "https://media.discordapp.net/attachments/949680123479728147/1047180882647187557/anime-milk-spit.gif",
            "https://media.discordapp.net/attachments/949680123479728147/1047180884236849232/ninjala-ninjala-anime.gif",
            "https://media.discordapp.net/attachments/949680123479728147/1047180888968020118/spit-takes.gif",
            "https://media.discordapp.net/attachments/949680123479728147/1047180894131191889/anime-spit.gif"
        ]
        embed=discord.Embed(title=f"{ctx.author.name} is spitting on {user.name} !",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)    
    

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(spit(bot))       
    print("spit is loaded")    
       
        
   