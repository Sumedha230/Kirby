import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import CommandTree
import requests
import discord.ui
from discord.ui import Button,View
import random

class salute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["salutes",'saluting'])
    async def salute(self,ctx,user:discord.Member=None):
        if user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        randomgifs = [
            "https://media.tenor.com/0mggmptfog0AAAAC/hai-salute.gif",
            "https://media.tenor.com/5H3pUTkK7eoAAAAC/johnny-depp-pirate.gif",
             "https://media.tenor.com/LdAr7ZnMsaMAAAAd/yes-sir-yes-boss.gif",
            "https://media.tenor.com/RXhoHZGn0NIAAAAC/jack-black-yes.gif",
            "https://media.tenor.com/0mggmptfog0AAAAC/hai-salute.gif",
            "https://media.tenor.com/d2X7R2oF2UYAAAAC/glorij-salute.gif",
            "https://media.tenor.com/I6BxzCDGRnkAAAAd/partybear-salute.gif",
            "https://media.tenor.com/GgmPs3PcUukAAAAC/okey-dokey-donald-duck.gif",
            "https://media.tenor.com/lHf6NVXAjqEAAAAC/homelander-salute.gif",
            "https://media.tenor.com/fj1bulyAUywAAAAd/salute-burt-lancaster.gif",
            "https://media.tenor.com/T7C4Ty-ETacAAAAC/america-captain-america.gif",
            "https://media.tenor.com/G7bV2qO98-sAAAAd/salute.gif",
            "https://media.tenor.com/1zepSl-gLoEAAAAC/officer-doofy-salute.gif",
            "https://media.tenor.com/WvYDxpcx6aEAAAAC/salute-military.gif",
            "https://media.tenor.com/VHKnmSrUnNwAAAAC/salute-bet.gif",
            "https://media.tenor.com/5H3pUTkK7eoAAAAC/johnny-depp-pirate.gif",
            "https://media.tenor.com/zMu9xwYsx2YAAAAd/vei-veibae.gif",
            "https://media.tenor.com/CDClB-mqD7sAAAAC/tom-and-jerry-tom-salute.gif",
            "https://media.tenor.com/k9tz0ltJYEIAAAAC/aimoto-rinku-d4dj-first-mix.gif",
            "https://media.tenor.com/28rhz0kPBmMAAAAC/youjo-senki-salute.gif",
            "https://media.tenor.com/R4NwWNfQ-jYAAAAC/hans-solo-salute.gif",
            "https://media.tenor.com/Fk57yabSTC0AAAAC/captain-america-salute.gif",
            "https://media.tenor.com/1kyq1SUWxQMAAAAC/salute-military.gif",
            "https://media.tenor.com/LLuVXeEPbh0AAAAC/super-meat-boy-meat-boy.gif",
            "https://media.tenor.com/RHlHtJC2STsAAAAC/katharine-hepburn.gif",
            "https://media.tenor.com/whzCBaPdjkgAAAAC/salute-team.gif",
            "https://media.tenor.com/xo490p7FtOYAAAAC/salute-good-bye.gif",
            "https://media.tenor.com/b-rNht0eLhIAAAAC/anime-girl-salute.gif",
            "https://media.tenor.com/aB4XAyZND3UAAAAC/salute-armin.gif",
            "https://media.tenor.com/M4KkAflIrnwAAAAC/power-rangers-megaforce-two-finger-salute.gif"
       
        ]
        
        embed=discord.Embed(title=f"{ctx.author.name} is saluting {user.name}!",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)     

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(salute(bot))       
    print("salute is loaded")    
       
        
   