import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import CommandTree
import requests
import discord.ui
from discord.ui import Button,View
import random

class laugh(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=["laughing","Laugh","Laughing"])
    async def laugh(self,ctx,user:discord.Member=None):
        if user == None:
            embed=discord.Embed(title=f"{ctx.author.name} is laughing",color = discord.Colour.purple())
        else:
            embed=discord.Embed(title=f"{ctx.author.name} is laughing at {user.name}",color = discord.Colour.purple())    
        if user!=None and user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return 
        randomgifs = [
            "https://media.discordapp.net/attachments/1045618243013984296/1046361695561453688/Happy_Cracking_Up_GIF_-_Find__Share_on_GIPHY.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046361695859261490/Minions_Laugh_GIF_-_Minions_Despicable_Me_Laugh_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046361696123506779/Moms_Mabley__The_Dirty_Granny_of_Stand_Up.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046361699881586718/Happy_Laugh_Sticker_-_Happy_Laugh_Funny_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046361700242313286/Celebrity__Entertainment___Chris_Evans_Does_This_1_Thing_Almost_Every_Time_He_Laughs_and_Its_Freakin_Adorable.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046361700598812692/Cracking_Up_Reaction_GIF_-_Find__Share_on_GIPHY.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046361700967923803/33_Random_Pics_To_Amuse_and_Entertain.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046361701295083540/When_someone_suggests_you_should_maybe_give_up_coffee_for_a_week_.gif"
        ]
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)   

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(laugh(bot))       
    print("laugh is loaded")    
       
        
   