import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import CommandTree
import requests
import discord.ui
from discord.ui import Button,View
import random

class marry(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    @commands.command(aliases=["Marry","MARRY"])
    async def marry(self,ctx,user:discord.Member=None):
        if user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        randomgifs = [
            "https://media.discordapp.net/attachments/949680123869814794/1046885786601136138/sportsmanias-just-married.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046885794087960626/anineogray-wedding.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046885802166206564/marriage-marry.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046885806226276432/TerribleRemorsefulCottontail-size_restricted.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046885979367165962/804a7b8872de5db7d3dee11a94a89449.gif?width=606&height=606",
            "https://media.discordapp.net/attachments/949680123869814794/1046885984442269758/tumblr_mllx0atPDj1r1r3hjo1_500.gif"
            ]
        
        embed=discord.Embed(title=f"{ctx.author.name} married {user.name} !! Congratulations to the newly weds",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)    

    @commands.command(aliases=["Love"])
    async def love(self,ctx,user:discord.Member=None):
        if user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        randomgifs = [
            "https://media.discordapp.net/attachments/1045618240900050954/1045664205388398643/love-kirby.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046156748983124050/love-gif.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046156765412200528/icegif-876.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046156775352713326/icegif-592.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046156785515495504/icegif-581.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046157241130156102/DarlingRectangularIsabellinewheatear-max-1mb.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046157205617004594/cute-love.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046157189548609546/WindingShorttermAfricanharrierhawk-size_restricted.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046157176118456441/bunny-rabbit.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046363448302379068/Muddu_Love_Sticker_-_Muddu_Love_Heart_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047171901522456576/love-kiss.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047171906714996836/mocha-mucha.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047171906840830043/milk-and-mocha-bears.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047171912603799653/love-hug.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047171919474069645/good-night-love-you.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047171931113271356/relajamiento-y-amor-love.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047172271678169138/love-you.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047172280960155699/love.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047172283376087150/emote.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047172288031752232/milk-and-mocha-bears_1.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047172307036160000/love-rabbit.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047172384316198943/donald-love.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047172387264811099/animated-cute.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047172392352493609/cartoon-heart.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047172395561140266/feelings-love.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047172402955702423/duck-cute.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047174325544943637/sending-love.gif"
        ]
        embed=discord.Embed(title=f"{ctx.author.name} sends love to {user.name}",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed) 

    @commands.command(aliases=["Nom","NOM"])
    async def nom(self,ctx,user:discord.Member=None):
        if user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        randomgifs = [
            "https://media.discordapp.net/attachments/949680123869814794/1046876009003225158/sMP.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046876014762008646/45ba063ad9212afec9fed28e79fbfe09.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046876072601456681/PaltryMadKusimanse-max-1mb.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046876072991543408/fe8f2a77e1f3b100e81ee0f1f454542a.gif"
            ]
        
        embed=discord.Embed(title=f"{ctx.author.name} noms on {user.name} !!",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)     

    @commands.command(aliases=["Punch",'punching'])
    async def punch(self,ctx,user:discord.Member=None):
        if user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        randomgifs = [
            "https://media.discordapp.net/attachments/1045618243013984296/1046657546347364432/punch-punching.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054492842732564481/punch10.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054492843072294982/punch9.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054492843718230096/punch8.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054492844607410206/punch6.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054492845492416622/punch4.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054492845836341348/punch3.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054492846192869443/punch2.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054492846549381172/punch1.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054492950027055145/punch12.gif"
        ]
        
        embed=discord.Embed(title=f"{ctx.author.name} punches {user.name} hard!",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed) 

    @commands.command(aliases=["STFU","shut","shutup","Shut"])
    async def stfu(self,ctx,user:discord.Member=None):
        if user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot and m.id != 530824411759116288]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        randomgifs = [
            "https://media.tenor.com/mBFdHahC7SwAAAAd/lmao-stfu.gif",
            "https://media.tenor.com/8HCiYkHSLWgAAAAd/stfu.gif",
            "https://media.tenor.com/jmEeIVgFhjQAAAAC/stfu-shut-up.gif",
            "https://media.tenor.com/2pgy64Sh5wYAAAAd/stfu-punching-stfu-gif.gif",
            "https://media.tenor.com/KKS3hJ33_sUAAAAC/stfu.gif",
            "https://media.tenor.com/QDuyGHlwjr4AAAAd/stfu.gif",
            "https://media.tenor.com/P_hk6dBzWUcAAAAC/stfu-can-you-stfu.gif",
            "https://media.tenor.com/_vBlPe9UqrEAAAAC/plastic-chair-plastic-knife.gif",
            "https://media.tenor.com/4__-628PgsUAAAAd/snoop-dogg-rapper.gif",
            "https://media.tenor.com/rqY-hzlUJokAAAAC/shut-up.gif",
            "https://media.tenor.com/kE818ge-WMcAAAAd/stfulmfao.gif",
            "https://media.tenor.com/TIvSjriG5k8AAAAC/stfu-discord.gif",
            "https://media.tenor.com/9XOxc5bL3ikAAAAC/stfu-pls.gif",
            "https://media.tenor.com/_c-tBlx1g0sAAAAd/nobody-care.gif",
            "https://media.tenor.com/6GhnldRykacAAAAd/charley3-stfu.gif",
            "https://media.tenor.com/DNsCIM3ExTkAAAAC/stfu-shut-up.gif",
            "https://media.tenor.com/br56Ph5l_moAAAAd/idc-stfu.gif",
            "https://media.tenor.com/wGYP0T-roIoAAAAC/grackles-shut-the-fuck-up.gif",
            "https://media.tenor.com/b69Hw9iU3IgAAAAC/chemmanna-chemmanna-stfu.gif",
            "https://media.tenor.com/dzYLz0zrtrgAAAAC/shut-up-just.gif",
            "https://media.tenor.com/I2x1XSezVDcAAAAC/chandler-bing-shut-up.gif",
            "https://media.tenor.com/82m9RQSFWboAAAAd/shutupangry.gif",
            "https://media.tenor.com/pHJlCcfg3LQAAAAC/penny-how-bout-you-stfu.gif",
            "https://media.tenor.com/JUpxZb-3DiAAAAAC/shut-up.gif",
            "https://media.tenor.com/edyHKYbvAiAAAAAC/ronald-mcdonald.gif"

            ]
        
        embed=discord.Embed(title=f"{ctx.author.name} is telling {user.name} to STFU !",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)       

    @commands.command(aliases=["sipping","slurp","sips","Sip"])
    async def sip(self,ctx):
        randomgifs = [
            'https://media.discordapp.net/attachments/1035565430422642718/1054479077593067580/sip3.gif',
            "https://media.discordapp.net/attachments/1035565430422642718/1054479078083792927/sip4.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054479078469673040/sip5.gif?width=606&height=606",
            "https://media.discordapp.net/attachments/1035565430422642718/1054479078821998592/sip6.gif?width=521&height=607",
            "https://media.discordapp.net/attachments/1035565430422642718/1054479079207866518/sip7.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054479079711191040/sip8.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054479080080281661/sip9.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054479080466161674/sip10.gif?width=606&height=606",
            "https://media.discordapp.net/attachments/1035565430422642718/1054479080860430426/sips.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054479081187577916/sips2.gif",
            "https://media.tenor.com/nmv_0Z6axwoAAAAi/sip-sipping-tea-gif.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054482139216871424/sip16.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054482139636310046/sip17.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054482139984433232/sip18.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054482140328362115/sip19.gif?width=606&height=606",
            "https://media.discordapp.net/attachments/1035565430422642718/1054482140676493312/sip20.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054482141053976748/sip21.gif?width=604&height=606",
            "https://media.discordapp.net/attachments/1035565430422642718/1054482141402107924/sip22.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054482141741842522/sip23.gif?width=606&height=606",
            "https://media.discordapp.net/attachments/1035565430422642718/1054482142199029821/sip24.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054482142517792878/sip25.gif?width=606&height=606",
            "https://media.discordapp.net/attachments/1035565430422642718/1054482231755821174/sip26.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054482232347197530/sip27.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054482232728887306/sip28.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054482233102192650/sip29.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054482233437716490/sip30.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054482234515652720/sips.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054483474716827748/sip32.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054483475106893884/sip33.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054483475450822706/sip34.gif?width=606&height=606"

            ]
        
        embed=discord.Embed(title=f" {ctx.author.name} is slurping their drink",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)            

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(marry(bot))       
    print("marry, love, nom, punch, shut, sip is loaded")    
       
        
   