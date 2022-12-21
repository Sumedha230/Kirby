import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import CommandTree
import requests
import discord.ui
from discord.ui import Button,View
import random

class fuck(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(aliases=["Fuck"])
    async def fuck(self,ctx,user:discord.Member=None):
        if user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        randomgifs = [
            "https://media.discordapp.net/attachments/1045618240900050954/1045661560326078535/how-did-they-how-did.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1045661934776754217/8768f928-3eb6-4254-9ffc-a378608a0fa8_text.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1045663257639272468/5kozue.jpg",
            "https://media.discordapp.net/attachments/1045618243013984296/1046475203296890900/caught-in.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046475208497844306/des2g4q-66b842d0-5e2b-4022-ae1e-41bb56bd77db.jpg?width=575&height=606",
            "https://media.discordapp.net/attachments/1045618243013984296/1046475214000754768/94aba787a7c7cab988321e224957e9c6c1f0db1ad92100eeef52232048ddb3ff_1.jpg?width=663&height=607",
            "https://media.discordapp.net/attachments/1045618243013984296/1046475215296798882/c411e4e207c54d2d5705fe8df09efd02f02614c395103128081c56b97d8a8d1c_1.jpg?width=485&height=606",
            "https://media.discordapp.net/attachments/1045618243013984296/1046475224360685608/ceeef3dc54fee1701d3331b48f948bacc0d1329ec436c6c4750bc6e67942213e_1.jpg"
        ]
        embed=discord.Embed(title=f"{ctx.author.name} tried to e-fuck {user.name} and were caught in 4k",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed) 

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(fuck(bot))       
    print("fuck is loaded")    
       
        
   
