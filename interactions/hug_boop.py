import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import CommandTree
import requests
import discord.ui
from discord.ui import Button,View
import random

class hug(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["Hug"])
    async def hug(self,ctx,user:discord.Member=None):
        if user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        randomgifs = [
            "https://media.discordapp.net/attachments/1045618240900050954/1045663962882134066/kirby-hug.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1045663980926029834/super-smash-bros-kirby.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1045666359662616627/a57a2cafc38622f62edecb82be278973.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046476088014020779/cute.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046476097597997146/polar-bear.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046476108192813137/dc6df1c-7186e0ed-c0e3-4940-8b2c-7a5707f1ad7e.gif?width=606&height=606",
            "https://media.discordapp.net/attachments/1045618243013984296/1046476112441651251/ddu4ws4-0d31ccf4-d249-4a23-86b3-3d42b7311307.gif?width=1083&height=607",
            "https://media.discordapp.net/attachments/1045618243013984296/1046476124143747142/200w_1.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046476125502713876/giphy_3.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046476787791708200/download_3.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046476788118859876/Tkthao219_Bubududu_Sticker_-_Tkthao219_Bubududu_Peach_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046476788471169034/Tuagom_Puffy_Bear_GIF_-_Tuagom_Puffy_Bear_Kiss_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046476788907393034/Mochi_Cat_Kiss_GIFs___Tenor.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046476789318430801/download_2.gif?width=606&height=606",
            "https://media.discordapp.net/attachments/1045618243013984296/1046476790807412896/download_1.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046476790522183690/Animated_Love_GIF_-_Animated_Love_Hug_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046476790140514355/Hugging_Cat_GIF_-_Hugging_Cat_Couples_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047167473687986227/cartoon-hug.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047167475281842276/hug.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047167478041690273/hug-cartoon.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047167478939258971/love-jumping.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047167573298520147/puuung-love.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047167585294237696/sushichaeng-adventure-time.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047167589513707530/tonari-no-kaibutsu-kun-my-little-monster.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047167592625881128/hug_1.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047167594903376004/hug_2.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047167612309749770/hug-cute.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047167673139732540/hug-kiss.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047167993685233715/bluey-bandit.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047168005047590942/miraculous-ladybug-lukanette.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047168012861571163/dnd-cartoon-dnd.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047168013046128692/ninjala-van.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047168015126503505/love-cartoon.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047168071388909638/kiyoi-mizushima_1.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047168075386060820/despicable-me-minions.gif"
        ]
        embed=discord.Embed(title=f"{ctx.author.name} hugs {user.name}",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)   

    @commands.command(aliases=["boops","bp"])
    async def boop(self,ctx,user:discord.Member=None):
        if user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        randomgifs = [
            "https://media.tenor.com/t2cbTFyvWVYAAAAC/consistent-boops-ollie-boop.gif",
            "https://media.tenor.com/ncx61LPfp2UAAAAd/chub-chubs.gif",
            "https://media.tenor.com/JjZtInaG4pEAAAAd/boop-cat-boop.gif",
            "https://media.tenor.com/HZWeNnmcbBYAAAAC/cat-boop.gif",
            "https://media.tenor.com/88HZjGgr3k0AAAAd/doggo-boop.gif",
            "https://media.tenor.com/AeCsQHEk-hwAAAAd/luna-nose.gif",
            "https://media.tenor.com/_dEtNdPuQjoAAAAd/gentle-boops-i-boop-you.gif",
            "https://media.tenor.com/le048t71RHwAAAAC/boop.gif",
            "https://media.tenor.com/1vUzPbEZ6fYAAAAd/gentle-boop-gentle-bup.gif",
            "https://media.tenor.com/RdxHFlPvKFUAAAAd/boop.gif",
            "https://media.tenor.com/3ZR8ctqIr6kAAAAd/dog-i-boop-you.gif",
            "https://media.tenor.com/oTBal8OUccQAAAAd/i-bestow-upon-you-a-boop-ollie-boop.gif",
            "https://media.tenor.com/j-C2_RyIDPcAAAAC/i-boop-you-ollie-boop.gif",
            "https://media.tenor.com/_dEtNdPuQjoAAAAd/gentle-boops-i-boop-you.gif",
            "https://media.tenor.com/J5PLqHYcyIcAAAAC/you-have-been-booped-booped.gif",
            "https://media.tenor.com/hW3o39B0zUcAAAAC/boop-cat.gif",
            "https://media.tenor.com/wdus8iPe9yAAAAAd/leothelab-boop.gif",
            "https://media.tenor.com/hwqX6sd39xMAAAAC/boop-shnoop.gif",
            "https://media.tenor.com/AOyF2C6ok0cAAAAd/fox-animation.gif"
              ]    
        embed=discord.Embed(title=f"{ctx.author.name} booped {user.name} ",color = discord.Colour.purple())    
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)        
       

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(hug(bot))       
    print("hug, boop is loaded")    
       
    
    