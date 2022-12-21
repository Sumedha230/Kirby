import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import CommandTree
import requests
import discord.ui
from discord.ui import Button,View
import random

class slap(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["Slap"])
    async def slap(self,ctx,user:discord.Member=None):
        if user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        randomgifs = [
            "https://media.discordapp.net/attachments/1045618240900050954/1045655137953263696/kirby-king-dedede.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1045656005356310558/WiffleGif.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1045657796986802217/kirboslapping.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046388711555870720/will-smith-will-smith-slap.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046388714768707645/40fa327344c9a71783b1cd77afa19ac9.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046388727225782313/4ec47d7b87a9ce093642fc8a3c2969e7.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046388736755253278/slapping.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047136738918809681/slap_4.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047136740512649237/slap-christmas.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047136744656621599/slap_5.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047136999401857024/spongebob-squarepants-patrick-star.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047137009317204078/slap-slapping_1.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047137009598222336/smack-shut-up_1.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047137013914148864/wrrruutchxxxxiii-slapt.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047137093538811914/molorant-ckaz_1.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047137098945269790/slap-slap.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047137109212938250/slap_7.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047137109397487616/slap_6.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047137289064697866/slap_9.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047137297524609076/slap_8.gif",
            "https://media.discordapp.net/attachments/949680123479728146/1047137299638525992/slap-dog-slap-shiba.gif?width=606&height=606"
        ]
        embed=discord.Embed(title=f"{ctx.author.name} has slapped {user.name}!",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)     
    

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(slap(bot))       
    print("slap is loaded")    
       
    