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

    @commands.command(aliases=["Pat,'patting"])
    async def pat(self,ctx,user:discord.Member=None):
        if user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        randomgifs = [
            "https://media.discordapp.net/attachments/1045618243013984296/1046400910332530698/mala-mishra-jha-pat-head.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046400915663503440/giphy.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046400927076188190/678116d6e7fdbb5275c2d1ca8c938099.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046401319113601125/giphy_1.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046401320745177139/cute-anime-umaru-head-pat-rabcmvfkpeuteckt.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046401334095659068/bunny-cute.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046401338688409630/cd77c5cab311d773ac3846079e483d67_w200.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046401349014802552/pat-cat.gif"
        ]
        embed=discord.Embed(title=f"{ctx.author.name} is patting {user.name} because they are cute!",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)     

    @commands.command(aliases=["PillowFight","Pillowfight","pf","PF",'pillowf','pfight'])
    async def pillowfight(self,ctx,user:discord.Member=None):
        if user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        randomgifs = [
            "https://media.discordapp.net/attachments/949680123869814794/1046846733818269836/grandparents-day-insomnia.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046846742060081332/pow-pillow-fight.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046846743398072400/edac8fd3339d460f5d609cb738c4d1c5.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046846745943998564/OptimisticPlaintiveAidi-size_restricted.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046846752013164584/733898f1a9d33a3db97fcebbf49dbb82.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046846813648465990/giphy_5.gif"
            ]
        
        embed=discord.Embed(title=f"{ctx.author.name} and {user.name} are pillowfighting !",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)  

    @commands.command(aliases=["pinching",'Pinch'])
    async def pinch(self,ctx,user:discord.Member=None):
        if user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        randomgifs = [
            "https://media.discordapp.net/attachments/993633626719780924/1046366440225247252/Milk_And_Mocha_Cheek_GIF_-_Milk_And_Mocha_Cheek_Chubby_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/993633626719780924/1046366440757940234/Little_piece_of_my_life.gif",
            "https://media.discordapp.net/attachments/993633626719780924/1046366441127034931/Squishy_Squishy_GIF_-_Squishy_Kitty_Cat_Cheeks_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/993633626719780924/1046366441424818186/Chubby_Cheeks_Pinch_GIF_-_Chubby_Cheeks_Pinch_Adorable_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/993633626719780924/1046366442049781870/Pull_Pinch_GIF_-_Pull_Pinch_Funny_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/993633626719780924/1046366442557280267/Pull_Pinch_Sticker_-_Pull_Pinch_Mochi_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/993633626719780924/1046366441764573254/Chicken_Bro_Chicken_GIF_-_Chicken_Bro_Chicken_Pinch_-_Discover__Share_GIFs.gif"
        ]
        embed=discord.Embed(title=f"{ctx.author.name} is pinching {user.name} !!",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)      

    @commands.command(aliases=["praying","prays"])
    async def pray(self,ctx,user:discord.Member=None):
        if user == None:
            embed=discord.Embed(title=f"{ctx.author.name} is praying",color = discord.Colour.purple())
        else:
            embed=discord.Embed(title=f"{ctx.author.name} is praying for {user.name}",color = discord.Colour.purple())    
        if user!=None and user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return 
        randomgifs = [
            "https://media.tenor.com/KTp9sgkLjzoAAAAC/jerry-the-mouse-tom-and-jerry.gif",
            "https://media.tenor.com/4IckGuTqWeYAAAAC/spongebob-squarepants-begging.gif",
            "https://media.tenor.com/TX04b7YAOl8AAAAd/please-please-god.gif",
            "https://media.tenor.com/DmOiqA-m5nAAAAAC/mushoku-tensei-rudeus.gif",
            "https://media.tenor.com/Yt5E0AQEPX8AAAAd/shirley-temple-praying.gif",
            "https://media.tenor.com/rwGUhTSCrL8AAAAd/takagi-san-takagi.gif",
            "https://media.tenor.com/qz1oO99DcK0AAAAd/wendy-praying-son-seungwan-praying.gif",
            "https://media.tenor.com/0FRabKRmgjAAAAAd/seungwan-youngstreet-son-seungwan-praying.gif",
            "https://media.tenor.com/GUV6HplSs7MAAAAC/loeya-pray.gif",
            "https://media.tenor.com/q--Ww86G0MoAAAAd/genshin-genshin-impact.gif",
            "https://media.tenor.com/g15Z-NkoKjsAAAAC/praying-prayer.gif",
            "https://media.tenor.com/K20UM-dZC4oAAAAd/lets-pray-pray.gif",
            "https://media.tenor.com/iZ6u-jpcKDIAAAAC/marie-mai-mariemai-news.gif",
            "https://media.tenor.com/tMtfOLuBZDUAAAAC/praying-hands-gucci-mane.gif",
            "https://media.tenor.com/1JJngkJOI3IAAAAC/hangouts-pray.gif",
            "https://media.tenor.com/js1RCj9wG1cAAAAC/ic0niclisa-praying.gif",
            "https://media.tenor.com/XsW48MrsCpwAAAAd/praying-prayers.gif",
            "https://media.tenor.com/WhgPx2O1I-QAAAAd/pray-praying.gif",
            "https://media.tenor.com/CyK_xV5Q3lkAAAAC/jiminjimin-jimin.gif",
            "https://media.tenor.com/YEwRtiurLiwAAAAd/yurina-yurina-meme.gif",
            "https://media.tenor.com/uI-iiI3Wnh8AAAAC/kejsi-pray.gif",
            "https://media.tenor.com/14pcWHa4-S4AAAAC/ryujin-cat.gif",
            "https://media.tenor.com/_E3TnFTI8ZkAAAAC/porfa-porfa-remix.gif"
           
        ]
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)   

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
    await bot.add_cog(hug(bot))       
    print("hug, boop, pat, pf, pinch, pray, salute is loaded")    
       
    
    