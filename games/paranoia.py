import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import CommandTree
import requests
import discord.ui
from discord.ui import Button,View

class paranoia(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.hybrid_command(name="paranoia",aliases=['para','par','pn'])
    async def par(self,ctx):
        """ Type kpara or kparanoia to play the game"""
        async def button_callback(interaction):
            r = requests.get("https://api.truthordarebot.xyz/api/paranoia")
            res = r.json()
            em = discord.Embed(title="Paranoia Question",description = f"{res['question']}",color = discord.Colour.purple())
            button = Button(label="Paranoia",style=discord.ButtonStyle.primary)
            button.callback = button_callback     
            view = View()
            view.add_item(button)
            await interaction.response.send_message(embed=em,view=view)
        button = Button(label="Paranoia",style=discord.ButtonStyle.primary)
        button.callback = button_callback      
        view = View()
        view.add_item(button)    
        r = requests.get("https://api.truthordarebot.xyz/api/paranoia")
        res = r.json()
        em = discord.Embed(title="Paranoia Question",description = f"{res['question']}",color = discord.Colour.purple())
        await ctx.send(embed=em,view=view)  

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(paranoia(bot))       
    print("paranoia is loaded")    
