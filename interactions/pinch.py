import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import CommandTree
import requests
import discord.ui
from discord.ui import Button,View
import random

class pinch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["pinching",'Pinch'])
    async def pinch(self,ctx,user:discord.Member=None):
        if user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        randomgifs = [
            "https://media.discordapp.net/attachments/993633626719780924/1046366440225247252/Milk_And_Mocha_Cheek_GIF_-_Milk_And_Mocha_Cheek_Chubby_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/993633626719780924/1046366440757940234/Little_piece_of_my_life.gif",
            "https://media.discordapp.net/attachments/993633626719780924/1046366441127034931/Squishy_Squishy_GIF_-_Squishy_Kitty_Cat_Cheeks_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/993633626719780924/1046366441424818186/Chubby_Cheeks_Pinch_GIF_-_Chubby_Cheeks_Pinch_Adorable_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/993633626719780924/1046366442049781870/Pull_Pinch_GIF_-_Pull_Pinch_Funny_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/993633626719780924/1046366442557280267/Pull_Pinch_Sticker_-_Pull_Pinch_Mochi_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/993633626719780924/1046366441764573254/Chicken_Bro_Chicken_GIF_-_Chicken_Bro_Chicken_Pinch_-_Discover__Share_GIFs.gif"
        ]
        embed=discord.Embed(title=f"{ctx.author.name} is pinching {user.name} !!",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)      

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(pinch(bot))       
    print("pinch is loaded")    
       
        
   