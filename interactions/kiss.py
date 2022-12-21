import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import CommandTree
import requests
import discord.ui
from discord.ui import Button,View
import random

class kiss(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["Kiss"])
    async def kiss(self,ctx,user:discord.Member=None):
        if user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        randomgifs = [
            "https://media.discordapp.net/attachments/1045618240900050954/1045658804034994226/0d095e578f2c91ad060fada5cde2fd4ebf6f9d18r1-450-375_hq.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1045659012743561316/kirby-kiss.gif",
            "https://cdn.weasyl.com/static/media/bf/d3/6d/bfd36da752a5cfdf862b01ebb4db652308807f907677e1cc0167d20dabc17b94.gif",
            "https://media.discordapp.net/attachments/1005851300195487875/1045660804852240455/IMG_9527.gif",
            "https://media.discordapp.net/attachments/1005851300195487875/1045660805162598422/IMG_9528.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046363447660654632/Kuzu_No_Honkai_Anime_GIF_-_Kuzu_No_Honkai_Anime_Kiss_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046363448029741056/Cute_Blow_Kiss_GIF_-_Cute_Blow_Kiss_Hearts_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046363448633733140/Tuagom_Puffybear_GIF_-_Tuagom_Puffybear_Exercise_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046363448960876596/Kissykissy_GIF_-_Kissykissy_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046363449267068998/Bear_Angry_GIF_-_Bear_Angry_Kiss_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046363449611005962/Smoochie_Smooches_Sticker_-_Smoochie_Smooches_Kisses_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046363449908789258/Animated_Kiss_Gif_Images.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046363450244341800/Milk_And_Mocha_Bear_Kiss_GIF_-_Milk_And_Mocha_Bear_Kiss_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047164877652902001/kissing-you.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047164878449815592/kiss-hugekiss.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047164886813253704/kiss-anime.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047164887966695557/lumity-lumity-kiss.gif?width=545&height=606",
            "https://media.discordapp.net/attachments/949680123479728146/1047164897470992424/cute-choobs.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047165170251743242/kiss.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047165170964779008/love-cute.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047165564025577512/lovestruck-kiss.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047165569339756554/beijo-cartoon.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047165580215590942/kiss-rabbit.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047165582765735936/koi-to-uso-kiss.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047165586343473233/kiss_1.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047165587215896666/kiss-sephiroth.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047165612880834600/mickey-mouse-minnie-mouse.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047165866124509194/fuuka-naruto.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047165870511755294/kiss-lovers.gif"
        ]
        embed=discord.Embed(title=f"{ctx.author.name} has kissed {user.name}",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)    

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(kiss(bot))       
    print("kiss is loaded")    
       
    