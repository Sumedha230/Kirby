import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import CommandTree
import requests
import discord.ui
from discord.ui import Button,View
import random

class animals(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cat(self,ctx):
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "cat"
           
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed=discord.Embed(title=f"{ctx.author.name} wants to see cute catto!!",color = discord.Colour.purple())
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed) 

    @commands.command()
    async def dog(self,ctx):
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "dog"
           
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed=discord.Embed(title=f"{ctx.author.name} wants to see cute dogs !!",color = discord.Colour.purple())
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)   

    @commands.command()
    async def otter(self,ctx):
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "otter"
           
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed=discord.Embed(title=f"{ctx.author.name} wants to see cute otters !!",color = discord.Colour.purple())
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)  

    @commands.command(aliases=['capy'])
    async def capybara(self,ctx):
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "capybara"
           
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed=discord.Embed(title=f"{ctx.author.name} wants to see cute capybaras !!",color = discord.Colour.purple())
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)  

    @commands.command(aliases=['polar'])
    async def polarbear(self,ctx):
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "polar bear"
           
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed=discord.Embed(title=f"{ctx.author.name} wants to see cute polar bears !!",color = discord.Colour.purple())
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)           

    @commands.command()
    async def raccoon(self,ctx):
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "raccoon"
           
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed=discord.Embed(title=f"{ctx.author.name} wants to see cute raccoons !!",color = discord.Colour.purple())
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)   

    @commands.command()
    async def panda(self,ctx):
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "panda"
           
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed=discord.Embed(title=f"{ctx.author.name} wants to see cute pandas !!",color = discord.Colour.purple())
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)    

    @commands.command()
    async def koala(self,ctx):
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "koala"
           
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed=discord.Embed(title=f"{ctx.author.name} wants to see cute koalas !!",color = discord.Colour.purple())
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed) 

    @commands.command(aliases=['squirrel'])
    async def squirrels(self,ctx):
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "squirrel"
           
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed=discord.Embed(title=f"{ctx.author.name} wants to see cute squirrels !!",color = discord.Colour.purple())
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)      

    @commands.command(aliases=['hamsters'])
    async def hamster(self,ctx):
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "hamster"
           
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed=discord.Embed(title=f"{ctx.author.name} wants to see cute hamsters !!",color = discord.Colour.purple())
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed) 

    @commands.command(aliases=['rabbits'])
    async def rabbit(self,ctx):
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "rabbit"
           
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed=discord.Embed(title=f"{ctx.author.name} wants to see cute rabbits !!",color = discord.Colour.purple())
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)   

    @commands.command()
    async def duck(self,ctx):
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "duck"
           
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed=discord.Embed(title=f"{ctx.author.name} wants to see cute ducks !!",color = discord.Colour.purple())
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)  

    @commands.command(aliases=['bunnies'])
    async def bunny(self,ctx):
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "bunny"
           
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed=discord.Embed(title=f"{ctx.author.name} wants to see cute bunnies !!",color = discord.Colour.purple())
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)      
    
    @commands.command(aliases=['ferrets'])
    async def ferret(self,ctx):
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "ferret"
           
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed=discord.Embed(title=f"{ctx.author.name} wants to see cute ferrets !!",color = discord.Colour.purple())
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed) 

    @commands.command()
    async def turtle(self,ctx):
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "turtle"
           
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed=discord.Embed(title=f"{ctx.author.name} wants to see cute turtles !!",color = discord.Colour.purple())
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)   

    @commands.command(aliases=['monke'])
    async def monkey(self,ctx):
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "monke"
           
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed=discord.Embed(title=f"{ctx.author.name} wants to see cute monkey !!",color = discord.Colour.purple())
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)   

    @commands.command(aliases=['pup'])
    async def puppy(self,ctx):
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "puppy"
           
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed=discord.Embed(title=f"{ctx.author.name} wants to see cute puppy !!",color = discord.Colour.purple())
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed) 

    @commands.command(aliases=['kitty'])
    async def kitten(self,ctx):
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "kittens"
           
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed=discord.Embed(title=f"{ctx.author.name} wants to see cute kitten !!",color = discord.Colour.purple())
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)   

    @commands.command()
    async def sloth(self,ctx):
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "sloth"
           
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed=discord.Embed(title=f"{ctx.author.name} is a sloth !!",color = discord.Colour.purple())
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)      

    @commands.command()
    async def cow(self,ctx):
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "cow"
           
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed=discord.Embed(title=f"{ctx.author.name} is a cow !!",color = discord.Colour.purple())
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)     

    @commands.command()
    async def fox(self,ctx):
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "cute fox"
           
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed=discord.Embed(title=f"{ctx.author.name} wants to see cute fox !!",color = discord.Colour.purple())
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed) 

    @commands.command(aliases=['seals'])
    async def seal(self,ctx):
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "cute seals"
           
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed=discord.Embed(title=f"{ctx.author.name} wants to see cute seal !!",color = discord.Colour.purple())
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)   

    @commands.command()
    async def pig(self,ctx):
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "cute pig"
           
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed=discord.Embed(title=f"{ctx.author.name} wants to see cute pig because they are one !!",color = discord.Colour.purple())
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed) 

    @commands.command()
    async def alpaca(self,ctx):
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "cute alpaca"
           
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed=discord.Embed(title=f"{ctx.author.name} wants to see cute alpaca !!",color = discord.Colour.purple())
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)   

    @commands.command()
    async def kia(self,ctx):
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "monke"
           
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed=discord.Embed(title=f"This is our Kia",color = discord.Colour.purple())
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)      

    @commands.command()
    async def patch(self,ctx):
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "cute otter"
           
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed=discord.Embed(title=f"This is Patch",color = discord.Colour.purple())
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)    

    @commands.command()
    async def hippo(self,ctx):
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "cute hippopotamus"
           
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed=discord.Embed(title=f"{ctx.author.name} wants to see cute hippo !!",color = discord.Colour.purple())
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed) 

    @commands.command()
    async def lion(self,ctx):
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "cute lions"
           
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed=discord.Embed(title=f"{ctx.author.name} wants to see cute lion !!",color = discord.Colour.purple())
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed) 

    @commands.command()
    async def zebra(self,ctx):
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "animal zebra"
           
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed=discord.Embed(title=f"{ctx.author.name} wants to see cute zebra !!",color = discord.Colour.purple())
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed) 

    @commands.command()
    async def penguin(self,ctx):
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "cute penguin"
           
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed=discord.Embed(title=f"{ctx.author.name} wants to see cute penguin !!",color = discord.Colour.purple())
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)    

    @commands.command()
    async def kashi(self,ctx):
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "wild guy"
           
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed=discord.Embed(title=f"This is kashi",color = discord.Colour.purple())
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)  

    @commands.command()
    async def dumdum(self,ctx):
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "dumbass"
           
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed=discord.Embed(title=f"Derron is a dumbass",color = discord.Colour.purple())
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed) 

    @commands.command()
    async def nessa(self,ctx):
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "cute baby"
           
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed=discord.Embed(title=f"This is NESSA",color = discord.Colour.purple())
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)                                                                                       

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(animals(bot))       
    print("cat, dog, otter, capybara, ,hippo, ,penguin, lion, zebra, polar bear, racoon, panda, koalas, squirrels, hamsters, rabbit, duck, bunny, ferrets, turtle, monke, puppy, kitty, sloth, cow, fox, seal, pig, alpaca is loaded")    
   
