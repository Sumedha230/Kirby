import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import CommandTree
import requests
import discord.ui
from discord.ui import Button,View
import random

class smirk(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=["smirking","smirks"])
    async def smirk(self,ctx,user:discord.Member=None):
        if user == None:
            embed=discord.Embed(title=f"{ctx.author.name} is smirking ",color = discord.Colour.purple())
        else:
            embed=discord.Embed(title=f"{ctx.author.name} is smirking at {user.name}",color = discord.Colour.purple())    
        if user!=None and user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return 
        randomgifs = [
            "https://media.discordapp.net/attachments/1035565430422642718/1054486185080258661/smirk.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054486185797505154/smirk1.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054486186183377036/smirk2.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054486186644733962/smirk3.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054486186984493227/smirk4.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054486187311644822/smirk5.gif?width=606&height=606",
            "https://media.discordapp.net/attachments/1035565430422642718/1054486187861082212/smirk6.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054486188322476082/smirk7.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054486188834177054/smirk8.gif?width=485&height=606",
            "https://media.discordapp.net/attachments/1035565430422642718/1054486189228425356/smirk9.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054486243666317445/smirk10.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054486243959910590/smirk11.gif?width=401&height=606",
            "https://media.discordapp.net/attachments/1035565430422642718/1054486244341579846/smirk12.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054486244702310462/smirk13.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054486245058818058/smirk14.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054486245406933072/smirk15.gif?width=369&height=606",
            "https://media.discordapp.net/attachments/1035565430422642718/1054486246111588362/smirk17.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054486246543589526/smirk18.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054486246895931442/smirk19.gif?width=606&height=606",
            "https://media.discordapp.net/attachments/1035565430422642718/1054486370091020409/smirk23.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054486370812448768/smirk25.gif?width=519&height=606",
            "https://media.discordapp.net/attachments/1035565430422642718/1054486371164762122/smirk26.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054486371865219112/smirk27.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054486372322390066/smirk28.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054486372712456192/smirk29.gif?width=628&height=606",
            "https://media.discordapp.net/attachments/1035565430422642718/1054486392899645610/smirk30.gif"
            ]
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)   
    @commands.command()    
    async def beetle(self,ctx):
        randomgifs = [
            "https://media.discordapp.net/attachments/1035565430422642718/1054488247415341239/beetle7.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054488247763472484/beetle6.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054488248111607908/beetle5.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054488248434556948/beetle4.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054488248761716838/beetle3.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054488249084686407/beetle1.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054488249420218440/beetle.gif"
        ]
        embed=discord.Embed(title=f"{ctx.author.name} is average Beetle enjoyer",color = discord.Colour.purple())    
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)

    @commands.command(aliases=["Cuddle","cuddles",'cuddling'])
    async def cuddle(self,ctx,user:discord.Member=None):
        if user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        randomgifs=[
            "https://media.tenor.com/5PpFO7VcU0MAAAAC/cuddle.gif",
            "https://media.tenor.com/xMAxRg5iwqcAAAAC/snuggle-cute.gif",
            "https://media.tenor.com/lgjnVcfWdpEAAAAC/love-snuggle.gif",
            "https://media.tenor.com/ZhwUZCqJCNMAAAAC/love-you.gif",
            "https://media.tenor.com/8F2KbUiJv30AAAAC/emdj-hug.gif",
            "https://media.tenor.com/bLttPccI_I4AAAAC/cuddle-anime.gif",
            "https://media.tenor.com/TsL3G4aPH2wAAAAC/milk-and-mocha-milk.gif",
            "https://media.tenor.com/lOX9rc2f36EAAAAC/milk-and-mocha-milkbear.gif",
            "https://media.tenor.com/pPMLO1IzPWIAAAAC/miss-may-tommy.gif",
            "https://media.tenor.com/FgfGLXI3mIQAAAAC/chibi-cute.gif",
            "https://media.tenor.com/H7i6GIP-YBwAAAAd/a-whisker-away-hug.gif",
            "https://media.tenor.com/q95BTrmPJqkAAAAd/cats-cat.gif",
            "https://media.tenor.com/HUE1PtW9UcYAAAAd/whiskey-sleep-cuddles.gif",
            "https://media.tenor.com/1BV_mELNCEkAAAAd/love-cuddle.gif",
            "https://media.tenor.com/qTb7G2FPsIYAAAAC/stiles-stilinski-malia-tate.gif",
            "https://media.tenor.com/FoFMuwi0kfoAAAAd/cat-cuddle.gif",
            "https://media.tenor.com/UheHuhz9o5IAAAAC/station19-maya-and-carina.gif",
            "https://media.tenor.com/gHAkopm2abMAAAAd/couple-sleeping-love.gif",
            "https://media.tenor.com/iOG9_cXxJzsAAAAC/sleepy-head-morning.gif",
            "https://media.tenor.com/VEPWJS4bxRIAAAAd/cuddle-game.gif",
            "https://media.tenor.com/rONLuXsZr2kAAAAd/cuddle-couple.gif",
            "https://media.tenor.com/wFxMAqCsQDoAAAAd/cats.gif",
            "https://media.tenor.com/pB-4ZWsqcQoAAAAd/cat-hug.gif",
            "https://media.tenor.com/9SG9pGSs1eIAAAAd/anime-cuddle-cuddle.gif",
            "https://media.tenor.com/-NFrGNy9UAUAAAAC/hugs-kiss.gif",
            "https://media.tenor.com/BmbTYhCZ5UsAAAAC/yuri-sleeping-yuri-sleep.gif",
            "https://media.tenor.com/d6IdGdhC80MAAAAC/kiss-love.gif",
            "https://media.tenor.com/mUB511Ai_K0AAAAC/mood-cuddles.gif",
            "https://media.tenor.com/GTlDCm4P4EsAAAAd/kitty-kitten.gif",
            "https://media.tenor.com/APJb4HKo9SsAAAAd/cuddle-love.gif",
            "https://media.tenor.com/fy2qB_-pAA8AAAAM/otter-cuddles-cuddles.gif",
            "https://media.tenor.com/EKlPRdcuoccAAAAC/otter-cute.gif",
            "https://media.tenor.com/y-04JHW1D5oAAAAd/otter-otters.gif",
            "https://media.tenor.com/YQEOx4ngGnAAAAAC/cat-cuddling.gif",
            "https://media.tenor.com/hP-wj0PBmR0AAAAd/love-snuggle.gif",
            "https://media.tenor.com/SrpgTEtutQYAAAAC/cuddles-mongooltje.gif",
            "https://media.tenor.com/xRLWMxHzNq8AAAAd/pug-cuddles.gif",
            "https://media.tenor.com/AIOnRY9EW9YAAAAd/bunny-cuddle.gif",
            "https://media.tenor.com/9W4-irrCChgAAAAd/otter-otters.gif",
            "https://media.tenor.com/ftIWvZpAqsIAAAAC/cuddle-otter.gif"
        ]
        embed=discord.Embed(title=f"{ctx.author.name} is cuddling {user.name} !",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)      

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(smirk(bot))       
    print("smirk, cuddle is loaded")    
       
        
   