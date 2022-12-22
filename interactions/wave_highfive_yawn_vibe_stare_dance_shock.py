import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import CommandTree
import requests
import discord.ui
from discord.ui import Button,View
import random

class wave(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=["waving","Wave","Waving"])
    async def wave(self,ctx,user:discord.Member=None):
        if user == None:
            embed=discord.Embed(title=f"{ctx.author.name} is waving",color = discord.Colour.purple())
        else:
            embed=discord.Embed(title=f"{ctx.author.name} waves at {user.name}",color = discord.Colour.purple())    
        if user!=None and user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return 
        randomgifs = [
            "https://media.tenor.com/tPumyOcid1cAAAAC/pepe-wink-wink.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046891679770230835/monkey-waving.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046891680093188298/kung-fu-panda-po-waving-ub3ic92611g1yvxk.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046891680407756821/d7i06j2-209054b9-be1e-46b0-aa61-ffbe4dc1ebda.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046891681255006328/hello-there-waving.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046891681640890398/200w.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046891682018369606/garfield-waving.gif"   
        ]
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)  

    @commands.command(aliases=["hf","Hf","highfiving",'highf','hfive'])
    async def highfive(self,ctx,user:discord.Member=None):
        if user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        randomgifs=[
            "https://media.tenor.com/KX6_14fSo0YAAAAi/akirambow-smile-person.gif",
            "https://media.tenor.com/TRSYCx4GnGoAAAAi/budding-pop-friends.gif",
            "https://media.tenor.com/D4geDkAW9jgAAAAi/cat-paw.gif",
            "https://media.tenor.com/zRQPetULV5kAAAAi/rascal-high-five.gif",
            "https://media.tenor.com/PDom-Pt-DYAAAAAi/high-five-yay.gif",
            "https://media.tenor.com/r322btJKK7EAAAAC/high-five-amy-santiago.gif",
            "https://media.tenor.com/qy_WcGdRzfgAAAAC/xluna-high-five.gif",
            "https://media.tenor.com/OR2z4Pkg45kAAAAC/high-five.gif",
            "https://media.tenor.com/7skQ3peC1mEAAAAC/high-five.gif",
            "https://media.tenor.com/5uzrkK8Pps0AAAAC/love-anniversary.gif",
            "https://media.tenor.com/uHSWiu1Jk2MAAAAC/base-high-five.gif",
            "https://media.tenor.com/EcTTHD9dnMUAAAAC/evan-and-katelyn-extreme-high-five.gif",
            "https://media.tenor.com/UtMb32NBztEAAAAC/neil-patrick-harris-high-five.gif",
            "https://media.tenor.com/gI49p3ZeN2AAAAAi/cool-blue-high-five.gif",
            "https://media.tenor.com/x_Z1QD8mQecAAAAi/shi-ngao.gif",
            "https://media.tenor.com/XlAB-tE7tMYAAAAi/hi5-high-five.gif",
            "https://media.tenor.com/7nDIBPMdjSoAAAAC/gts-good-time-society.gif",
            "https://media.tenor.com/fmDOIOVxfVoAAAAC/seth-meyers-late-night-seth.gif",
            "https://media.tenor.com/mpCnVpX0xIYAAAAC/high-five-spongebob.gif",
            "https://media.tenor.com/_KGWqG2EBdIAAAAC/anime-girls.gif",
            "https://media.tenor.com/JsCGv-NM-w0AAAAC/cat-high.gif",
            "https://media.tenor.com/K4dK6z75fQUAAAAC/high-five-slow-motion.gif",
            "https://media.tenor.com/BD-trsxTZPoAAAAC/barney-stinson-high-five.gif",
            "https://media.tenor.com/9vnJU85-7GwAAAAC/yeah-high.gif",
            "https://media.tenor.com/RXYUxZdBaUcAAAAd/stukk-high-five.gif",
            "https://media.tenor.com/Rs5Gyiw0OysAAAAC/high-five-high-five-cat.gif",
            "https://media.tenor.com/2NgSVoaOwtMAAAAC/high-five.gif",
            "https://media.tenor.com/MDTYbqilAxgAAAAC/ogvhs-high-five.gif",
            "https://media.tenor.com/sQzOqyKfGv4AAAAd/pokemon-scorbunny.gif",
            "https://media.tenor.com/zuGJiqsnkPIAAAAC/eevee-pikachu.gif",
            "https://media.tenor.com/RusIdB6WS-IAAAAC/cat-high-five.gif",
            "https://media.tenor.com/cfBsYK73HLkAAAAC/puppy-dog.gif",
            "https://media.tenor.com/umyVoo90A_sAAAAd/high-five-dog-high-five-xiteb.gif",
            "https://media.tenor.com/r0sUDFfn6o0AAAAC/high-five-awesome.gif",
            "https://media.tenor.com/EFVbyCW4ITEAAAAd/dogs-high-five.gif",
            "https://media.tenor.com/ZVyre2PZC4EAAAAd/dog-high-five.gif",
            "https://media.tenor.com/MZuZ9C_3_ZkAAAAC/dog-high-five.gif",
            "https://media.tenor.com/SUQuOYlPZU4AAAAd/high-five-the-pack.gif",
            "https://media.tenor.com/8hFGXTck6usAAAAC/pawfive-dogfive.gif",
            "https://media.tenor.com/JrV7r-u405wAAAAd/hanzo-husky-hanzo-the-husky.gif",
            "https://media.tenor.com/-Xe4wBdy7f4AAAAC/paws-cat.gif",
            "https://media.tenor.com/qVun4U93OiYAAAAC/meomoc-high-five.gif",
            "https://media.tenor.com/nUPVAKITU0YAAAAd/high-five-cat.gif",
            "https://media.tenor.com/a2GGLtACrqsAAAAC/bakabaka7-adventure-time.gif",
            "https://media.tenor.com/CQn2tIIADEcAAAAC/monkey-high-five.gif"
        ]
        embed=discord.Embed(title=f"{ctx.author.name} is high fiving {user.name} !",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)   

    @commands.command(aliases=["yawning","yawns"])
    async def yawn(self,ctx,user:discord.Member=None):
        if user == None:
            embed=discord.Embed(title=f"{ctx.author.name} is yawning ",color = discord.Colour.purple())
        else:
            embed=discord.Embed(title=f"{ctx.author.name} is yawning because of {user.name}",color = discord.Colour.purple())    
        if user!=None and user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return 
        randomgifs = [
            "https://media.tenor.com/S96iCeYOWCcAAAAd/yawngirl-yawnkid.gif",
            "https://media.tenor.com/XVRTqgVzAQQAAAAC/yawn-yawning.gif",
            "https://media.tenor.com/HMhYjZY3Oa0AAAAd/bugs-bunny-yawn.gif",
            "https://media.tenor.com/oNaCRbvHu3oAAAAd/johnny-english-rowan-atkinson.gif",
            "https://media.tenor.com/zYw6FpUqW7MAAAAd/monkey-yawn.gif",
            "https://media.tenor.com/hclnFXnLhQ0AAAAC/pikachu-yawn.gif",
            "https://media.tenor.com/LoOKUaCO-04AAAAC/yawn-tom-and-jerry.gif",
            "https://media.tenor.com/GUGZujRyUXYAAAAC/boring-yawn.gif",
            "https://media.tenor.com/6L5o7Ov-__sAAAAC/kitaro-yawn.gif",
            "https://media.tenor.com/4hZZgLvA7W0AAAAd/cat-yawn.gif",
            "https://media.tenor.com/40263d2eyREAAAAd/cat-waking-up.gif",
            "https://media.tenor.com/2Dzbry2XP_sAAAAd/cat-meow.gif",
            "https://media.tenor.com/TEWbYOiUSiEAAAAd/time-for-bed-bedtime.gif",
            "https://media.tenor.com/TV6ckPX9EcAAAAAd/cute-cat-yawning.gif",
            "https://media.tenor.com/OgdDRulZx-UAAAAd/wembley-yawn.gif",
            "https://media.tenor.com/iRAIQjbzYOAAAAAd/otter-yawn.gif",
            "https://media.tenor.com/32f48oSEHMgAAAAC/sleepy-anime.gif",
            "https://media.tenor.com/8KkpLp3zkQwAAAAd/yawn-yawning.gif",
            "https://media.tenor.com/OgdDRulZx-UAAAAd/wembley-yawn.gif"
           ]
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)  

    @commands.command(aliases=["vibing","Vibe","Vibing"])
    async def vibe(self,ctx,user:discord.Member=None):
        if user == None:
            embed=discord.Embed(title=f"{ctx.author.name} is vibing",color = discord.Colour.purple())
        else:
            embed=discord.Embed(title=f"{user.name} and {ctx.author.name} are vibing",color = discord.Colour.purple())    
        if user!=None and user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return 
        randomgifs = [
           "https://media.discordapp.net/attachments/949680123869814794/1046845051109658684/vibe-rabbit.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046845066347548723/teo-cat.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046845070235664465/tumblr_7d502f156e5b5458e8d05495f5936e44_008adab0_500.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046845075684073492/giphy_4.gif",
            "https://media.discordapp.net/attachments/1033808352133783595/1047090652002930758/adventure-time-jake.gif"
        ]
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)  

    @commands.command(aliases=["staring","stares"])
    async def stare(self,ctx,user:discord.Member=None):
        if user == None:
            embed=discord.Embed(title=f"{ctx.author.name} is staring",color = discord.Colour.purple())
        else:
            embed=discord.Embed(title=f"{ctx.author.name} is staring at {user.name}",color = discord.Colour.purple())    
        if user!=None and user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return 
        randomgifs = [
            "https://media.tenor.com/OVUDwIM8mBkAAAAd/cat-cat-stare.gif",
            "https://media.tenor.com/bN2IkZ5vzxIAAAAd/byuntear-meme.gif",
            "https://media.tenor.com/UhzFGLgrEWMAAAAC/staring-cat.gif",
            "https://media.tenor.com/DC7Wfck9t1oAAAAd/elmo-stare.gif",
            "https://media.tenor.com/Lp8_Goqa9LwAAAAd/cat-staring.gif",
            "https://media.tenor.com/6Yh6ZMnx1WcAAAAC/encanto-mirabel-madrigal.gif",
            "https://media.tenor.com/syRQ7NZHxR0AAAAd/cat-cats.gif",
            "https://media.tenor.com/AXNcrOrmW-gAAAAd/judging-stare.gif",
            "https://media.tenor.com/1SDNH_1wEkgAAAAC/judging-staring.gif",
            "https://media.tenor.com/zwd6Pu_S4_8AAAAC/wtf-judging.gif",
            "https://media.tenor.com/kTdUCcxyZEcAAAAC/judging.gif",
            "https://media.tenor.com/sXS_6sev18sAAAAd/staring-black-man-staring.gif",
            "https://media.tenor.com/v_IqC1wqppcAAAAC/death.gif",
            "https://media.tenor.com/He1TTQAiSysAAAAC/kermit-death-stare.gif",
            "https://media.tenor.com/tMxD2LYCBI0AAAAd/cats-stare-stare.gif",
            "https://media.tenor.com/b5neCS9mBAoAAAAi/what-huh.gif",
            "https://media.tenor.com/k_tMmWqpBKAAAAAi/goober-cat-stare.gif",
            "https://media.tenor.com/afghdfq3VQMAAAAi/mehhh-chick.gif",
            "https://media.tenor.com/ImGGRKpI4nwAAAAi/catstare.gif",
            "https://media.tenor.com/lZeNItuNm08AAAAd/cat-stare.gif",
            "https://media.tenor.com/kTRfSNaThpcAAAAi/intense-stare-crabby-crab.gif",
            "https://media.tenor.com/NsrW-lM8hM0AAAAC/favorite-person.gif",
            "https://media.tenor.com/RbqwVF-lzLkAAAAC/sonic-x-knuckles.gif",
            "https://media.tenor.com/rkvlaOAyM9cAAAAd/what-staring.gif",
            "https://media.tenor.com/nJXREhSyJ5gAAAAC/wait-what.gif",
            "https://media.tenor.com/UUTVUk3Ghr4AAAAC/mario-kart-luigi.gif",
            "https://media.tenor.com/fJ_WOY5K1HYAAAAd/cartoon-cartoon-stare.gif",
            "https://media.tenor.com/UambViphH-gAAAAd/dog-dog-stare.gif",
            "https://media.tenor.com/Nfct9RreQfUAAAAd/dog-meme.gif",
            "https://media.tenor.com/jOX-QDKZZOoAAAAd/cat-stare.gif",
            "https://media.tenor.com/7X513x6912oAAAAC/staring-staring-respectfully.gif",
            "https://media.tenor.com/3mvt0crJS6kAAAAC/intense-stare-crabby-crab.gif",
            "https://media.tenor.com/8FuCbwNQSqsAAAAC/peepo-stare.gif",
            "https://media.tenor.com/axum-jbte_sAAAAC/old-man-cat.gif",
            "https://media.tenor.com/MdU23gMRK10AAAAC/cosette-schneider-destiny.gif",
            "https://media.tenor.com/BHgQEy2AsXkAAAAC/hamster-camera.gif",
            "https://media.tenor.com/xFWEQdyFMF4AAAAd/husky-aoshima.gif",
            "https://media.tenor.com/SyQkIGpHPlQAAAAC/gtfo-here.gif",
            "https://media.tenor.com/V8Ggrj5o6LMAAAAC/star-stare.gif",
            "https://media.tenor.com/t8s69XtatUMAAAAd/laughing.gif",
            "https://media.tenor.com/lcWVmQyyEfsAAAAd/very-fast-rat-rat.gif",
            "https://media.tenor.com/vW4zvZvd-5IAAAAd/caught-staring.gif"
            ]
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)     

    @commands.command(aliases=["dancing","dances"])
    async def dance(self,ctx,user:discord.Member=None):
        if user == None:
            embed=discord.Embed(title=f"{ctx.author.name} is dancing",color = discord.Colour.purple())
        else:
            embed=discord.Embed(title=f"{user.name} and {ctx.author.name} are dancing",color = discord.Colour.purple())    
        if user!=None and user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return 
        randomgifs = [
            "https://media.tenor.com/tInXY9TY0oMAAAAd/meme-dance.gif",
            "https://media.tenor.com/LUFs-A8Gx0MAAAAd/dance-dancing.gif",
            "https://media.tenor.com/I5aPBidmLF0AAAAC/pokemon-gavin.gif",
            "https://media.tenor.com/FVL5Kgfv8kAAAAAd/happy.gif",
            "https://media.tenor.com/D4UWrImI444AAAAC/milk-and-mocha-dance.gif",
            "https://media.tenor.com/xoxmiTsSwpoAAAAC/pikachu-happy-dance.gif",
            "https://media.tenor.com/VDB_fhhFgc0AAAAd/dancing-funny.gif",
            "https://media.tenor.com/ME4hOuZqjx4AAAAC/bear-dance.gif",
            "https://media.tenor.com/4lSmlqz0_6kAAAAC/happy-dance.gif",
            "https://media.tenor.com/U37Ev2O1FCQAAAAC/drink-thats.gif",
            "https://media.tenor.com/J8KeZSDe_acAAAAC/dace.gif",
            "https://media.tenor.com/Qg2Nyx9Z_HgAAAAC/jhope-dancing-hobi-jhope-dancing.gif",
            "https://media.tenor.com/wFtRdoHX-ssAAAAd/dance-happy.gif",
            "https://media.tenor.com/z3HX03QXMqgAAAAd/leslie-jordan-leslie.gif",
            "https://media.tenor.com/JkxKNE7CzDYAAAAC/depeg-nation.gif",
            "https://media.tenor.com/lm63WPHdZe8AAAAd/gummib%C3%A4r-gummibar.gif",
            "https://media.tenor.com/5wrERrJEcHUAAAAd/elastic-dancer-dancer.gif",
            "https://media.tenor.com/JJK-l5dmdVkAAAAd/jim-carrey-jim.gif"

         ]
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)

    @commands.command(aliases=["shocking","shocked"])
    async def shock(self,ctx,user:discord.Member=None):
        if user == None:
            embed=discord.Embed(title=f"{ctx.author.name} is shocked!",color = discord.Colour.purple())
        else:
            embed=discord.Embed(title=f"{ctx.author.name} is shocked at {user.name}'s actions",color = discord.Colour.purple())    
        if user!=None and user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return 
        randomgifs = [
            "https://media.tenor.com/brOqSeAfbnoAAAAC/amazed-jerry.gif",
            "https://media.tenor.com/Ogxu9GElDCAAAAAd/jinki948-cat.gif",
            "https://media.tenor.com/HQcfsVLt2F8AAAAC/tom-and-jerry-tom-the-cat.gif",
            "https://media.tenor.com/MMBniFK8VrsAAAAC/amazing-pikachu.gif",
            "https://media.tenor.com/rXksyOJqrsIAAAAC/milkandmocha-wtf.gif",
            "https://media.tenor.com/hjHD1XIY3scAAAAd/blink-ibigmerm.gif",
            "https://media.tenor.com/r8tcf2YZ5TIAAAAd/blinking-eyes-white-guy.gif",
            "https://media.tenor.com/iNdp1FlmIJgAAAAC/hand-over-mouth-shock.gif",
            "https://media.tenor.com/gzZyXppSYFoAAAAC/kirk-shocked.gif",
            "https://media.tenor.com/YgB6fvEfC2AAAAAC/droggo-dog.gif",
            "https://media.tenor.com/uPNLNvFpl5UAAAAd/shocked-shock.gif",
            "https://media.tenor.com/Fipe91QSAegAAAAd/dedikodu-gossip.gif",
            "https://media.tenor.com/B_vjl0kQEYMAAAAd/arifn13-candiace-dillard.gif",
            "https://media.tenor.com/34LWBKgBDB4AAAAM/hololive-lamy.gif",
            "https://media.tenor.com/2utsFw5wZnUAAAAC/in-shock.gif",
            "https://media.tenor.com/Xz3CtMXod5kAAAAC/humanity-has-declined-jinrui-wa-suitai-shimashita.gif",
            "https://media.tenor.com/sw-icRLFAiwAAAAd/shock-shocked.gif",
            "https://media.tenor.com/HU6E9HN1dSAAAAAd/head-turn.gif",
            "https://media.tenor.com/qr0f_Ki14P4AAAAC/little-witch-academia-lotte-jansson.gif",
            "https://media.tenor.com/6MLf0Ut6zsQAAAAC/little-witch-academia-atsuko-kagari.gif",
            "https://media.tenor.com/h0MIy3XsGK0AAAAC/cammy-cammy-nation.gif",
            "https://media.tenor.com/MidkE6WxcsYAAAAC/cultofthelamb-shocked.gif",
            "https://media.tenor.com/ODbZar1rE_AAAAAC/shock-shocking.gif",
            "https://media.tenor.com/J_0YTU6KnYMAAAAC/omg-shock.gif",
            "https://media.tenor.com/-u5rwwp3_NEAAAAC/hikari-shock.gif"
            ]
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)      
           

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(wave(bot))       
    print("wave, highfive, yawn, vibe, stare, dance is loaded")    
       
        
   