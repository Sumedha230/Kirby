import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import CommandTree
import requests
import discord.ui
from discord.ui import Button,View
import random

class sit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["Sit",'sitting'])
    async def sit(self,ctx,user:discord.Member=None):
        if user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        randomgifs = [
            "https://media.discordapp.net/attachments/1045618243013984296/1046471106657259530/dog-cat.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046471124340453437/200.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046472037327179867/They_cheat_at_staring_contests_.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046472037851463790/Chair_You_Never_Hold_Still.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046473490133426197/Hank_the_Chihuahua_and_Angus_the_Great_Dane_-_DogPerDay.png?width=729&height=606",
            "https://media.discordapp.net/attachments/1045618243013984296/1046473490489954344/Animals_Sitting_on_Capybaras.jpg?width=454&height=606",
            "https://media.discordapp.net/attachments/1045618243013984296/1046473490741592165/brenna-louise.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046473491211362344/Dog_Puppy_GIF_-_Find__Share_on_GIPHY.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046473493480493066/New_Beginnings_66.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046473493786656788/download.jpg?width=651&height=606"
             ]
        embed=discord.Embed(title=f"{ctx.author.name} sits on {user.name} and crushes them!",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)       

   

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(sit(bot))       
    print("sit is loaded")    
       
        
   