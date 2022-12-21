import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import CommandTree
import requests
import discord.ui
from discord.ui import Button,View
import random

class lie(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["lie","Lie","Liar","LIAR",'lying'])
    async def liar(self,ctx,user:discord.Member=None):
        if user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        randomgifs = [
            "https://media.tenor.com/lEmpYF98RJMAAAAC/joker-liar-liar.gif",
            "https://media.tenor.com/zPMz7FtaEGoAAAAd/you-know-you-lying.gif",
            "https://media.tenor.com/mBebRanGR0IAAAAd/zootopia-you-liar.gif",
            "https://media.tenor.com/nbGzicBmHW0AAAAC/amanchabukswar.gif",
            "https://media.tenor.com/ZZi-EEsk_X8AAAAC/liar-mad.gif",
            "https://media.tenor.com/4fNbw8ZolPwAAAAC/stop-lying-why-you-always-lying.gif",
            "https://media.tenor.com/FxZKX1VySIgAAAAd/lying-why-you-always-lying.gif",
            "https://media.tenor.com/upA200Y35LEAAAAd/nope-thas-a-lie-thasa-lie.gif",
            "https://media.tenor.com/7v9jzDMWnz4AAAAC/rickey-smiley-thats-a-fucking-lie.gif",
            "https://media.tenor.com/oZrRoDQDXZ4AAAAC/anakin-liar.gif",
            "https://media.tenor.com/RcqfIAjFt5wAAAAC/spongebob-squarepants-patrick-star.gif",
            "https://media.tenor.com/Ixkt-65LcSAAAAAC/khloe-kardashian-liar.gif",
            "https://media.tenor.com/yXbIThapEjEAAAAC/the-simpsons-bender.gif",
            "https://media.tenor.com/RN_ZCtgVAP0AAAAC/we-know-youre-lying-tiffany-wallace.gif",
            "https://media.tenor.com/OPpHy63ti7sAAAAd/you-think-i-dont-know-what-a-lying-man-looks-like-marianne-jean-baptiste.gif",
            "https://media.tenor.com/eWBBzvu8uLsAAAAC/now-i-know-what-it-looks-like-when-you-lie-tallinn.gif",
            "https://media.tenor.com/tDxmO-ZJTRQAAAAC/telling-lies-oh-really.gif",
            "https://media.tenor.com/aeWIy-mPwMIAAAAd/you-lie-funny-animals.gif",
            "https://media.tenor.com/KC64tt5FIbsAAAAC/lie-zim.gif",
            "https://media.tenor.com/_a0jQcBtX8QAAAAC/you-lie-stranger-things.gif",
            "https://media.tenor.com/TlaGwI1L-TEAAAAC/marriedtomed-married-to-medicine.gif",
            "https://media.tenor.com/nJYAj-fbk0sAAAAC/disguised-toast-toast-liar.gif",
            "https://media.tenor.com/K1kMp4W47mAAAAAC/youre-a-liar-priscilla-owens.gif",
            "https://media.tenor.com/QmtmQsP7UZIAAAAC/youre-a-liar-kevin-hart.gif",
            "https://media.tenor.com/7cJrVoOHBSQAAAAC/youre-a-liar-nadia-vulvokov.gif",
            "https://media.tenor.com/rZkbqOMk9zYAAAAd/youre-a-freakin-liar-lies.gif",
            "https://media.tenor.com/OzAUohohRksAAAAC/youre-a-freaking-liar-freaking-liar.gif",
            "https://media.tenor.com/UzNVGKAJgcwAAAAC/you-are-a-liar-steven-grant.gif",
            "https://media.tenor.com/Cs9ySzxxH1UAAAAC/you-are-such-a-liar-thats-not-true.gif",
            "https://media.tenor.com/47d7uhOyke8AAAAC/youre-such-a-liar-lies.gif",
            "https://media.tenor.com/kYa8KucQUysAAAAd/liar-freaking-liar.gif",
            "https://media.tenor.com/fUJOdchNgp0AAAAC/liar-captain-spock.gif",
            "https://media.tenor.com/P0KAKqaWsPoAAAAC/real-housewives-real.gif",
            "https://media.tenor.com/lKi031Ys4pgAAAAd/shark-tale-oh-youre-a-liar.gif",
            "https://media.tenor.com/Y-BxTt_zLRwAAAAC/youre-a-liar-eric-cartman.gif",
            "https://media.tenor.com/QhMeBH8SuTIAAAAd/lying-liar.gif",
            "https://media.tenor.com/oU8o8DPW9X8AAAAC/eyes-puss-in-boots.gif",
            "https://media.tenor.com/U7RGcgYK8SIAAAAC/frank-accuse.gif",
            "https://media.tenor.com/FnsxpY-ydboAAAAd/lying-liar.gif",
            "https://media.tenor.com/xd-_VjSWOE0AAAAC/critical-bard-cb.gif",
            "https://media.tenor.com/nPTwMqBAxDoAAAAC/ellen-shade.gif",          
        ]
        
        embed=discord.Embed(title=f"{ctx.author.name} is calling {user.name} a liar !",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)    

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(lie(bot))       
    print("lie is loaded")    
       
        
   