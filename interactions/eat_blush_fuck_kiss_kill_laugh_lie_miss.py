import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import CommandTree
import requests
import discord.ui
from discord.ui import Button,View
import random

class eat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["Eating","eat","Eat"])
    async def eating(self,ctx):
        randomgifs = [
            "https://media.discordapp.net/attachments/1045618240900050954/1046361143976935454/b9a29258-8eb8-4ad4-81a1-ab085059d8af.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046361145553997874/Comendopipoca_GIF_-_Comendopipoca_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046361146485133362/Happy_Spongebob_Squarepants_GIF_-_Find__Share_on_GIPHY.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046361146971668540/Smash_Bros_Eating_GIF_-_Smash_Bros_Eating_Cute_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046361147378520114/Milk_And_Mocha_Gnam_GIF_-_Milk_And_Mocha_Gnam_Omnom_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046361214881632306/eating-food.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046361224247525426/7e7a012b54676d29a26f83e63f860178_w200.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046361236574576721/eating-kirby.gif",
            "https://media.tenor.com/c4t_zeBjjKoAAAAd/lets-eat-pizza.gif",
            "https://media.tenor.com/k9Qi_PrDtYwAAAAC/yum-eating.gif",
            "https://media.tenor.com/zc17cWljUR4AAAAd/sushichaeng-reaction.gif",
            "https://media.tenor.com/LDq6TYyHL6kAAAAC/miss-kobayashi.gif",
            "https://media.tenor.com/RMBrWjoO5dUAAAAd/cat-eating-fast.gif",
            "https://media.tenor.com/fWELEHRuVAUAAAAd/pingu-angry-dad-pingu-eating-dinner.gif",
            "https://media.tenor.com/VHU3Ii0DYZwAAAAC/eating.gif",
            "https://media.tenor.com/8skDEfCnvZ8AAAAd/happy-dance-eat.gif",
            "https://media.tenor.com/zkmre31oApEAAAAC/kirby-eat.gif",
            "https://media.tenor.com/-0Ly8VUuog8AAAAC/breakfast-hungry.gif",
            "https://media.tenor.com/BZJLoYs2TwEAAAAi/usagyuuun-usagyuuun-sticker.gif",
            "https://media.tenor.com/7ws8DGC0knsAAAAi/capoo-blue.gif",
            "https://media.tenor.com/9lxUwZra_sgAAAAi/panda-cartoon.gif",
            "https://media.tenor.com/JHjSWtXxYzYAAAAi/food.gif",
            "https://media.tenor.com/NtUfujVgkpkAAAAi/hungry-eating.gif",
            "https://media.tenor.com/aqYeaIooiI0AAAAi/eating-crab-eric-cartman.gif",
            "https://media.tenor.com/kkC1Cu4Qdj0AAAAC/choco-choco.gif",
            "https://media.tenor.com/4glKvahciNgAAAAd/big-ed-thisisbiged.gif",
            "https://media.tenor.com/NblSZhc__XYAAAAd/pso2-rappy.gif",
            "https://media.tenor.com/eWWh5gw8IkEAAAAC/wow-wow-wubbzy-wubbzy.gif",
            "https://media.tenor.com/VeluGVdUpFMAAAAd/ima-eat-dinner-time.gif",
            "https://media.tenor.com/kI_l6rj_VsQAAAAC/eating.gif",
            "https://media.tenor.com/VTwG3eL3eL8AAAAC/mochi-nyao.gif",
            "https://media.tenor.com/WZEe1IgycUYAAAAd/vtube.gif",
            "https://media.tenor.com/gQjxza31pxIAAAAd/my-dress-up-darling-anime-eat.gif",
            "https://media.tenor.com/AlnCyj8wubIAAAAC/unhealthy-eating.gif",
            "https://media.tenor.com/9A_t_PCgJR8AAAAd/he-hongry-dog.gif"
        ]
        embed=discord.Embed(title=f"{ctx.author.name} is eating! Yummy food",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed) 

    @commands.command(aliases=["blushes","blushing","Blush"])
    async def blush(self,ctx,user:discord.Member=None):
        if user == None:
            embed=discord.Embed(title=f"{ctx.author.name} is blushing",color = discord.Colour.purple())
        else:
            embed=discord.Embed(title=f"{user.name} made {ctx.author.name} blush",color = discord.Colour.purple())    
        if user!=None and user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return 
        randomgifs = [
            "https://media.tenor.com/hC6WrRkokJsAAAAd/tom-and-jerry-tom.gif",
            "https://media.tenor.com/3g-vM1sZ2g4AAAAC/blush.gif",
            "https://media.tenor.com/4vyIazBzLVoAAAAC/blushes-deeply-blushing-intensifies.gif",
            "https://media.tenor.com/1IeHa_QMLdwAAAAC/sailor-moon-extremely.gif",
            "https://media.tenor.com/9ut2GHmvO0cAAAAd/laugh.gif",
            "https://media.tenor.com/efy3bKjLl3QAAAAC/shy-aww.gif",
            "https://media.tenor.com/DuFLd7RrrygAAAAC/sonrojado.gif",
            "https://media.tenor.com/57ykwUGXE08AAAAC/blush-shinji.gif",
            "https://media.tenor.com/PXWh80tfKXIAAAAC/cute-fingers-fixed-cat.gif",
            "https://media.tenor.com/lsT6PTKnnF8AAAAC/shy-please.gif",
            "https://media.tenor.com/tn4LOK2uvroAAAAC/tom-and.gif",
            "https://media.tenor.com/G2yZJgS0RjIAAAAC/shame-blushing-girl.gif",
            "https://media.tenor.com/CEkiOjpsylwAAAAd/kitagawa-kitagawa-marin.gif",
            "https://media.tenor.com/PGXshKPAUh4AAAAC/my-dress-up-darling-anime-love.gif",
            "https://media.tenor.com/LpIXLQcbY2kAAAAC/marin-kitagawa.gif",
            "https://media.tenor.com/x_9-mUKTCIQAAAAd/sono-bisque-doll-my-dress-up-darling.gif",
            "https://media.tenor.com/yKtYfA0mizYAAAAC/my-dress-up-darling-anime-blush.gif",
            "https://media.tenor.com/gu0EZJfpXP8AAAAC/marin-kitagawa-my-dress-up-darling.gif",
            "https://media.tenor.com/Y0v7dZFqClkAAAAC/thor-chris-hemsworth.gif",
            "https://media.tenor.com/VRUQ_YhZZIAAAAAC/anime-blush.gif",
            "https://media.tenor.com/vjpKNHGxMs0AAAAC/cute-shy.gif",
            "https://media.tenor.com/TfM5W6MtLPkAAAAC/shinchan.gif",
            "https://media.tenor.com/9avuvzHbgv4AAAAd/sumi-sakurasawa-rent-a-girlfriend.gif",
            "https://media.tenor.com/6Omqf_97IbAAAAAC/kanojo-okarishimasu-sumi.gif",
            "https://media.tenor.com/7KaaBzVxAdAAAAAC/rpg-fudousan-anime-blush.gif",
            "https://media.tenor.com/qYS0n4QWxd4AAAAC/blush-anime.gif",
            "https://media.tenor.com/BgBq7npMTusAAAAi/stitch-blush.gif",
            "https://media.tenor.com/1Aaso_pJcsIAAAAi/qoobee-blushing.gif",
            "https://media.tenor.com/9f3piKJ75w4AAAAi/shy-blush.gif",
            "https://media.tenor.com/GKQNAbb_F84AAAAi/uwu-but.gif",
            "https://media.tenor.com/dS8xjfhJUr4AAAAi/blush-blissful.gif",
            "https://media.tenor.com/48lXDrWmY94AAAAC/blush.gif",
            "https://media.tenor.com/Y6KoYUuYKWAAAAAd/yor-forger-yor.gif"
           ]
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)  

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

    @commands.command(aliases=["Kill","KILL",'killing'])
    async def kill(self,ctx,user:discord.Member=None):
        if user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        randomgifs = [
            "https://media.tenor.com/NbBCakbfZnkAAAAC/die-kill.gif",
            "https://media.tenor.com/PuHWmlv-KTsAAAAC/die.gif",
            "https://media.tenor.com/8TfmfQv5lqgAAAAd/doggo-killing-cat.gif",
            "https://media.tenor.com/vHW4bc5x9IwAAAAC/playing-bully.gif",
            "https://media.tenor.com/1dtHuFICZF4AAAAC/kill-smack.gif",
            "https://media.tenor.com/5Pdr2eFmGG4AAAAC/kill-me.gif",
            "https://media.tenor.com/u1YGw2-Ac0kAAAAC/kill-bill.gif",
            "https://media.tenor.com/ZKdcSexdkY0AAAAC/somebody-gonna-die-today-kill.gif",
            "https://media.tenor.com/50egAhARCjEAAAAC/cat-shooting.gif",
            "https://media.tenor.com/50egAhARCjEAAAAC/cat-shooting.gif",
            "https://media.tenor.com/HisBdTOnhx4AAAAC/activating-instand-kill-spiderman-instant-kill.gif",
            "https://media.tenor.com/PDEnDgVjYEAAAAAC/mob-psycho.gif",
            "https://media.tenor.com/SjVdRr-PZHAAAAAC/bmo-adventure-time.gif",
            "https://media.tenor.com/WOpPM1NdBE4AAAAi/agung.gif",
            "https://media.tenor.com/qHioKThCl1AAAAAi/love.gif",
            "https://media.tenor.com/tGZQisW1c2kAAAAi/bonk.gif",
            "https://media.tenor.com/4eYmBHh-118AAAAi/knife-ghostface.gif",
            "https://media.tenor.com/DIq2K_xXpTgAAAAi/chainsaw-evil.gif",
            "https://media.tenor.com/oSSU2r9NWrMAAAAC/freddie-chainsaw.gif",
            "https://media.tenor.com/bm-RAmg9Q-wAAAAi/dream-robot.gif",
            "https://media.tenor.com/X2rzi5IdJ40AAAAi/kirby-kirbyknife.gif",
            "https://media.tenor.com/sUrVm6QQG6AAAAAi/white-angry.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046847843597549608/l55gmjfacebook.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046847850849513543/74c150a96ce7654c2131c7095dbfcc52.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046847852615303178/kill-me.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046847859510759494/kill-you-kill.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046847860165066833/giphy_6.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046847872529874944/kill-stab.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046848106035154964/cc87656cf72979fb8ee01c3eebc5cdff.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046848112565694534/among-us-kill-icegif.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046848114419581008/duck-mad.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046848121952542781/69649.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046848137723117618/804e237839129b79dd956eb9c2ec1803.gif"
            ]
        
        embed=discord.Embed(title=f"{ctx.author.name} killed {user.name} ! They definitely won't be able to type again",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)      

    @commands.command(aliases=["laughing","Laugh","Laughing"])
    async def laugh(self,ctx,user:discord.Member=None):
        if user == None:
            embed=discord.Embed(title=f"{ctx.author.name} is laughing",color = discord.Colour.purple())
        else:
            embed=discord.Embed(title=f"{ctx.author.name} is laughing at {user.name}",color = discord.Colour.purple())    
        if user!=None and user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return 
        randomgifs = [
            "https://media.tenor.com/4yDNX1P_QboAAAAC/jerry-laugh.gif",
            "https://media.tenor.com/Vh07Ax3q4voAAAAd/kid-laugh.gif",
            "https://media.tenor.com/aRyiCpjkNIUAAAAC/funny-squirrel.gif",
            "https://media.tenor.com/Rvy1so6nirQAAAAC/minions-laughing-rofl.gif",
            "https://media.tenor.com/5FTx6fGF5HUAAAAC/funny-donald-duck.gif",
            "https://media.tenor.com/83qR14S3hoQAAAAC/elmo-laughing.gif",
            "https://media.tenor.com/Y_5OAa2LQUAAAAAC/laughing-funny.gif",
            "https://media.tenor.com/KZSCnVzDgKcAAAAd/controlling-laugh-laughing.gif",
            "https://media.tenor.com/hNN574xBqjwAAAAC/holding-back-laughter-laugh.gif",
            "https://media.tenor.com/JCYLRqm7oyIAAAAd/trying-not-to-laugh-zoom-in.gif",
            "https://media.tenor.com/Bz5HuDTf7BgAAAAC/holding-laugh-trying-not-to-laugh.gif",
            "https://media.tenor.com/sWDtl3qODfgAAAAd/laughing-hysterically-cant-stop-laughing.gif",
            "https://media.tenor.com/3MBb9OcZK-IAAAAd/kitty-forman-debra-jo-rupp.gif",
            "https://media.tenor.com/SnxaOxGekxAAAAAC/johnny-test-evil-laugh.gif",
            "https://media.tenor.com/24aiNbky2tsAAAAd/laughing-phat-tuesdays.gif",
            "https://media.tenor.com/92P0V36zt0cAAAAC/jimbei-jinbe.gif",
            "https://media.tenor.com/Gz_DmBbfxP4AAAAd/drake-giggling-drake-laughing.gif",
            "https://media.tenor.com/NGCiTD9yh6EAAAAd/josuke-laugh.gif",
            "https://media.tenor.com/7rmzWTmbfkgAAAAd/kek-cat-kek.gif",
            "https://media.tenor.com/RqKEPJqkI0wAAAAC/death-note-light-yagami.gif",
            "https://media.tenor.com/lEcc1EHQ900AAAAd/laughing-dying.gif",
            "https://media.tenor.com/QdB7f-2y4ewAAAAC/takumi-laugh.gif",
            "https://media.tenor.com/0AnI7-n7wIMAAAAC/sml-junior.gif",
            "https://media.tenor.com/RWfoyoLrN1oAAAAC/johnny-test-bling-bling-boy.gif",
            "https://media.tenor.com/agrQMQjQTzgAAAAd/talking-ben-laugh.gif",
            "https://media.tenor.com/rDNhehCwpJwAAAAC/the-chazz-laughing.gif",
            "https://media.tenor.com/BSAEGR5ftsUAAAAC/satania-gabriel.gif",
            "https://media.tenor.com/XQxOkKXFG7oAAAAC/satania-laugh.gif",
            "https://media.tenor.com/-K7HcKA-_KYAAAAC/the-loud-house-luan-loud.gif",
            "https://media.tenor.com/Qn8Zpe3199MAAAAC/squidward-lol.gif",
            "https://media.tenor.com/OomP4DS2RF4AAAAC/reasonsimbroke-batman-laugh.gif",
            "https://media.tenor.com/jP1dnT_EWj0AAAAC/enel-eneru.gif",
            "https://media.tenor.com/iWVjQrBsyOEAAAAC/obito-laugh.gif",
            "https://media.tenor.com/aiFznJ8Xni8AAAAC/mahito-sukuna.gif",
            "https://media.tenor.com/f29kmmR0d9YAAAAC/happy-laugh.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046361695561453688/Happy_Cracking_Up_GIF_-_Find__Share_on_GIPHY.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046361695859261490/Minions_Laugh_GIF_-_Minions_Despicable_Me_Laugh_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046361696123506779/Moms_Mabley__The_Dirty_Granny_of_Stand_Up.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046361699881586718/Happy_Laugh_Sticker_-_Happy_Laugh_Funny_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046361700242313286/Celebrity__Entertainment___Chris_Evans_Does_This_1_Thing_Almost_Every_Time_He_Laughs_and_Its_Freakin_Adorable.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046361700598812692/Cracking_Up_Reaction_GIF_-_Find__Share_on_GIPHY.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046361700967923803/33_Random_Pics_To_Amuse_and_Entertain.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046361701295083540/When_someone_suggests_you_should_maybe_give_up_coffee_for_a_week_.gif"
        ]
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)  

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

    @commands.command(aliases=["Missing","miss","Miss"])
    async def missing(self,ctx,user:discord.Member=None):
        if user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        randomgifs = [
            "https://media.tenor.com/dINQhpsCmF0AAAAC/texting-good.gif",
            "https://media.tenor.com/1hXu9gCR3yYAAAAC/missing-you.gif",
            "https://media.tenor.com/ehZ0H83LP60AAAAC/miss-you.gif",
            "https://media.tenor.com/k1Y29IQqH7wAAAAC/miss-you.gif",
            "https://media.tenor.com/39sOrl_JAjQAAAAC/miss-you-pikachu.gif",
            "https://media.tenor.com/LfWRMoxQbUkAAAAC/patrick-star-miss-you.gif",
            "https://media.tenor.com/F5AczKXVI5oAAAAC/regular-show-rigby.gif",
            "https://media.tenor.com/jJU0-lPXaAwAAAAC/miss-you-i-miss-you.gif",
            "https://media.tenor.com/vbKNNH0cwqQAAAAC/miss-you.gif",
            "https://media.tenor.com/q-3U-fXc-_cAAAAC/miss-you.gif",
            "https://media.tenor.com/PebbchgGFKAAAAAC/i-miss-you-too-love-you.gif",
            "https://media.tenor.com/BIBv-hwgRmUAAAAC/miss-you-miss-you-more.gif",
            "https://media.tenor.com/CB_jxPMbUjwAAAAC/chick-pio.gif",
            "https://media.tenor.com/NugftrLvkVIAAAAC/miss-you-missing-you.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1045693438982619146/miss-you-shy-bear-wgvvsi8epdvui25t.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1045693439276236810/b5395bd842e048cd00cc021b50c37ba6.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1045693439574024282/missing-you-badly-waiting.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046155561265287188/7fd9ff3c81c5ea8cf317c05794a22363.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046155628684525698/dog-triste.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046155851494326372/i-miss-you-so-much-i-miss-you.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046155978267164692/SjOp.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046156399069102090/i-miss-you-bear-crying-d9eflc3t9immbccm.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047173771200577637/love-you_1.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047173775235489802/sanrio-hello-kitty.gif0",
            "https://media.discordapp.net/attachments/949680123479728146/1047173778838409226/hello-kitty.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047173782168670279/goodnight-miss.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047173918257053797/miss.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047173924800167986/missing-you.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047173927128027156/miss-you.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047174320750874704/cat-i-love-you.gif?width=424&height=606",
            "https://media.discordapp.net/attachments/949680123479728146/1047174325393948732/love-cute.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047174335372218388/love-languages-miss-you.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047174609700659321/i-miss-you.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047174611323846766/miss-you-pikachu.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047174612007530546/missing.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047174617703403660/dino-i-miss-you.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047174629762023494/i-miss-you-anya.gif?width=606&height=606",
            "https://media.discordapp.net/attachments/949680123479728146/1047174904262443098/rascal-miss-you.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047174905260675113/spongebob-patrick-star.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047174906309255188/fatcatzcouple-fluffy.gif"
        ]
        embed=discord.Embed(title=f"{ctx.author.name} is missing {user.name}",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)          

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(eat(bot))       
    print("eat, blush, fuck, kiss, kill, laugh, lie, miss is loaded")    
       
        
   