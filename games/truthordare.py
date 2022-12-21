import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import CommandTree
import requests
import discord.ui
from discord.ui import Button,View

class tord(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.hybrid_command(name="truth_or_dare",aliases=['tord','truth','dare','truthordare'])
    async def truth_or_dare(self,ctx):
        """ Type ktord or ktruth_or_dare to play the game"""
        button = Button(label="Truth",style=discord.ButtonStyle.primary)
        async def button_callback(interaction):
            r = requests.get("https://api.truthordarebot.xyz/v1/truth")
            res = r.json()
            em = discord.Embed(title="Truth Question",description = f"{res['question']}",color = discord.Colour.purple())
            button = Button(label="Truth",style=discord.ButtonStyle.primary)
            button.callback = button_callback
            button2 = Button(label="Dare",style=discord.ButtonStyle.primary)
            button2.callback = button2_callback  
            view = View()
            view.add_item(button)
            view.add_item(button2)
            await interaction.response.send_message(embed=em,view=view)
        button.callback = button_callback    
        button2 = Button(label="Dare",style=discord.ButtonStyle.primary)
        async def button2_callback(interaction):
            r = requests.get("https://api.truthordarebot.xyz/v1/dare")
            res = r.json()
            button2 = Button(label="Dare",style=discord.ButtonStyle.primary)
            button2.callback = button2_callback   
            button = Button(label="Truth",style=discord.ButtonStyle.primary)
            button.callback = button_callback
            em = discord.Embed(title="Dare",description = f"{res['question']}",color = discord.Colour.purple())
            view = View()
            view.add_item(button)
            view.add_item(button2)
            await interaction.response.send_message(embed=em,view=view)
        button2.callback = button2_callback      
        view = View()
        view.add_item(button)
        view.add_item(button2)
        em = discord.Embed(title="Truth or Dare",description = f"Choose either a Truth or a Dare",color = discord.Colour.purple())
        await ctx.send(embed=em,view=view)  
        

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(tord(bot))       
    print("truth or dare is loaded")    
