import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import CommandTree
import requests
import discord.ui
from discord.ui import Button,View

class wyr(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.hybrid_command(name="would_you_rather",aliases=["wyr",'wouldyourather','wouldyr'])
    async def wyr(self,ctx):
        """Type kwould_you_rather or kwyr to play the game"""
        async def button_callback(interaction):
            r = requests.get("https://api.truthordarebot.xyz/api/wyr")
            res = r.json()
            em = discord.Embed(title="Would You Rather Question",description = f"{res['question']}",color = discord.Colour.purple())
            button = Button(label="Would You Rather",style=discord.ButtonStyle.primary)
            button.callback = button_callback     
            view = View()
            view.add_item(button)
            await interaction.response.send_message(embed=em,view=view)
        button = Button(label="Would You Rather",style=discord.ButtonStyle.primary)
        button.callback = button_callback      
        view = View()
        view.add_item(button)    
        r = requests.get("https://api.truthordarebot.xyz/api/wyr")
        res = r.json()
        em = discord.Embed(title="Would You Rather Question",description = f"{res['question']}",color = discord.Colour.purple())
        await ctx.send(embed=em,view=view)   
        

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(wyr(bot))       
    print("would you rather is loaded")    
