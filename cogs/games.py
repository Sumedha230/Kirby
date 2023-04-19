import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import CommandTree
import requests
import discord.ui
from discord.ui import Button,View
from pprint import pprint
import random

class games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name="never_have_i_ever",aliases=['nhie','neverhie','neverhaveiever'])
    async def nhie(self,ctx):
        async def button_callback(interaction):
            r = requests.get("https://api.truthordarebot.xyz/api/nhie")
            res = r.json()
            em = discord.Embed(title="Never Have I Ever Question",description = f"{res['question']}",color = discord.Colour.purple())
            button = Button(label="Never Have I Ever",style=discord.ButtonStyle.primary)
            button.callback = button_callback     
            view = View()
            view.add_item(button)
            await interaction.response.edit_message(embed=em,view=view)
        button = Button(label="Never Have I Ever",style=discord.ButtonStyle.primary)
        button.callback = button_callback      
        view = View()
        view.add_item(button)    
        r = requests.get("https://api.truthordarebot.xyz/api/nhie")
        res = r.json()
        em = discord.Embed(title="Never Have I Ever Question",description = f"{res['question']}",color = discord.Colour.purple())
        await ctx.send(embed=em,view=view)  

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
            await interaction.response.edit_message(embed=em,view=view)
        button = Button(label="Paranoia",style=discord.ButtonStyle.primary)
        button.callback = button_callback      
        view = View()
        view.add_item(button)    
        r = requests.get("https://api.truthordarebot.xyz/api/paranoia")
        res = r.json()
        em = discord.Embed(title="Paranoia Question",description = f"{res['question']}",color = discord.Colour.purple())
        await ctx.send(embed=em,view=view) 

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
            await interaction.response.edit_message(embed=em,view=view)
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
    
    @commands.hybrid_command(name="repeat",aliases=['rep'])
    async def repeat(self,ctx, times: int,*,content:str):
        """Repeats whatever the user has typed  using krepeat 2 hi or krep 2 hi"""
        if 0<times<=5:
            for i in range(times):
                await ctx.send("".join(content)) 
        else:
            embed = discord.Embed(color = discord.Colour.purple(),description="Kirby is not a fool and won't spam the chat")
            embed.set_image(url ="https://media.discordapp.net/attachments/1042790120652275853/1045611042228666408/kirby-mad.gif")
            await ctx.send(embed=embed) 

    @commands.hybrid_command(name="would_you_rather",aliases=["wyr",'wouldyourather','wouldyr'])
    async def wyr(self,ctx):
        async def button_callback(interaction):
            r = requests.get("https://api.truthordarebot.xyz/api/wyr")
            res = r.json()
            em = discord.Embed(title="Would You Rather Question",description = f"{res['question']}",color = discord.Colour.purple())
            button = Button(label="Would You Rather",style=discord.ButtonStyle.primary)
            button.callback = button_callback     
            view = View()
            view.add_item(button)
            await interaction.response.edit_message(embed=em,view=view)
        button = Button(label="Would You Rather",style=discord.ButtonStyle.primary)
        button.callback = button_callback      
        view = View()
        view.add_item(button)    
        r = requests.get("https://api.truthordarebot.xyz/api/wyr")
        res = r.json()
        em = discord.Embed(title="Would You Rather Question",description = f"{res['question']}",color = discord.Colour.purple())
        await ctx.send(embed=em,view=view) 

    @commands.hybrid_command(aliases=['dk','darkj','dark'])
    async def darkjoke(self,ctx):
        if ctx.channel.is_nsfw():
            r = requests.get("https://v2.jokeapi.dev/joke/Dark")
            res = r.json()
            if res['type']=='single':
                jokes = "".join(res['joke'])
                em = discord.Embed(title="Dark Joke",description = f"{jokes}",color = discord.Colour.purple())
            else:
                jokes = "".join(res['setup'])
                em = discord.Embed(title="Dark Joke",description = f"{jokes}",color = discord.Colour.purple())
                jokes = "".join(res['delivery'])
                em.add_field(name='---',value=f"{jokes}")
            await ctx.send(embed=em)        
        else:
            await ctx.send("Dark Jokes are not for everyone so do in an NSFW Channel")  

    @commands.hybrid_command()
    async def joke(self,ctx):
        r = requests.get("https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,explicit")
        res = r.json()
        if res['type']=='single':
            jokes = "".join(res['joke'])
            em = discord.Embed(title="Bad Joke",description = f"{jokes}",color = discord.Colour.purple())
        else:
            jokes = "".join(res['setup'])
            em = discord.Embed(title="Bad Joke",description = f"{jokes}",color = discord.Colour.purple())
            jokes = "".join(res['delivery'])
            em.add_field(name='---',value=f"{jokes}")
        await ctx.send(embed=em)   

    @commands.hybrid_command(aliases=['dadj','dj'])
    async def dadjoke(self,ctx):
        url = "https://dad-jokes.p.rapidapi.com/random/joke"

        headers = {
	     "X-RapidAPI-Key": "eb205e7f48mshbe28519f8133dcap1aea11jsnaed55c3ce6bf",
	       "X-RapidAPI-Host": "dad-jokes.p.rapidapi.com"
         }

        response = requests.request("GET", url, headers=headers)
        res = response.json()
    
        t = res['body']
        t = t[0]
        
        ret = "".join(t['setup'])
        em = discord.Embed(title="Dad Joke",description = f"{ret}",color = discord.Colour.purple())
        jokes = "".join(t['punchline'])
        em.add_field(name='---',value=f"{jokes}")
        await ctx.send(embed=em)

    @commands.hybrid_command()
    async def weather(self,ctx,*,city:str):
        url = "https://weatherapi-com.p.rapidapi.com/current.json"
        querystring = {"q":f"{city}"}
        headers = {
	"X-RapidAPI-Key": "eb205e7f48mshbe28519f8133dcap1aea11jsnaed55c3ce6bf",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}
        response = requests.request("GET", url, headers=headers, params=querystring)
        res = response.json()
        em = discord.Embed(title="Weather Condition",description = f"The Weather in {res['location']['name']} is",color = discord.Colour.purple())
        em.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        t = res['current']
        em.add_field(name="Current Conditions",value=f"Temperature in Celsius : {t['temp_c']} °C\nTemperature in Farhenheit : {t['temp_f']} F",inline="False")
        t = res['location']
        em.add_field(name="Country Details",value=f"Country : {t['country']}\nTime in {t['country']} : {t['localtime']}\nCity : {t['name']}\nRegion : {t['region']}")
        em.set_thumbnail(url="https://media.tenor.com/Xh858Z_KDZcAAAAC/hurricane-storm.gif")
        
        await ctx.send(embed=em)  


async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(games(bot))       
    print("Nhie , para , tord , repeat , wyr, darkjoke, joke, dadjoke, weather is loaded")    
