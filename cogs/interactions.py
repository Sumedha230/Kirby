import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import CommandTree
import requests
import discord.ui
from discord.ui import Button,View
import random

class interaction(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["Block",'blocking'])
    async def block(self,ctx,user:discord.Member=None):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            user = original.author
        elif user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return

        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "block"
           
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed=discord.Embed(title=f"{ctx.author.name} has blocked {user.name}, They probably deserved it ",color = discord.Colour.purple())
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed) 

    @commands.command(aliases=["Bonk","BONK"])
    async def bonk(self,ctx,user:discord.Member=None):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            user = original.author
        elif user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "bonk"
           
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        
        embed=discord.Embed(title=f"{ctx.author.name} bonks {user.name} for being horny",color = discord.Colour.purple())
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)      

    @commands.command(aliases=["cheering","Cheer","Cheering"])
    async def cheer(self,ctx,user:discord.Member=None):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            user = original.author
            embed=discord.Embed(title=f"{ctx.author.name} is cheering for {user.name}",color = discord.Colour.purple()) 
        elif user == None:
            embed=discord.Embed(title=f"{ctx.author.name} is cheering",color = discord.Colour.purple())
        else:
            embed=discord.Embed(title=f"{ctx.author.name} is cheering for {user.name}",color = discord.Colour.purple())    
        if user!=None and user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return 
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "cheer"
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)   

    @commands.command(aliases=["Choke",'choking'])
    async def choke(self,ctx,user:discord.Member=None):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            user = original.author
        elif user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "anime choke"     
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed=discord.Embed(title=f"{ctx.author.name} is choking {user.name} hard!!",color = discord.Colour.purple())
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)   

    @commands.command(aliases=["Cope"])
    async def cope(self,ctx,user:discord.Member=None):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            user = original.author
        elif user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "cope"    
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed=discord.Embed(title=f"{ctx.author.name} is telling {user.name} to cope harder",color = discord.Colour.purple())
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)   

    @commands.command(aliases=["Crying","cry","Cry"])
    async def crying(self,ctx,user:discord.Member=None):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            user = original.author
            embed=discord.Embed(title=f"{user.name} made {ctx.author.name} cry! Truly a monster",color = discord.Colour.purple())
        elif user == None:
            embed=discord.Embed(title=f"{ctx.author.name} is crying",color = discord.Colour.purple())
        else:
            embed=discord.Embed(title=f"{user.name} made {ctx.author.name} cry! Truly a monster",color = discord.Colour.purple())    
        if user!=None and user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return 
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "cry"  
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)            

    @commands.command(aliases=["Eating","eat","Eat"])
    async def eating(self,ctx):
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "eat"  
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed=discord.Embed(title=f"{ctx.author.name} is eating! Yummy food",color = discord.Colour.purple())
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed) 

    @commands.command(aliases=["blushes","blushing","Blush"])
    async def blush(self,ctx,user:discord.Member=None):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            user = original.author
            embed=discord.Embed(title=f"{user.name} made {ctx.author.name} blush",color = discord.Colour.purple())        
        elif user == None:
            embed=discord.Embed(title=f"{ctx.author.name} is blushing",color = discord.Colour.purple())
        else:
            embed=discord.Embed(title=f"{user.name} made {ctx.author.name} blush",color = discord.Colour.purple())    
        if user!=None and user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return 
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "blush"  
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)  

    
    @commands.command(aliases=["Kiss"])
    async def kiss(self,ctx,user:discord.Member=None):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            user = original.author
        elif user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        embed=discord.Embed(title=f"{ctx.author.name} has kissed {user.name}",color = discord.Colour.purple())
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "anime kiss"  
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed) 

    @commands.command(aliases=["Kill","KILL",'killing'])
    async def kill(self,ctx,user:discord.Member=None):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            user = original.author
        elif user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return 
        embed=discord.Embed(title=f"{ctx.author.name} killed {user.name} ! They definitely won't be able to type again",color = discord.Colour.purple())
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "anime kill"  
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed) 

    @commands.command()
    async def fuck(self,ctx,user:discord.Member=None):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            user = original.author
        elif user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return 
        embed=discord.Embed(title=f"{ctx.author.name} fucked {user.name}",color = discord.Colour.purple())
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "anime sexy eyes"  
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)          

    @commands.command(aliases=["laughing","Laugh","Laughing"])
    async def laugh(self,ctx,user:discord.Member=None):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            user = original.author
            embed=discord.Embed(title=f"{ctx.author.name} is laughing at {user.name}",color = discord.Colour.purple())
        elif user == None:
            embed=discord.Embed(title=f"{ctx.author.name} is laughing",color = discord.Colour.purple())
        else:
            embed=discord.Embed(title=f"{ctx.author.name} is laughing at {user.name}",color = discord.Colour.purple())    
        if user!=None and user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return 
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "anime laugh"  
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)  

    @commands.command(aliases=["lie","Lie","Liar","LIAR",'lying'])
    async def liar(self,ctx,user:discord.Member=None):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            user = original.author
        elif user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        
        embed=discord.Embed(title=f"{ctx.author.name} is calling {user.name} a liar !",color = discord.Colour.purple())
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "liar"  
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)      

    @commands.command(aliases=["Missing","miss","Miss"])
    async def missing(self,ctx,user:discord.Member=None):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            user = original.author
        elif user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        
        embed=discord.Embed(title=f"{ctx.author.name} is missing {user.name}",color = discord.Colour.purple())
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "anime miss"  
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)  

    @commands.command(aliases=["Hug"])
    async def hug(self,ctx,user:discord.Member=None):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            user = original.author
        elif user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        embed=discord.Embed(title=f"{ctx.author.name} hugs {user.name}",color = discord.Colour.purple())
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "anime hug"  
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)   

    @commands.command(aliases=["boops","bp"])
    async def boop(self,ctx,user:discord.Member=None):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            user = original.author
        elif user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        embed=discord.Embed(title=f"{ctx.author.name} booped {user.name} ",color = discord.Colour.purple())    
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "boop"  
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)   

    @commands.command(aliases=["Pat,'patting","pet"])
    async def pat(self,ctx,user:discord.Member=None):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            user = original.author
        elif user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        
        embed=discord.Embed(title=f"{ctx.author.name} is patting {user.name} because they are cute!",color = discord.Colour.purple())
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "pat"  
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)     

    @commands.command(aliases=["PillowFight","Pillowfight","pf","PF",'pillowf','pfight'])
    async def pillowfight(self,ctx,user:discord.Member=None):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            user = original.author
        elif user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
       
        embed=discord.Embed(title=f"{ctx.author.name} and {user.name} are pillowfighting !",color = discord.Colour.purple())
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "pillowfight"  
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)  

    @commands.command(aliases=["pinching",'Pinch'])
    async def pinch(self,ctx,user:discord.Member=None):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            user = original.author
        elif user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        
        embed=discord.Embed(title=f"{ctx.author.name} is pinching {user.name} !!",color = discord.Colour.purple())
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "pinch"  
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)      

    @commands.command(aliases=["praying","prays"])
    async def pray(self,ctx,user:discord.Member=None):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            user = original.author
            embed=discord.Embed(title=f"{ctx.author.name} is praying for {user.name}",color = discord.Colour.purple())
        elif user == None:
            embed=discord.Embed(title=f"{ctx.author.name} is praying",color = discord.Colour.purple())
        else:
            embed=discord.Embed(title=f"{ctx.author.name} is praying for {user.name}",color = discord.Colour.purple())    
        if user!=None and user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return 
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "pray"  
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)   

    @commands.command(aliases=["salutes",'saluting'])
    async def salute(self,ctx,user:discord.Member=None):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            user = original.author
        elif user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        
        embed=discord.Embed(title=f"{ctx.author.name} is saluting {user.name}!",color = discord.Colour.purple())
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "salute"  
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed) 

    @commands.command(aliases=["Marry","MARRY"])
    async def marry(self,ctx,user:discord.Member=None):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            user = original.author
        elif user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "anime marry"
           
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
    
        embed=discord.Embed(title=f"{ctx.author.name} married {user.name} !! Congratulations to the newly weds",color = discord.Colour.purple())
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)    

    @commands.command(aliases=["Love"])
    async def love(self,ctx,user:discord.Member=None):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            user = original.author
        elif user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        if user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "anime love"
           
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,50)
        url = data['results'][randomgif]["media_formats"]['gif']['url']    
       
        embed=discord.Embed(title=f"{ctx.author.name} sends love to {user.name}",color = discord.Colour.purple())
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed) 

    @commands.command(aliases=["Nom","NOM"])
    async def nom(self,ctx,user:discord.Member=None):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            user = original.author
        elif user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        
        embed=discord.Embed(title=f"{ctx.author.name} noms on {user.name} !!",color = discord.Colour.purple())
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "anime bite"  
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)    

    @commands.command(aliases=["bites","biting"])
    async def bite(self,ctx,user:discord.Member=None):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            user = original.author
        elif user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        
        embed=discord.Embed(title=f"{ctx.author.name} is biting {user.name} !!",color = discord.Colour.purple())
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "animal bite"  
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)          

    @commands.command(aliases=["Punch",'punching'])
    async def punch(self,ctx,user:discord.Member=None):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            user = original.author
        elif user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        
        embed=discord.Embed(title=f"{ctx.author.name} punches {user.name} hard!",color = discord.Colour.purple())
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "punch"  
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed) 

    @commands.command(aliases=["STFU","shut","shutup","Shut"])
    async def stfu(self,ctx,user:discord.Member=None):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            user = original.author
        elif user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot and m.id != 530824411759116288]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        
        embed=discord.Embed(title=f"{ctx.author.name} is telling {user.name} to STFU !",color = discord.Colour.purple())
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "shut up"  
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)       

    @commands.command(aliases=["sipping","slurp","sips","Sip"])
    async def sip(self,ctx):
       
        embed=discord.Embed(title=f" {ctx.author.name} is slurping their drink",color = discord.Colour.purple())
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "sip"  
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)

    @commands.command(aliases=["bore","boring"])
    async def bored(self,ctx,user:discord.Member=None):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            user = original.author
            embed=discord.Embed(title=f"{ctx.author.name} is bored of {user.name}",color = discord.Colour.purple())
        elif user == None:
            embed=discord.Embed(title=f"{ctx.author.name} is bored",color = discord.Colour.purple())
        else:
            embed=discord.Embed(title=f"{ctx.author.name} is bored of {user.name}",color = discord.Colour.purple())    
        if user!=None and user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return 
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "bored"  
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)     

    @commands.command(aliases=["smirking","smirks"])
    async def smirk(self,ctx,user:discord.Member=None):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            user = original.author
            embed=discord.Embed(title=f"{ctx.author.name} is smirking at {user.name}",color = discord.Colour.purple())
        elif user == None:
            embed=discord.Embed(title=f"{ctx.author.name} is smirking ",color = discord.Colour.purple())
        else:
            embed=discord.Embed(title=f"{ctx.author.name} is smirking at {user.name}",color = discord.Colour.purple())    
        if user!=None and user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return 
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "smirk"  
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)

    @commands.command()    
    async def beetle(self,ctx):
        randomgifs = [
            "https://media.discordapp.net/attachments/1035565430422642718/1054488247415341239/beetle7.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054488247763472484/beetle6.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054488248111607908/beetle5.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054488248434556948/beetle4.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054488248761716838/beetle3.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054488249084686407/beetle1.gif",
            "https://media.discordapp.net/attachments/1035565430422642718/1054488249420218440/beetle.gif"
        ]
        embed=discord.Embed(title=f"{ctx.author.name} is average Beetle enjoyer",color = discord.Colour.purple())    
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)

    @commands.command(aliases=["Cuddle","cuddles",'cuddling'])
    async def cuddle(self,ctx,user:discord.Member=None):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            user = original.author
        elif user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        
        embed=discord.Embed(title=f"{ctx.author.name} is cuddling {user.name} !",color = discord.Colour.purple())
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "anime cuddle"  
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed) 

    @commands.command(aliases=["Sit",'sitting'])
    async def sit(self,ctx,user:discord.Member=None):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            user = original.author
        elif user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        embed=discord.Embed(title=f"{ctx.author.name} sits on {user.name} and crushes them!",color = discord.Colour.purple())
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "anime sit"  
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)     

    @commands.command(aliases=["Slap"])
    async def slap(self,ctx,user:discord.Member=None):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            user = original.author
        elif user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        
        embed=discord.Embed(title=f"{ctx.author.name} has slapped {user.name}!",color = discord.Colour.purple())
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "slap"  
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)

    @commands.command(aliases=["Spank","SPANK","spanking","Spanking"])
    async def spank(self,ctx,user:discord.Member=None):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            user = original.author
        elif user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        
        embed=discord.Embed(title=f"{ctx.author.name} is spanking {user.name} !",color = discord.Colour.purple())
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "anime spank"  
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)     

    @commands.command(aliases=["Spit"])
    async def spit(self,ctx,user:discord.Member=None):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            user = original.author
        elif user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        
        embed=discord.Embed(title=f"{ctx.author.name} is spitting on {user.name} !",color = discord.Colour.purple())
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "spit"  
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)        

    @commands.command(aliases=["Threaten","THREATEN",'threat'])
    async def threaten(self,ctx,user:discord.Member=None):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            user = original.author
        elif user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        embed=discord.Embed(title=f"{ctx.author.name} is threating {user.name}'s e-life !",color = discord.Colour.purple())
        embed.add_field(name= "Aftermath",value=f"{user.name} is very scared now and won't be able to log in again")
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "threaten"  
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)          
        

    @commands.command(aliases=["Fight",'fighting','fights'])
    async def fight(self,ctx,user:discord.Member=None):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            user = original.author
        elif user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return    
        embed=discord.Embed(title=f"{user.name} and {ctx.author.name} are fighting !",color = discord.Colour.purple())    
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "fight"  
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)  

    @commands.command(aliases=["Judge","JUDGE",'judging','Judging'])
    async def judge(self,ctx,user:discord.Member=None):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            user = original.author
        elif user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        embed=discord.Embed(title=f"{ctx.author.name} is judging {user.name} hard",color = discord.Colour.purple())
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "judging"  
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)          

    @commands.command(aliases=["winking","winks"])
    async def wink(self,ctx,user:discord.Member=None):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            user = original.author
            embed=discord.Embed(title=f"{ctx.author.name} is winking at {user.name}",color = discord.Colour.purple())
        elif user == None:
            embed=discord.Embed(title=f"{ctx.author.name} is winking",color = discord.Colour.purple())
        else:
            embed=discord.Embed(title=f"{ctx.author.name} is winking at {user.name}",color = discord.Colour.purple())    
        if user!=None and user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return 
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "wink"  
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)          

    @commands.command(aliases=["Tickle","Tick"])
    async def tickle(self,ctx,user:discord.Member=None):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            user = original.author
        elif user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        embed=discord.Embed(title=f"{ctx.author.name} is tickling {user.name} ! hehe",color = discord.Colour.purple())
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "tickle"  
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)          

    @commands.command(aliases=["tg","touchg",'tgrass','touch'])
    async def touchgrass(self,ctx,user:discord.Member=None):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            user = original.author
        elif user == None:
            embed=discord.Embed(title=f"{ctx.author.name} is touching grass!",color = discord.Colour.purple())
        else:
            embed=discord.Embed(title=f"{ctx.author.name} is telling {user.name} to touch grass",color = discord.Colour.purple())    
        if user!=None and user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return 
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "touch grass"  
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)          

    @commands.command(aliases=["twerking","twerks"])
    async def twerk(self,ctx,user:discord.Member=None):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            user = original.author
            embed=discord.Embed(title=f"{ctx.author.name} is twerking for{user.name}",color = discord.Colour.purple()) 
        elif user == None:
            embed=discord.Embed(title=f"{ctx.author.name} is twerking!",color = discord.Colour.purple())
        else:
            embed=discord.Embed(title=f"{ctx.author.name} is twerking for{user.name}",color = discord.Colour.purple())    
        if user!=None and user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return 
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "anime twerk"  
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)   

    @commands.command(aliases=["waving","Wave","Waving"])
    async def wave(self,ctx,user:discord.Member=None):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            user = original.author
            embed=discord.Embed(title=f"{ctx.author.name} waves at {user.name}",color = discord.Colour.purple()) 
        elif user == None:
            embed=discord.Embed(title=f"{ctx.author.name} is waving",color = discord.Colour.purple())
        else:
            embed=discord.Embed(title=f"{ctx.author.name} waves at {user.name}",color = discord.Colour.purple())    
        if user!=None and user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return 
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "waving"  
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)  

    @commands.command(aliases=["hf","Hf","highfiving",'highf','hfive'])
    async def highfive(self,ctx,user:discord.Member=None):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            user = original.author
        elif user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
       
        embed=discord.Embed(title=f"{ctx.author.name} is high fiving {user.name} !",color = discord.Colour.purple())
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "high five"  
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)   

    @commands.command(aliases=["yawning","yawns"])
    async def yawn(self,ctx,user:discord.Member=None):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            user = original.author
            embed=discord.Embed(title=f"{ctx.author.name} is yawning because of {user.name}",color = discord.Colour.purple()) 
        elif user == None:
            embed=discord.Embed(title=f"{ctx.author.name} is yawning ",color = discord.Colour.purple())
        else:
            embed=discord.Embed(title=f"{ctx.author.name} is yawning because of {user.name}",color = discord.Colour.purple())    
        if user!=None and user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return 
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "yawn"  
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)  

    @commands.command(aliases=["vibing","Vibe","Vibing"])
    async def vibe(self,ctx,user:discord.Member=None):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            user = original.author
            embed=discord.Embed(title=f"{user.name} and {ctx.author.name} are vibing",color = discord.Colour.purple())
        elif user == None:
            embed=discord.Embed(title=f"{ctx.author.name} is vibing",color = discord.Colour.purple())
        else:
            embed=discord.Embed(title=f"{user.name} and {ctx.author.name} are vibing",color = discord.Colour.purple())    
        if user!=None and user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return 
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "vibing"  
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)  

    @commands.command(aliases=["staring","stares"])
    async def stare(self,ctx,user:discord.Member=None):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            user = original.author
            embed=discord.Embed(title=f"{ctx.author.name} is staring at {user.name}",color = discord.Colour.purple())
        elif user == None:
            embed=discord.Embed(title=f"{ctx.author.name} is staring",color = discord.Colour.purple())
        else:
            embed=discord.Embed(title=f"{ctx.author.name} is staring at {user.name}",color = discord.Colour.purple())    
        if user!=None and user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return 
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "stare"  
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)     

    @commands.command(aliases=["dancing","dances"])
    async def dance(self,ctx,user:discord.Member=None):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            user = original.author
            embed=discord.Embed(title=f"{user.name} and {ctx.author.name} are dancing",color = discord.Colour.purple())   
        elif user == None:
            embed=discord.Embed(title=f"{ctx.author.name} is dancing",color = discord.Colour.purple())
        else:
            embed=discord.Embed(title=f"{user.name} and {ctx.author.name} are dancing",color = discord.Colour.purple())    
        if user!=None and user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return 
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "dance"  
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)

    @commands.command(aliases=["shocking","shocked"])
    async def shock(self,ctx,user:discord.Member=None):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            user = original.author
            embed=discord.Embed(title=f"{ctx.author.name} is shocked at {user.name}'s actions",color = discord.Colour.purple())
        elif user == None:
            embed=discord.Embed(title=f"{ctx.author.name} is shocked!",color = discord.Colour.purple())
        else:
            embed=discord.Embed(title=f"{ctx.author.name} is shocked at {user.name}'s actions",color = discord.Colour.purple())    
        if user!=None and user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return 
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "shock"  
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)  

    @commands.command(aliases=["licks",'licking'])
    async def lick(self,ctx,user:discord.Member=None):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            user = original.author
        elif user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
       
        embed=discord.Embed(title=f"{ctx.author.name} is licking {user.name} !",color = discord.Colour.purple())
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "anime lick"  
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)       

    @commands.command(aliases=["pokes",'poking'])
    async def poke(self,ctx,user:discord.Member=None):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            user = original.author
        elif user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
       
        embed=discord.Embed(title=f"{ctx.author.name} is poking {user.name} !",color = discord.Colour.purple())
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "anime poke"  
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)     

    @commands.command(aliases=["deals"])
    async def deal(self,ctx,user:discord.Member=None):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            user = original.author
        elif user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
       
        embed=discord.Embed(title=f"{ctx.author.name} just signed a deal with {user.name} !",color = discord.Colour.purple())
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "anime deal"  
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)   

    @commands.command(aliases=["farting","farts"])
    async def fart(self,ctx,user:discord.Member=None):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            user = original.author
            embed=discord.Embed(title=f"{ctx.author.name} is farting in {user.name}'s face ",color = discord.Colour.purple())
        elif user == None:
            embed=discord.Embed(title=f"{ctx.author.name} is farting ",color = discord.Colour.purple())
        else:
            embed=discord.Embed(title=f"{ctx.author.name} is farting in {user.name}'s face ",color = discord.Colour.purple())    
        if user!=None and user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return 
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "fart"  
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)  

    @commands.command(aliases=["fp","facep"])
    async def facepalm(self,ctx,user:discord.Member=None):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            user = original.author
            embed=discord.Embed(title=f"{ctx.author.name} facepalmed because of {user.name}",color = discord.Colour.purple())
        elif user == None:
            embed=discord.Embed(title=f"{ctx.author.name} is facepalming ",color = discord.Colour.purple())
        else:
            embed=discord.Embed(title=f"{ctx.author.name} facepalmed because of {user.name}",color = discord.Colour.purple())    
        if user!=None and user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return 
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "facepalm"  
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)     

    @commands.command(aliases=["Fake"])
    async def fake(self,ctx,user:discord.Member=None):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            user = original.author
        elif user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
       
        embed=discord.Embed(title=f"{ctx.author.name} is calling {user.name} fake !",color = discord.Colour.purple())
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "fake"  
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)        

    @commands.command()
    async def hurt(self,ctx,user:discord.Member=None):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            user = original.author
            embed=discord.Embed(title=f"{user.name} deeply hurt {ctx.author.name}",color = discord.Colour.purple())    
        elif user == None:
            embed=discord.Embed(title=f"{ctx.author.name} is hurt ",color = discord.Colour.purple())
        else:
            embed=discord.Embed(title=f"{user.name} deeply hurt {ctx.author.name}",color = discord.Colour.purple())    
        if user!=None and user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return 
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "hurt"  
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)   

    @commands.command()
    async def bitch(self,ctx,user:discord.Member=None):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            user = original.author
        elif user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
       
        embed=discord.Embed(title=f"{ctx.author.name} is calling {user.name} a fucking bitch !",color = discord.Colour.purple())
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "bitch"  
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)  

    @commands.command(aliases=['eyer','eroll'])
    async def eyeroll(self,ctx,user:discord.Member=None):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            user = original.author
            embed=discord.Embed(title=f"{ctx.author.name} is rolling their eyes at {user.name}",color = discord.Colour.purple()) 
        elif user == None:
            embed=discord.Embed(title=f"{ctx.author.name} is rolling their eyes ",color = discord.Colour.purple())
        else:
            embed=discord.Embed(title=f"{ctx.author.name} is rolling their eyes at {user.name}",color = discord.Colour.purple())    
        if user!=None and user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return 
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "eye roll"  
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)  

    @commands.command()
    async def smack(self,ctx,user:discord.Member=None):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            user = original.author
        elif user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
       
        embed=discord.Embed(title=f"{ctx.author.name} smacked {user.name}",color = discord.Colour.purple())
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "smack"  
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)   

    @commands.command()
    async def bow(self,ctx,user:discord.Member=None):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            user = original.author
        elif user == None:
            humans = [m for m in ctx.guild.members if m != ctx.author and not m.bot]
            user = random.choice(humans)
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
       
        embed=discord.Embed(title=f"{ctx.author.name} is bowing to {user.name}",color = discord.Colour.purple())
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "bow"  
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed) 
    
    @commands.command()
    async def sleep(self,ctx):
        embed=discord.Embed(title=f"{ctx.author.name} is sleepy",color = discord.Colour.purple())
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "sleep"  
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed) 
    
    @commands.command()
    async def tired(self,ctx):
        embed=discord.Embed(title=f"{ctx.author.name} is tired af",color = discord.Colour.purple())
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "tired"  
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)   

    @commands.command()
    async def run(self,ctx,user:discord.Member=None):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            user = original.author
            embed=discord.Embed(title=f"{ctx.author.name} is running away from {user.name}",color = discord.Colour.purple()) 
        elif user == None:
            embed=discord.Embed(title=f"{ctx.author.name} is running",color = discord.Colour.purple())
        else:
            embed=discord.Embed(title=f"{ctx.author.name} is running away from {user.name}",color = discord.Colour.purple())    
        if user!=None and user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return 
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "run"  
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed) 

    @commands.command()
    async def ew(self,ctx,user:discord.Member=None):
        if ctx.message.reference:
            original = await ctx.fetch_message(ctx.message.reference.message_id)
            user = original.author
            embed=discord.Embed(title=f"{ctx.author.name} is repulsed by {user.name}",color = discord.Colour.purple()) 
        elif user == None:
            embed=discord.Embed(title=f"{ctx.author.name} is repulsed",color = discord.Colour.purple())
        else:
            embed=discord.Embed(title=f"{ctx.author.name} is repulsed by {user.name}",color = discord.Colour.purple())    
        if user!=None and user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return 
        KEY = "AIzaSyBWKLC74AeG_xh_QPN37y9aJoIznvQ2KBk"  # click to set to your apikey
        lmt = 50
        ckey = "test" 
        searchTerm = "ew"  
        r = requests.get(f"https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" %(searchTerm, KEY, ckey,  lmt))
        data = r.json()
        randomgif = random.randint(0,49)
        url = data['results'][randomgif]["media_formats"]['gif']['url']
        embed.set_image(url = url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)     

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(interaction(bot))       
    print("block, bonk, cheer, choke, cope, cry ,eat, blush, fuck, kiss, beetle, kill, laugh, lie, miss ,hug, boop, pat, pf, pinch, pray, salute , marry, love, nom, punch, shut, sip, bored ,smirk, cuddle, sit, slap, spank, spit ,threaten, fight, judge, wink, tickle, touch ,twerk ,wave, highfive, yawn, vibe, stare, dance ,shock ,lick, poke, deal, facepalm, fake, fart, hurt, bitch, eyeroll, smack, bow, run, ew is loaded")    
       
        
   
