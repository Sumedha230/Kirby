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
    

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(eat(bot))       
    print("eat, blush is loaded")    
       
        
   