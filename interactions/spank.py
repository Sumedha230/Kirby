import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import CommandTree
import requests
import discord.ui
from discord.ui import Button,View
import random

class spank(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["Spank","SPANK","spanking","Spanking"])
    async def spank(self,ctx,user:discord.Member=None):
        if user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        randomgifs = [
            "https://media.tenor.com/xRq5_v71Gc0AAAAC/mochi-cat-spanking.gif",
            "https://media.tenor.com/B2uwAzBjCVIAAAAC/mad-tom-and-jerry.gif",
            "https://media.tenor.com/q4gfw2sfTiwAAAAC/bubu-spank.gif"
            "https://media.tenor.com/qFPN3DN38EQAAAAC/momonofu-hololive.gif",
            "https://media.tenor.com/ThVjkORaVm4AAAAC/planktoons-plankie.gif",
            "https://media.tenor.com/IsatImqfv9cAAAAC/looney-tunes-foghorn-leghorn.gif",
            "https://media.tenor.com/tqULzMukOsoAAAAd/moti-spanks.gif",
            "https://media.tenor.com/BuNcNGQ22DsAAAAC/batman-beyond-deedee.gif",
            "https://media.tenor.com/E9Bbq5HfJxEAAAAC/cartoon-spamking-clock.gif",
            "https://media.tenor.com/7xhgL0ckmH4AAAAd/wake-up.gif"

            ]     
        embed=discord.Embed(title=f"{ctx.author.name} is spanking {user.name} !",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)     

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(spank(bot))       
    print("spank is loaded")    
       
    