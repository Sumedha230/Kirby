import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import CommandTree
import requests
import discord.ui
from discord.ui import Button,View
import random

class block(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["Block",'blocking'])
    async def block(self,ctx,user:discord.Member=None):
        if user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        randomgifs = [
            "https://media.discordapp.net/attachments/1045618243013984296/1046464011241271326/giphy.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046464027955564665/364354045cd96a0726981be285a0ab74.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046465161105522770/critical-bard-cb.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046465161961164850/giphy_1.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046465167048855672/brucevain-blocked.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046465170593034270/giphy_2.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046465187840012288/tumblr_p2yzauQ8lq1qgf1i8o1_500.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054497056091279410/block6.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054497056452001842/block5.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054497056980467783/block4.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054497057378943077/block3.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054497057928380426/block2.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054497058310078547/block1.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054497058612051998/block10.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054497058930823238/block9.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054497059245408276/block8.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054497135552372818/block18.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054497135988584538/block17.gif?width=536&height=606",
            "https://media.discordapp.net/attachments/1035565430422642718/1054497136433176628/block12.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054497136844222514/block11.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054497137695658134/block15.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054497138412888134/block13.gif"         
        ]
        embed=discord.Embed(title=f"{ctx.author.name} has blocked {user.name}, They probably deserved it ",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed) 

    @commands.command(aliases=["Bonk","BONK"])
    async def bonk(self,ctx,user:discord.Member=None):
        if user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        randomgifs = [
            "https://media.discordapp.net/attachments/949680123869814794/1046892437043429416/detcgjg-50c2474a-fbbb-44f1-9766-a89f7f8e8253.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046892437555130440/bonk_2.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046892437953593534/b0d270b7c07757cc6c3fb6efc60229e8.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046892438322688190/bonk-anime.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046892438654030045/bonk.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046892439060885646/giphy.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054499490423386112/bonk10.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054499490746335252/bonk9.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054499491157389342/bonk8.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054499491425812580/bonk7.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054499491723628594/bonk6.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054499492092719115/bonk5.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054499492478582805/bonk4.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054499492801556570/bonk3.gif?width=606&height=606",
            "https://media.discordapp.net/attachments/1035565430422642718/1054499493149671524/bonk2.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054499493489430628/bonk1.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054499538708213770/bonk20.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054499539056332850/bonk19.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054499539421245611/bonk18.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054499539870027916/bonk17.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054499540276879420/bonk16.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054499540985716907/bonk14.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054499540612419625/bonk15.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054499541459677205/bonk13.gif?width=606&height=606",
            "https://media.discordapp.net/attachments/1035565430422642718/1054499541820383332/bonk12.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054499542185283656/bonk11.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054499590121979964/bonk30.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054499590814056478/bonk28.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054499590491086909/bonk29.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054499591871021169/bonk25.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054499592214937661/bonk24.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054499592902819850/bonk22.gif?width=506&height=607",
            "https://media.discordapp.net/attachments/1035565430422642718/1054499593221570653/bonk21.gif"
            ]
        
        embed=discord.Embed(title=f"{ctx.author.name} bonks{user.name} for being horny",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)      

    @commands.command(aliases=["cheering","Cheer","Cheering"])
    async def cheer(self,ctx,user:discord.Member=None):
        if user == None:
            embed=discord.Embed(title=f"{ctx.author.name} is cheering",color = discord.Colour.purple())
        else:
            embed=discord.Embed(title=f"{ctx.author.name} is cheering for {user.name}",color = discord.Colour.purple())    
        if user!=None and user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return 
        randomgifs = [
            "https://media.discordapp.net/attachments/949680123479728146/1047091558597525565/cheer-up-cheer.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047091560598224906/cheer.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047091564226293800/despicable-me-cheering.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047091568198291496/c25208508f5a3d1ada8feab3a503fe46.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047091736985481307/cute-snoopy-cheering-yddakcevbu0bsx26.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047091737136463944/quby-cute.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047091744740749332/cheer_1.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047091750549868564/animated-cheerleader-image-0028.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047091773949870080/go-bun.gif",
            "https://media.tenor.com/KNgFUnmfO7wAAAAi/penguin-ganbatte.gif",
            "https://media.tenor.com/SVcoiQw-iPkAAAAC/pikachu-cheer-dance.gif",
            "https://media.tenor.com/nOvvLYVNyFsAAAAd/sashaverse.gif",
            "https://media.tenor.com/7XmW1k6F5XsAAAAC/plusle-minun.gif",
            "https://media.tenor.com/4WxLSgRaPNkAAAAi/cheer-enthusiastic.gif",
            "https://media.tenor.com/gx9p7k_gd94AAAAC/patrick-star-spongebob-squarepants.gif",
            "https://media.tenor.com/_efodCJKu6kAAAAi/cheer-cheers.gif",
            "https://media.tenor.com/EfVExmxbj2oAAAAi/menhera-cheer-up.gif",
            "https://media.tenor.com/c_tVFX3CxuIAAAAi/stitch-cheer.gif",
            "https://media.tenor.com/BiuI7UqmupIAAAAC/bear-cute.gif",
            "https://media.tenor.com/I0vlwUD6cWYAAAAC/pokemon-anime.gif",
            "https://media.tenor.com/d2NYSXokaK4AAAAC/pikachu-cheer-dance.gif",
            "https://media.tenor.com/HfAkD-3qf0QAAAAd/cheerleader-jerry.gif",
            "https://media.tenor.com/LgK6vitibRoAAAAC/cheerleader-cheering.gif",
            "https://media.tenor.com/yrqYJ1IqqcAAAAAC/lets-cheer-snoopy.gif",
            "https://media.tenor.com/PJ7zlIHzDY8AAAAC/pokemon-piplup.gif",
            "https://media.tenor.com/Bo6MNAAEj3AAAAAC/tontonfriends-cheers.gif",
            "https://media.tenor.com/jWspRlpyVtcAAAAC/snl-cheer.gif",
            "https://media.tenor.com/qjtbJam6ZOAAAAAd/friends-rachel-green.gif",
            "https://media.tenor.com/Q3v16em3H4EAAAAC/tobi-winnie.gif",
            "https://media.tenor.com/ik5fbcb8EE4AAAAC/thumbs-up-go.gif",
            "https://media.tenor.com/vLpb3TKeGswAAAAC/woohoo-cheer.gif",
            "https://media.tenor.com/7uZ-4XLhRB0AAAAC/cheer-up-angel.gif",
            "https://media.tenor.com/yTs3fJHYLI0AAAAC/pikachu-yeah.gif",
        ]
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)   

    @commands.command(aliases=["Choke",'choking'])
    async def choke(self,ctx,user:discord.Member=None):
        if user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        randomgifs = [
            "https://media.tenor.com/CzFhk3N8pcEAAAAC/angry-anime-choke.gif",
            "https://media.tenor.com/8SLcFEZpv7wAAAAd/bert-hellinger-choked.gif",
            "https://media.tenor.com/zsfT_l5SRvoAAAAC/homer-choking.gif",
            "https://media.tenor.com/9tLFBQer1j4AAAAC/the-mandalorian-star-wars.gif",
            "https://media.tenor.com/_o0Y5AXQPYMAAAAd/choke-cekek.gif",
            "https://media.tenor.com/_z2Bd1bfpCIAAAAC/seo-ye-ji-its-okay-to-not-be-okay.gif",
            "https://media.tenor.com/paw7IWHfk0kAAAAC/chokehold-choke-out.gif",
            "https://media.tenor.com/8hvUDwOBhooAAAAd/bjj-jiu-jitsu.gif",
            "https://media.tenor.com/WNfDRGwgS7IAAAAC/jerm-jermbeezy.gif",
            "https://media.tenor.com/arqy-kNpbn0AAAAC/miko-yotsuya-julia-niguredou.gif",
            "https://media.tenor.com/wFlSXwp_VE4AAAAC/choked-hurt.gif",
            "https://media.tenor.com/GYRFVcpy-_8AAAAC/friends-messing.gif",
            "https://media.tenor.com/gC2FMcLVP3AAAAAd/choke-out.gif",
            "https://media.tenor.com/n0xD9x7Ftc0AAAAd/192-cops.gif",
            "https://media.tenor.com/1_RSoYB6i5QAAAAd/itachi-sasuke.gif",
            "https://media.tenor.com/kAxTkID2xKMAAAAC/kojiro-musashi.gif",
            "https://media.tenor.com/JWz5PnSB0KIAAAAC/choking-flower.gif",
            "https://media.tenor.com/USfsssJOQOUAAAAC/kurosue-anime.gif",
            "https://media.tenor.com/RuUwgozqcGgAAAAC/lloyd-irving-tales-of-symphonia.gif",
            "https://media.tenor.com/TclCqj4Fj50AAAAC/kubi-shime-anime.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046357753582583838/Kylo_Ren_Star_Wars_GIF_-_Kylo_Ren_Star_Wars_Choke_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046357753905565746/Love_Choked_GIF_-_Love_Choked_Spongebob_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046357754199158814/Homer_Choking_Bart_GIF_-_Simpsons_Angry_Furious_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046357754522107975/Choke_Love_GIF_-_Choke_Love_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046475535770976326/Anime_Choke_GIF_-_Anime_Choke_Hug_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046475536521773147/Margot_Robbie_Choke_GIF_-_Margot_Robbie_Choke_Joker_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046475536916025454/gif.gif",
            "https://media.tenor.com/MAyctLUTrwQAAAAi/axie-infinity-axie.gif",
            "https://media.tenor.com/-Q91GHdD5d8AAAAC/choke-the.gif",
            "https://media.tenor.com/PiFqVBIspFYAAAAC/anime-choke.gif",
            "https://media.tenor.com/CzFhk3N8pcEAAAAC/angry-anime-choke.gif",
            "https://media.tenor.com/YR-Mxu6SE6sAAAAC/mitskidiamandis-homer.gif",
            "https://media.tenor.com/sg3WsigaMEcAAAAd/choke.gif",
            "https://media.tenor.com/_o0Y5AXQPYMAAAAd/choke-cekek.gif",
            "https://media.tenor.com/wFlSXwp_VE4AAAAC/choked-hurt.gif",
            "https://media.tenor.com/0fr2YNH7HAEAAAAC/sml-junior.gif",
            "https://media.tenor.com/9jQlNTyZJDkAAAAd/peaches-chokehold.gif"
        ]
        embed=discord.Embed(title=f"{ctx.author.name} is choking {user.name} hard!!",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)   

    @commands.command(aliases=["Cope"])
    async def cope(self,ctx,user:discord.Member=None):
        if user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        randomgifs = [
            "https://media.discordapp.net/attachments/1045618243013984296/1046467949839532135/6glhrr.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046467960799248424/929.gif?width=581&height=606",
            "https://media.discordapp.net/attachments/1045618243013984296/1046467971104636998/cope_3.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046467979115765791/cope_1.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046467982357958656/cope_2.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046467982697709658/AmazingGleamingAlpineroadguidetigerbeetle-size_restricted.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046468043431235645/cope.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046468043934548088/cope-seethe-cope-cope.gif"         
        ]
        embed=discord.Embed(title=f"{ctx.author.name} is telling {user.name} to cope harder",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)   

    @commands.command(aliases=["Crying","cry","Cry"])
    async def crying(self,ctx,user:discord.Member=None):
        if user == None:
            embed=discord.Embed(title=f"{ctx.author.name} is crying",color = discord.Colour.purple())
        else:
            embed=discord.Embed(title=f"{user.name} made {ctx.author.name} cry! Truly a monster",color = discord.Colour.purple())    
        if user!=None and user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return 
        randomgifs = [
            "https://media.discordapp.net/attachments/1045618240900050954/1046356250385977444/byuntear-baby-cry.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046356587108913172/spiderman-crying.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046356597573697576/de7c30415be157a3f579b38bc6564461.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046356607216398406/c7eb5bbae52025b4d2ad9b8224022bd4.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046474508028088430/25e2a496c8204acd1e5c459d86d905e4.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046474520413884476/c4f0d6c08257f3a75725a7583894b1b8.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046474541683183616/RigidDimpledAmericanpainthorse-max-1mb.gif"
            "https://media.discordapp.net/attachments/1045618243013984296/1046476115088252928/Capoo_Bugcat_Sticker_-_Capoo_Bugcat_Blue_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046476116929556520/Anime_Cry_GIF_-_Anime_Cry_Crying_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046476117697101926/Cat_Cry_Sticker_-_Cat_Cry_Meme_-_Discover__Share_GIFs.gif",
            "https://media.tenor.com/hLgZBJ7RjzYAAAAi/cute-dog.gif",
            "https://media.tenor.com/ba50GB33iE4AAAAd/baby-crying-crying-baby.gif",
            "https://media.tenor.com/UIXwsWt9n9cAAAAd/crying-girl-crying.gif",
            "https://media.tenor.com/Q9MAbF6w__QAAAAC/spy-x-family-anya-cry.gif",
            "https://media.tenor.com/dpMo4mGQqisAAAAd/sakura-yamauchi-crying-anime-girl.gif",
            "https://media.tenor.com/Dn5rWga89nQAAAAd/woman-crying-crying.gif",
            "https://media.tenor.com/AkwsdClClm4AAAAd/james-team-rocket.gif",
            "https://media.tenor.com/5I5gZD2WPX8AAAAC/crying-cry.gif",
            "https://media.tenor.com/lzDMeUaMEvkAAAAd/jmthjk.gif",
            "https://media.tenor.com/bMTwfdlrXJMAAAAd/crying-sad.gif",
            "https://media.tenor.com/zAahgvyStyUAAAAC/angry-baby-baby.gif",
            "https://media.tenor.com/TYSqB4d-uvoAAAAi/cute-crying.gif",
            "https://media.tenor.com/oSDgPLREcwQAAAAd/ousama-ranking-bojji.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046357237255372840/Kuromi_Crying_GIF_-_Kuromi_Crying_Onegai_My_Melody_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046357237599309824/Anime_Cry_GIF_-_Anime_Cry_Crying_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046357237876138014/Emoji_Crying_GIF_-_Emoji_Crying_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046357238161342514/Sad_Monsters_Inc_GIF_by_filmeditor_-_Find__Share_on_GIPHY.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046474523995820073/woman-crying-hard-lskfg2qn6wo9yiox.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046474547374870528/tumblr_nabqw145or1slmtxco1_500.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046476115964866630/download.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046476116602388490/Sad_The_Simpsons_GIF_-_Find__Share_on_GIPHY.gif"

        ]
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)                   

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(block(bot))       
    print("block, bonk, cheer, choke, cope, cry is loaded")    
       
        
   
