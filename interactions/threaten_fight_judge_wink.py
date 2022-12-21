import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import CommandTree
import requests
import discord.ui
from discord.ui import Button,View
import random

class threaten(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["Threaten","THREATEN",'threat'])
    async def threaten(self,ctx,user:discord.Member=None):
        if user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        randomgifs = [
            "https://media.discordapp.net/attachments/949680123479728146/1047092343041445948/giphy_2.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047092349601337374/giphy_1.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047092355066511391/d6a692e62b02933ed00e8ccc16657ed7.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047092398087487538/b99-knife.gif"
            ]
        
        embed=discord.Embed(title=f"{ctx.author.name} is threating {user.name}'s e-life !",color = discord.Colour.purple())
        embed.add_field(name= "Aftermath",value=f"{user.name} is very scared now and won't be able to log in again")
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)     

    @commands.command(aliases=["Fight",'fighting','fights'])
    async def fight(self,ctx,user:discord.Member=None):
        if user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return    
        randomgifs =[
            "https://media.tenor.com/l5sIE_3H3EEAAAAd/cats-fighting-fighting-cats.gif",
            "https://media.tenor.com/CZJGXrvl9LoAAAAd/cats-fighting-mma-takedown.gif",
            "https://media.tenor.com/Y2JNQLkzz8sAAAAd/cats-funny.gif",
            "https://media.tenor.com/saVFWCC23KoAAAAd/cat-fight-cats-fighting.gif",
            "https://media.tenor.com/UW6vxndZpfMAAAAd/cat-meme.gif",
            "https://media.tenor.com/szPtb6lqakIAAAAC/beating-up-beating-up-lilo.gif",
            "https://media.tenor.com/iWKGJATqdTEAAAAd/martin-lawrence-beat-up.gif",
            "https://media.tenor.com/HsnuQ0vN1s8AAAAC/naruto-sasuke.gif",
            "https://media.tenor.com/N_ZmqyzFKXUAAAAd/stan-twitter.gif",
            "https://media.tenor.com/a0F-sE53rgcAAAAC/cats-fight.gif",
            "https://media.tenor.com/6QwxgzQLGKUAAAAC/battle.gif",
            "https://media.tenor.com/8BUHGz3NKKUAAAAC/angry-frustrated.gif",
            "https://media.tenor.com/u37OUTuQ-sQAAAAC/baby.gif",
            "https://media.tenor.com/Ls2Xy-p7vcwAAAAd/cat-kitty.gif",
            "https://media.tenor.com/oziRBzETrrYAAAAC/jin-mori-fight.gif",
            "https://media.tenor.com/L0U84S9YTrYAAAAC/pikachu-slap.gif",
            "https://media.tenor.com/0WJHZ449SSQAAAAC/hasbulla-hasbullah.gif",
            "https://media.tenor.com/ZF9T7-Ily9EAAAAC/fighting-cat-cat-vs-human.gif",
            "https://media.tenor.com/1Ovi0yAhAFsAAAAC/tom-and-jerry-cartoon.gif",
            "https://media.tenor.com/AeFZ_gUU0YsAAAAC/gif.gif",
            "https://media.tenor.com/WB0owmgShUcAAAAC/the-god-of-highschool-goh.gif",
            "https://media.tenor.com/GMQE_GsGQGkAAAAd/the-god-of-high-school.gif",
            "https://media.tenor.com/E8LBekhMVy8AAAAd/itadori-yuji.gif",
            "https://media.tenor.com/mxYFOG9-ylkAAAAd/jujutsu-kaisen-anime.gif",
            "https://media.tenor.com/s1P3uAdLrrQAAAAC/fight-anime.gif",
            "https://media.tenor.com/JbdTmeTpEZEAAAAC/hoseokmaraj-stan-twitter.gif",
            "https://media.tenor.com/AiDJRKi1SwsAAAAd/99percent-of-kik-fight-cute.gif",
            "https://media.tenor.com/YuR7uAqxHPkAAAAd/fighting-anime.gif"
        ]
        embed=discord.Embed(title=f"{user.name} and {ctx.author.name} are fighting !",color = discord.Colour.purple())    
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)  

    @commands.command(aliases=["Judge","JUDGE",'judging','Judging'])
    async def judge(self,ctx,user:discord.Member=None):
        if user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        randomgifs = [
            "https://media.discordapp.net/attachments/949680123869814794/1047080460200722493/Things_you_should_never_to_do_in_Ireland_as_a_tourist.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1047080460590788609/Finger_Wag_GIF_-_Inauguration_CNN2017_Donald_Trump_Finger_Wag_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1047080460951486564/Nbc_Judging_You_GIF_by_Good_Girls_-_Find__Share_on_GIPHY.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1047080461521928242/Mark_Wahlberg_No_GIF_by_Daddys_Home_-_Find__Share_on_GIPHY.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1047080461916188692/clint_eastwood_gran_turino_gif.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1047080462297858088/Hoe_vaak_moet_je_je_haar_wassen_-_en_is_het_slecht_als_je_elke_dag_wast_.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1047080462654390282/Seventeen_Judge_GIF_-_Seventeen_Judge_Minghao_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1047080463006707752/37a2e9de-3063-4401-a8a4-c37c82695aac.gif" 
            ]
        
        embed=discord.Embed(title=f"{ctx.author.name} is judging {user.name} hard",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed) 

    @commands.command(aliases=["winking","winks"])
    async def wink(self,ctx,user:discord.Member=None):
        if user == None:
            embed=discord.Embed(title=f"{ctx.author.name} is winking",color = discord.Colour.purple())
        else:
            embed=discord.Embed(title=f"{ctx.author.name} is winking at {user.name}",color = discord.Colour.purple())    
        if user!=None and user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return 
        randomgifs = [
            "https://media.tenor.com/NqfVYEvKxTcAAAAC/mr-bean-wink-wink.gif",
            "https://media.tenor.com/FspCvtI5W54AAAAC/qoobee-wink-wink.gif",
            "https://media.tenor.com/q1yaXv-U8_4AAAAC/wink-flirty.gif",
            "https://media.tenor.com/LnbPYzKnp1MAAAAC/wink-eye.gif",
            "https://media.tenor.com/COm_PYzkLY4AAAAC/wink-wink-wink.gif",
            "https://media.tenor.com/SENM5TMtwIMAAAAC/anime-banished-from-the-heros-party.gif",
            "https://media.tenor.com/alFY5CG_x5wAAAAC/cat-cat-wink.gif",
            "https://media.tenor.com/tYJREL-BRcAAAAAC/dean-winchester-supernatural.gif",
            "https://media.tenor.com/dhpg1ANC_YoAAAAC/pikamee-wink.gif",
            "https://media.tenor.com/xqVLGvBsBagAAAAC/yeah-wink.gif",
            "https://media.tenor.com/lQLtWMRyI2IAAAAC/nakaru-rikka-rikka.gif",
            "https://media.tenor.com/KDAqyHrnSqAAAAAd/watame-wink-hololive.gif",
            "https://media.tenor.com/83KICXAA2DgAAAAC/himouto-umaru.gif",
            "https://media.tenor.com/mpFuM0d0ekQAAAAC/wink-oscar-mayer.gif",
            "https://media.tenor.com/6ZKE7QK8YzgAAAAC/dog-doge.gif",
            "https://media.tenor.com/_433fTxiAmYAAAAd/minagawa-mina.gif",
            "https://media.tenor.com/YSrNi73c0VAAAAAC/mowgli-mowgli-wink.gif",
            "https://media.tenor.com/h4UZrUdRi4IAAAAC/kokomi-kokomi-wink.gif",
            "https://media.tenor.com/650BkxB0094AAAAC/spongebob-squarepants-wink-wink.gif",
            "https://media.tenor.com/dNJP18aYrKUAAAAC/mime-mimes.gif",
            "https://media.tenor.com/LSKRA-5bqIEAAAAC/wink-winking.gif",
            "https://media.tenor.com/1859qBpNXr0AAAAd/mihoyo-genshin.gif",
            "https://media.tenor.com/V5ac9XkOf-wAAAAC/wink.gif",
            "https://media.tenor.com/QhyoQSgnN8YAAAAC/dog-wink.gif",
            "https://media.tenor.com/wrCss7-RUi0AAAAC/classy-wink-stay-classy.gif",
            "https://media.tenor.com/MhH3iDxh8lwAAAAC/bella-poarch-wink.gif",
            "https://media.tenor.com/S7ah9uq9qWkAAAAi/wink-hi.gif",
            "https://media.tenor.com/joY_eHVYPU4AAAAi/eneko-wink-arachne.gif",
            "https://media.tenor.com/i0Wd9klJFq8AAAAi/couple-cute.gif",
            "https://media.tenor.com/9NX3H1ptKYEAAAAi/machiko-rabbit.gif",
            "https://media.tenor.com/392Wg3agT9EAAAAi/meobeo-wink.gif",
            "https://media.tenor.com/oPhZRCMT5ukAAAAC/vi-wink.gif",
            "https://media.tenor.com/Nn2MJuuP06QAAAAC/pitzah-wink.gif",
            "https://media.tenor.com/ysi4igpTeV8AAAAC/pizza-steve-wink.gif",
            "https://media.tenor.com/DkT6AfUOKkIAAAAC/wink-taylor-swift.gif",
            "https://media.tenor.com/R9IK6u49rxMAAAAC/the-rock-wink.gif",
            "https://media.tenor.com/CC8imz8PKssAAAAC/gojo-satoru.gif",
            "https://media.tenor.com/eo-Tu1wwQg8AAAAC/baby-kitty-baby-felix.gif",
            "https://media.tenor.com/P6GVbSgbRSwAAAAC/winking-wink.gif",
            "https://media.tenor.com/dh3Ks6Da17EAAAAC/the-loud-house-luan-loud.gif",
            "https://media.tenor.com/vqsOVnolr4kAAAAC/ritsu-sakuma-ritsu.gif",
            "https://media.tenor.com/qGVr9VIt80sAAAAC/guffo-wink.gif",
            "https://media.tenor.com/nfLtNVUiYI0AAAAC/evacomics-kopi.gif",
            "https://media.tenor.com/mo0CJOXIxIYAAAAC/cat-cat-winking.gif",
            "https://media.tenor.com/yMakMVq6Z4sAAAAd/corgi-smile.gif",
            "https://media.tenor.com/jWHiKwSPwdEAAAAd/wink-got-it-dude.gif",
            "https://media.tenor.com/OWI_ai132b0AAAAC/wink-dog.gif",
            "https://media.tenor.com/4Htrx8dCwzoAAAAd/flirt-wink.gif",
            "https://media.tenor.com/s8IyfuaeV3sAAAAC/wink-wink-wink.gif",
            "https://media.tenor.com/QsCmMJ2JtMMAAAAC/wink-misaki-shokuhou.gif",
            "https://media.tenor.com/wwRcgvLAVH0AAAAC/tamako-market-anime-wink.gif",
            "https://media.tenor.com/XyenxWhdZb0AAAAC/wink-winking.gif",
            "https://media.tenor.com/YW7ZIUrBHo4AAAAC/anime-anime-girl.gif",
            "https://media.tenor.com/ulcw93lYQJ8AAAAC/xmr-monero.gif"

        ]
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)                

    
async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(threaten(bot))       
    print("threaten, fight, judge, wink is loaded")    
       
        
   