import os
import asyncio
import discord
from dotenv.main import load_dotenv
from discord.ext import commands
from discord.ext.commands import Bot
from discord import app_commands
import random
from random import choice
from discord import interactions
from discord.ext.commands import has_permissions,CheckFailure


def main():
    load_dotenv()

    token = "MTA0Mzg1ODk0MDk5MzIyODgwMA.Gm_EjW.NqIKfa5fplbIlTHi1PPzOPHL3xWudW6sroqW5s"
    intents = discord.Intents.all()
    intents.members = True

    bot = commands.Bot(intents= intents, command_prefix= ["k!","K!"] , description='Cute Kirby!',activity = discord.Game(name="Super Smash Bros"))

    @bot.event
    async def on_ready():
        print(f"{bot.user.name} has Connected")  
        try:
            synced = await bot.tree.sync()
            print(f"Synced {len(synced)} commands")
        except Exception as e:
            print(e)

    @bot.command()
    async def ping(ctx):
        """Checks for a response from the bot"""
        await ctx.send("Pong")   
    

    class MyHelp(commands.HelpCommand):
        async def send_bot_help(self, mapping):
            embed = discord.Embed(title="Help", description = "Bot Commands ",color = discord.Colour.purple())
            embed.add_field(name="User Commands", value = "avatar, ,guild_avatar, banner, serverinfo ,userinfo",inline=False)
            embed.add_field(name="Fun Commands",value = "choose, say(also a slash command /say), repeat ", inline=False)
            embed.add_field(name= "Interaction Command", value = "block, bonk, choke, cope, cry, crying, eating, fuck, hug, kill, kiss, laugh, love, marry, missing, nom, pat, ,pillowfight, pinch, punch, realkiss, sit, slap, spit, tickle, vibe, wave",inline=False)
            await self.context.send(embed=embed)

        async def block(self, command):
            embed = discord.Embed(title="Block",description= "Pretend to block a user with this interaction",color = discord.Colour.purple())
            await self.context.send(embed=embed)    

    @bot.tree.command(name="dice")
    async def dice(interaction:discord.Interaction,num:int):
        if num==6 or num==12:
            await interaction.response.send_message(f"{random.randint(1,int(num))}")       
        else:
            await interaction.response.send_message("Invalid Choice = Choose between 6 or 12")    



    @bot.tree.command(name="say")
    async def imitate(interaction: discord.Interaction,say:str,member:discord.Member):
        webhook = await interaction.channel.create_webhook(name=member.name)
        await webhook.send(str(say), username=member.display_name, avatar_url=member.display_avatar.url)

        webhooks = await interaction.channel.webhooks()
        for webhook in webhooks:
            await webhook.delete()

    @bot.command(aliases=["Say"])
    async def say(ctx, member: discord.Member, *, message=None):
        if message == None:
            await ctx.send('provide a message with that!')
            return

        webhook = await ctx.channel.create_webhook(name=member.name)
        await webhook.send(str(message), username=member.name, avatar_url=member.avatar.url)

        webhooks = await ctx.channel.webhooks()
        for webhook in webhooks:
            await webhook.delete()
        
    @bot.command(aliases=["SI","si"])
    async def serverinfo(ctx):
        members = len(ctx.guild.members)
        Roles = len(ctx.guild.roles)
        embed=discord.Embed(title=f"***Server Information***",color = discord.Colour.purple() )    
        embed.add_field(name='Name:', value=ctx.guild.name, inline=False)
        embed.add_field(name='ID:', value=ctx.guild.id, inline=False)
        embed.add_field(name='Owner:', value=ctx.guild.owner.name, inline=False)
        embed.add_field(name='Created At:', value=ctx.guild.created_at.strftime('Day: %d/%m/%Y Hour: %H:%M:%S %p'), inline=False)
        gc= 0
        bc = 0
        for member in ctx.guild.members:
            if member.bot == False:
                gc += 1
            else:
                bc+=1    
        embed.add_field(name="Total Member Count",value = f"The total headcount in this server is {ctx.guild.member_count}", inline=False)
        embed.add_field(name="Member Count",value = f"There are a total of {gc} members in this server", inline=False)
        embed.add_field(name="Bot Count",value = f"There are a total of {bc} bots in this server",inline=False)
        await ctx.send(embed=embed)         
    
    @bot.tree.command(name="serverinfo")
    async def si(interaction: discord.Interaction):
        members = len(interaction.guild.members)
        Roles = len(interaction.guild.roles)
        embed=discord.Embed(title=f"***Server Information***",color = discord.Colour.purple() )    
        embed.add_field(name='Name:', value=interaction.guild.name, inline=False)
        embed.add_field(name='ID:', value=interaction.guild.id, inline=False)
        embed.add_field(name='Owner:', value=interaction.guild.owner.name, inline=False)
        embed.add_field(name='Created At:', value=interaction.guild.created_at.strftime('Day: %d/%m/%Y Hour: %H:%M:%S %p'), inline=False)
        gc= 0
        bc = 0
        for member in interaction.guild.members:
            if member.bot == False:
                gc += 1
            else:
                bc+=1    
        embed.add_field(name="Total Member Count",value = f"The total headcount in this server is {interaction.guild.member_count}", inline=False)
        embed.add_field(name="Member Count",value = f"There are a total of {gc} members in this server", inline=False)
        embed.add_field(name="Bot Count",value = f"There are a total of {bc} bots in this server",inline=False)
        await interaction.response.send_message(embed=embed)   


    @bot.command(aliases=["useri","ui"])
    async def userinfo(ctx,member:discord.Member=None):
        if member == None:
            member = ctx.message.author
        roles = [role for role in member.roles]
        embed=discord.Embed(title=f"***User Information***",color = discord.Colour.purple(),timestamp = ctx.message.created_at)   
        embed.add_field(name = "Name",value = member,inline=False) 
        embed.add_field(name = "ID",value = member.id,inline=False) 
        embed.add_field(name = "Nickname",value = member.display_name,inline=False)
        embed.add_field(name = "Status",value = member.status,inline=False)
        embed.add_field(name = "Created At",value = member.created_at.strftime("Day: %d/%m/%Y Hour: %H:%M:%S %p"),inline=False)
        embed.add_field(name = "Joined At",value = member.joined_at.strftime("Day: %d/%m/%Y Hour: %H:%M:%S %p"),inline=False) 
        embed.add_field(name = f" Total Roles ({len(roles)})",value = " ".join([role.mention for role in roles])) 
        embed.set_thumbnail(url = member.avatar.url)
        await ctx.send(embed=embed)

    @bot.command()
    async def choose(ctx, *choices: str):
        """Choose between the choices given by the user for example
        k!choose 1 2 3 """
        await ctx.send(random.choice(choices)) 
    
    
    @bot.command()
    async def repeat(ctx, times: int, *content:str):
        """Repeats whatever the user has typed 
        k!repeat 2 hi"""
        if 0<times<=5:
            for i in range(times):
                await ctx.send(" ".join(content)) 
        else:
            embed = discord.Embed(color = discord.Colour.purple(),description="Kirby is not a fool and won't spam the chat")
            embed.set_image(url ="https://media.discordapp.net/attachments/1042790120652275853/1045611042228666408/kirby-mad.gif")
            await ctx.send(embed=embed)

    @bot.command(aliases=["av","a"])
    async def avatar(ctx, *,  avamember : discord.Member=None):
        test = discord.Embed(title=f"<:kirby_thumbsup:1034765537185632276>  {avamember.name}'s Avatar",color = discord.Colour.purple())
        test.set_author(name=avamember.name, icon_url=avamember.avatar.url)
        test.set_image(url=avamember.avatar.url)
        await ctx.send(embed=test)

    @bot.tree.command(name="avatar")
    async def avatar(interaction: discord.Interaction,user:discord.Member=None):
        test = discord.Embed(title=f"<:kirby_thumbsup:1034765537185632276>  {user.name}'s Avatar",color = discord.Colour.purple())
        test.set_author(name=user.name, icon_url=user.avatar.url)
        test.set_image(url=user.avatar.url)
        await interaction.response.send_message(embed=test)

    @bot.tree.command(name="guild_avatar")
    async def guild_avatar(interaction: discord.Interaction,user:discord.Member=None):
        test = discord.Embed(title=f"<:kirby_thumbsup:1034765537185632276>  {user.name}'s Avatar",color = discord.Colour.purple())
        test.set_author(name=user.name, icon_url=user.avatar.url)
        test.set_image(url=user.display_avatar.url)
        await interaction.response.send_message(embed=test)    


    @bot.command()
    async def banner(ctx, user:discord.Member = None):
        if not user:
            user = ctx.author
        user = await bot.fetch_user(user.id)  
        if user.banner:
            embed = discord.Embed(title = f"<:kirby_thumbsup:1034765537185632276>  {user.name}'s Banner",color = discord.Colour.purple())
            embed.set_author(name=user.name,icon_url=user.avatar.url)
            embed.set_image(url = user.banner.url)
            await ctx.send(embed=embed)
        else:
            await ctx.send(f'<a:idlekirby:1039819001380995122> this user has no banner')

    @bot.tree.command(name="banner")
    async def banner(interaction, user:discord.Member = None):
        if not user:
            user = interaction.author
        user = await bot.fetch_user(user.id)  
        if user.banner:
            embed = discord.Embed(title = f"<:kirby_thumbsup:1034765537185632276>  {user.name}'s Banner",color = discord.Colour.purple())
            embed.set_author(name=user.name,icon_url=user.avatar.url)
            embed.set_image(url = user.banner.url)
            await interaction.response.send_message(embed=embed)
        else:
            await interaction.response.send_message(f'<a:idlekirby:1039819001380995122> this user has no banner')        
    
    
    
    @bot.command(aliases=["Slap"])
    async def slap(ctx,user:discord.Member=None):
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        if user == None:
            humans = [m for m in ctx.guild.members if not m.bot]
            user = random.choice(humans)
        randomgifs = [
            "https://media.discordapp.net/attachments/1045618240900050954/1045655137953263696/kirby-king-dedede.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1045655292773400596/Punishment_Spanked_Sticker_-_Punishment_Spanked_Booty_Slap_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1045656005356310558/WiffleGif.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1045657796986802217/kirboslapping.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046388711555870720/will-smith-will-smith-slap.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046388714768707645/40fa327344c9a71783b1cd77afa19ac9.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046388727225782313/4ec47d7b87a9ce093642fc8a3c2969e7.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046388736755253278/slapping.gif"
        ]
        embed=discord.Embed(title=f"{ctx.author.name} has slapped {user.name}!",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)

    @bot.command(aliases=["Kiss"])
    async def kiss(ctx,user:discord.Member=None):
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        if user == None:
            humans = [m for m in ctx.guild.members if not m.bot]
            user = random.choice(humans)
        randomgifs = [
            "https://media.discordapp.net/attachments/1045618240900050954/1045658804034994226/0d095e578f2c91ad060fada5cde2fd4ebf6f9d18r1-450-375_hq.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1045659012743561316/kirby-kiss.gif",
            "https://cdn.weasyl.com/static/media/bf/d3/6d/bfd36da752a5cfdf862b01ebb4db652308807f907677e1cc0167d20dabc17b94.gif",
            "https://media.discordapp.net/attachments/1005851300195487875/1045660804852240455/IMG_9527.gif",
            "https://media.discordapp.net/attachments/1005851300195487875/1045660805162598422/IMG_9528.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046363447660654632/Kuzu_No_Honkai_Anime_GIF_-_Kuzu_No_Honkai_Anime_Kiss_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046363448029741056/Cute_Blow_Kiss_GIF_-_Cute_Blow_Kiss_Hearts_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046363448633733140/Tuagom_Puffybear_GIF_-_Tuagom_Puffybear_Exercise_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046363448960876596/Kissykissy_GIF_-_Kissykissy_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046363449267068998/Bear_Angry_GIF_-_Bear_Angry_Kiss_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046363449611005962/Smoochie_Smooches_Sticker_-_Smoochie_Smooches_Kisses_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046363449908789258/Animated_Kiss_Gif_Images.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046363450244341800/Milk_And_Mocha_Bear_Kiss_GIF_-_Milk_And_Mocha_Bear_Kiss_-_Discover__Share_GIFs.gif"
        ]
        embed=discord.Embed(title=f"{ctx.author.name} has kissed {user.name}",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)

    @bot.command(aliases=["Realkiss","RealKiss","REALKISS","RK","rk"])
    async def realkiss(ctx,user:discord.Member=None):
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        if user == None:
            humans = [m for m in ctx.guild.members if not m.bot]
            user = random.choice(humans)
        randomgifs = [
            "https://media.discordapp.net/attachments/1005851300195487875/1045660381525331978/IMG_9526.gif",
            "https://media.discordapp.net/attachments/1005851300195487875/1045660805510742076/IMG_9529.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046362820914188328/Black_And_White_GIF_-_Find__Share_on_GIPHY.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046362821295886367/File_Stefan-Elena-stefan-and-elena-32515768-500-265-1-_gif.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046362821627224094/Kiss_Couple_GIF_-_Kiss_Couple_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046362822088593409/Kisses_Stupid_Love_GIF_-_Kisses_Kiss_Stupid_Love_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046362822503845909/Kiss_Couple_GIF_-_Kiss_Couple_Romance_-_Discover__Share_GIFs.gif"
        ]
        embed=discord.Embed(title=f"{ctx.author.name} has kissed {user.name} hard",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)

    @bot.command(aliases=["Fuck"])
    async def fuck(ctx,user:discord.Member=None):
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        randomgifs = [
            "https://media.discordapp.net/attachments/1045618240900050954/1045661560326078535/how-did-they-how-did.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1045661934776754217/8768f928-3eb6-4254-9ffc-a378608a0fa8_text.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1045663257639272468/5kozue.jpg",
            "https://media.discordapp.net/attachments/1045618243013984296/1046475203296890900/caught-in.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046475208497844306/des2g4q-66b842d0-5e2b-4022-ae1e-41bb56bd77db.jpg?width=575&height=606",
            "https://media.discordapp.net/attachments/1045618243013984296/1046475214000754768/94aba787a7c7cab988321e224957e9c6c1f0db1ad92100eeef52232048ddb3ff_1.jpg?width=663&height=607",
            "https://media.discordapp.net/attachments/1045618243013984296/1046475215296798882/c411e4e207c54d2d5705fe8df09efd02f02614c395103128081c56b97d8a8d1c_1.jpg?width=485&height=606",
            "https://media.discordapp.net/attachments/1045618243013984296/1046475224360685608/ceeef3dc54fee1701d3331b48f948bacc0d1329ec436c6c4750bc6e67942213e_1.jpg"
        ]
        embed=discord.Embed(title=f"{ctx.author.name} tried to e-fuck {user.name} and were caught in 4k",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)   

    @bot.command(aliases=["Hug"])
    async def hug(ctx,user:discord.Member=None):
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        if user == None:
            humans = [m for m in ctx.guild.members if not m.bot]
            user = random.choice(humans)
        randomgifs = [
            "https://media.discordapp.net/attachments/1045618240900050954/1045663962882134066/kirby-hug.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1045663980926029834/super-smash-bros-kirby.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1045666359662616627/a57a2cafc38622f62edecb82be278973.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046476088014020779/cute.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046476097597997146/polar-bear.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046476108192813137/dc6df1c-7186e0ed-c0e3-4940-8b2c-7a5707f1ad7e.gif?width=606&height=606",
            "https://media.discordapp.net/attachments/1045618243013984296/1046476112441651251/ddu4ws4-0d31ccf4-d249-4a23-86b3-3d42b7311307.gif?width=1083&height=607",
            "https://media.discordapp.net/attachments/1045618243013984296/1046476124143747142/200w_1.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046476125502713876/giphy_3.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046476787791708200/download_3.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046476788118859876/Tkthao219_Bubududu_Sticker_-_Tkthao219_Bubududu_Peach_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046476788471169034/Tuagom_Puffy_Bear_GIF_-_Tuagom_Puffy_Bear_Kiss_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046476788907393034/Mochi_Cat_Kiss_GIFs___Tenor.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046476789318430801/download_2.gif?width=606&height=606",
            "https://media.discordapp.net/attachments/1045618243013984296/1046476790807412896/download_1.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046476790522183690/Animated_Love_GIF_-_Animated_Love_Hug_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046476790140514355/Hugging_Cat_GIF_-_Hugging_Cat_Couples_-_Discover__Share_GIFs.gif"
        ]
        embed=discord.Embed(title=f"{ctx.author.name} hugs {user.name}",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed) 

    @bot.command(aliases=["Love"])
    async def love(ctx,user:discord.Member=None):
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        if user == None:
            humans = [m for m in ctx.guild.members if not m.bot]
            user = random.choice(humans)
        randomgifs = [
            "https://media.discordapp.net/attachments/1045618240900050954/1045664205388398643/love-kirby.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046156748983124050/love-gif.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046156765412200528/icegif-876.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046156775352713326/icegif-592.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046156785515495504/icegif-581.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046157241130156102/DarlingRectangularIsabellinewheatear-max-1mb.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046157205617004594/cute-love.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046157189548609546/WindingShorttermAfricanharrierhawk-size_restricted.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046157176118456441/bunny-rabbit.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046363448302379068/Muddu_Love_Sticker_-_Muddu_Love_Heart_-_Discover__Share_GIFs.gif"
        ]
        embed=discord.Embed(title=f"{ctx.author.name} sends love to {user.name}",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)

    @bot.command(aliases=["Missing"])
    async def missing(ctx,user:discord.Member=None):
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        if user == None:
            humans = [m for m in ctx.guild.members if not m.bot]
            user = random.choice(humans)
        randomgifs = [
            "https://media.discordapp.net/attachments/949680123869814794/1045693438982619146/miss-you-shy-bear-wgvvsi8epdvui25t.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1045693439276236810/b5395bd842e048cd00cc021b50c37ba6.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1045693439574024282/missing-you-badly-waiting.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046155561265287188/7fd9ff3c81c5ea8cf317c05794a22363.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046155628684525698/dog-triste.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046155851494326372/i-miss-you-so-much-i-miss-you.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046155978267164692/SjOp.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046156399069102090/i-miss-you-bear-crying-d9eflc3t9immbccm.gif"
        ]
        embed=discord.Embed(title=f"{ctx.author.name} is missing {user.name}",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)  
    @bot.command(aliases=["Tickle","Tick"])
    async def tickle(ctx,user:discord.Member=None):
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        if user == None:
            humans = [m for m in ctx.guild.members if not m.bot]
            user = random.choice(humans)
        randomgifs = [
            "https://media.discordapp.net/attachments/1045618240900050954/1046100540821610516/91a686f18ccc56616078a25bb55bfed9.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046100541475930112/tickle-feet.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046100541152964638/giphy_5.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046153500029100043/bae.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046154095213420564/giphy_6.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046154459635527710/6VniMLU.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046154782680813578/aaaaaaaahahahah-tickling-is-awesome.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046154913308221540/371fa72fcc90fc98902266fa258718c3.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046155310815002654/butt-tickles.gif"
        ]
        embed=discord.Embed(title=f"{ctx.author.name} is tickling {user.name} ! hehe",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)
        
    @bot.command(aliases=["Spit"])
    async def spit(ctx,user:discord.Member=None):
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        if user == None:
            humans = [m for m in ctx.guild.members if not m.bot]
            user = random.choice(humans)
        randomgifs = [
            "https://media.discordapp.net/attachments/1045618240900050954/1046353978193084426/18s1.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046353997621108806/OnlyDisloyalHare-size_restricted.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046354474748362762/GrouchyCleverGreatdane-size_restricted.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046354573641658418/hasbulla-magomedov-hasbulla.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046354595431067648/giphy.gif"
        ]
        embed=discord.Embed(title=f"{ctx.author.name} is spitting on {user.name} !",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)  
        
    @bot.command(aliases=["Cry"])
    async def cry(ctx,user:discord.Member=None):
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        if user == None:
            humans = [m for m in ctx.guild.members if not m.bot]
            user = random.choice(humans)
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
            "https://media.discordapp.net/attachments/1045618243013984296/1046476117697101926/Cat_Cry_Sticker_-_Cat_Cry_Meme_-_Discover__Share_GIFs.gif"

        ]
        embed=discord.Embed(title=f"{user.name} made {ctx.author.name} cry! Truly a monster",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)   
    
    @bot.command(aliases=["Crying"])
    async def crying(ctx):
        
        randomgifs = [
            "https://media.discordapp.net/attachments/1045618240900050954/1046357237255372840/Kuromi_Crying_GIF_-_Kuromi_Crying_Onegai_My_Melody_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046357237599309824/Anime_Cry_GIF_-_Anime_Cry_Crying_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046357237876138014/Emoji_Crying_GIF_-_Emoji_Crying_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046357238161342514/Sad_Monsters_Inc_GIF_by_filmeditor_-_Find__Share_on_GIPHY.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046474523995820073/woman-crying-hard-lskfg2qn6wo9yiox.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046474547374870528/tumblr_nabqw145or1slmtxco1_500.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046476115964866630/download.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046476116602388490/Sad_The_Simpsons_GIF_-_Find__Share_on_GIPHY.gif"

        ]
        embed=discord.Embed(title=f"{ctx.author.name} is crying",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)   

    @bot.command(aliases=["Choke"])
    async def choke(ctx,user:discord.Member=None):
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        if user == None:
            humans = [m for m in ctx.guild.members if not m.bot]
            user = random.choice(humans)
        randomgifs = [
            "https://media.discordapp.net/attachments/1045618240900050954/1046357753582583838/Kylo_Ren_Star_Wars_GIF_-_Kylo_Ren_Star_Wars_Choke_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046357753905565746/Love_Choked_GIF_-_Love_Choked_Spongebob_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046357754199158814/Homer_Choking_Bart_GIF_-_Simpsons_Angry_Furious_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046357754522107975/Choke_Love_GIF_-_Choke_Love_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046475535770976326/Anime_Choke_GIF_-_Anime_Choke_Hug_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046475536521773147/Margot_Robbie_Choke_GIF_-_Margot_Robbie_Choke_Joker_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046475536916025454/gif.gif"
        ]
        embed=discord.Embed(title=f"{ctx.author.name} is choking {user.name} hard!!",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)   

    @bot.command(aliases=["Eating"])
    async def eating(ctx):
        randomgifs = [
            "https://media.discordapp.net/attachments/1045618240900050954/1046361143976935454/b9a29258-8eb8-4ad4-81a1-ab085059d8af.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046361145553997874/Comendopipoca_GIF_-_Comendopipoca_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046361146485133362/Happy_Spongebob_Squarepants_GIF_-_Find__Share_on_GIPHY.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046361146971668540/Smash_Bros_Eating_GIF_-_Smash_Bros_Eating_Cute_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046361147378520114/Milk_And_Mocha_Gnam_GIF_-_Milk_And_Mocha_Gnam_Omnom_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046361214881632306/eating-food.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046361224247525426/7e7a012b54676d29a26f83e63f860178_w200.gif",
            "https://media.discordapp.net/attachments/1045618240900050954/1046361236574576721/eating-kirby.gif"
        ]
        embed=discord.Embed(title=f"{ctx.author.name} is eating! Yummy food",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)     

    @bot.command(aliases=["Laugh"])
    async def laugh(ctx):
        randomgifs = [
            "https://media.discordapp.net/attachments/1045618243013984296/1046361695561453688/Happy_Cracking_Up_GIF_-_Find__Share_on_GIPHY.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046361695859261490/Minions_Laugh_GIF_-_Minions_Despicable_Me_Laugh_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046361696123506779/Moms_Mabley__The_Dirty_Granny_of_Stand_Up.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046361699881586718/Happy_Laugh_Sticker_-_Happy_Laugh_Funny_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046361700242313286/Celebrity__Entertainment___Chris_Evans_Does_This_1_Thing_Almost_Every_Time_He_Laughs_and_Its_Freakin_Adorable.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046361700598812692/Cracking_Up_Reaction_GIF_-_Find__Share_on_GIPHY.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046361700967923803/33_Random_Pics_To_Amuse_and_Entertain.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046361701295083540/When_someone_suggests_you_should_maybe_give_up_coffee_for_a_week_.gif"
        ]
        embed=discord.Embed(title=f"{ctx.author.name} is laughing! hehehee",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)   

    @bot.command(aliases=["Pinch"])
    async def pinch(ctx,user:discord.Member=None):
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        if user == None:
            humans = [m for m in ctx.guild.members if not m.bot]
            user = random.choice(humans)
        randomgifs = [
            "https://media.discordapp.net/attachments/993633626719780924/1046366440225247252/Milk_And_Mocha_Cheek_GIF_-_Milk_And_Mocha_Cheek_Chubby_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/993633626719780924/1046366440757940234/Little_piece_of_my_life.gif",
            "https://media.discordapp.net/attachments/993633626719780924/1046366441127034931/Squishy_Squishy_GIF_-_Squishy_Kitty_Cat_Cheeks_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/993633626719780924/1046366441424818186/Chubby_Cheeks_Pinch_GIF_-_Chubby_Cheeks_Pinch_Adorable_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/993633626719780924/1046366442049781870/Pull_Pinch_GIF_-_Pull_Pinch_Funny_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/993633626719780924/1046366442557280267/Pull_Pinch_Sticker_-_Pull_Pinch_Mochi_-_Discover__Share_GIFs.gif",
            "https://media.discordapp.net/attachments/993633626719780924/1046366441764573254/Chicken_Bro_Chicken_GIF_-_Chicken_Bro_Chicken_Pinch_-_Discover__Share_GIFs.gif"
        ]
        embed=discord.Embed(title=f"{ctx.author.name} is pinching {user.name} !!",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)          

    @bot.command(aliases=["Pat"])
    async def pat(ctx,user:discord.Member=None):
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        if user == None:
            humans = [m for m in ctx.guild.members if not m.bot]
            user = random.choice(humans)
        randomgifs = [
            "https://media.discordapp.net/attachments/1045618243013984296/1046400910332530698/mala-mishra-jha-pat-head.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046400915663503440/giphy.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046400927076188190/678116d6e7fdbb5275c2d1ca8c938099.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046401319113601125/giphy_1.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046401320745177139/cute-anime-umaru-head-pat-rabcmvfkpeuteckt.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046401334095659068/bunny-cute.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046401338688409630/cd77c5cab311d773ac3846079e483d67_w200.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046401349014802552/pat-cat.gif"
        ]
        embed=discord.Embed(title=f"{ctx.author.name} is patting {user.name} because they are cute!",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)      

    @bot.command(aliases=["Block"])
    async def block(ctx,user:discord.Member=None):
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        if user == None:
            humans = [m for m in ctx.guild.members if not m.bot]
            user = random.choice(humans)
        randomgifs = [
            "https://media.discordapp.net/attachments/1045618243013984296/1046464011241271326/giphy.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046464027955564665/364354045cd96a0726981be285a0ab74.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046465161105522770/critical-bard-cb.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046465161961164850/giphy_1.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046465167048855672/brucevain-blocked.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046465170593034270/giphy_2.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046465187840012288/tumblr_p2yzauQ8lq1qgf1i8o1_500.gif"            
        ]
        embed=discord.Embed(title=f"{ctx.author.name} has blocked {user.name}, They probably deserved it ",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed) 

    @bot.command(aliases=["Cope"])
    async def cope(ctx,user:discord.Member=None):
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        if user == None:
            humans = [m for m in ctx.guild.members if not m.bot]
            user = random.choice(humans)
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

    @bot.command(aliases=["Sit"])
    async def sit(ctx,user:discord.Member=None):
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        if user == None:
            humans = [m for m in ctx.guild.members if not m.bot]
            user = random.choice(humans)
        randomgifs = [
            "https://media.discordapp.net/attachments/1045618243013984296/1046471106657259530/dog-cat.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046471124340453437/200.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046472037327179867/They_cheat_at_staring_contests_.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046472037851463790/Chair_You_Never_Hold_Still.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046473490133426197/Hank_the_Chihuahua_and_Angus_the_Great_Dane_-_DogPerDay.png?width=729&height=606",
            "https://media.discordapp.net/attachments/1045618243013984296/1046473490489954344/Animals_Sitting_on_Capybaras.jpg?width=454&height=606",
            "https://media.discordapp.net/attachments/1045618243013984296/1046473490741592165/brenna-louise.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046473491211362344/Dog_Puppy_GIF_-_Find__Share_on_GIPHY.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046473493480493066/New_Beginnings_66.gif",
            "https://media.discordapp.net/attachments/1045618243013984296/1046473493786656788/download.jpg?width=651&height=606"
             ]
        embed=discord.Embed(title=f"{ctx.author.name} sits on {user.name} and crushes them!",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)           

    @bot.command(aliases=["Punch"])
    async def punch(ctx,user:discord.Member=None):
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        if user == None:
            humans = [m for m in ctx.guild.members if not m.bot]
            user = random.choice(humans)
        randomgifs = [
            "https://media.discordapp.net/attachments/1045618243013984296/1046657546347364432/punch-punching.gif"
        ]
        
        embed=discord.Embed(title=f"{ctx.author.name} punches {user.name} hard!",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)
        

    @bot.command(aliases=["Vibe"])
    async def vibe(ctx):
        randomgifs = [
            "https://media.discordapp.net/attachments/949680123869814794/1046845051109658684/vibe-rabbit.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046845066347548723/teo-cat.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046845070235664465/tumblr_7d502f156e5b5458e8d05495f5936e44_008adab0_500.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046845075684073492/giphy_4.gif"
        ]
        embed=discord.Embed(title=f"{ctx.author.name} is vibing !",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed) 

    @bot.command(aliases=["PillowFight","Pillowfight","pf","PF"])
    async def pillowfight(ctx,user:discord.Member=None):
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        if user == None:
            humans = [m for m in ctx.guild.members if not m.bot]
            user = random.choice(humans)
        randomgifs = [
            "https://media.discordapp.net/attachments/949680123869814794/1046846733818269836/grandparents-day-insomnia.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046846742060081332/pow-pillow-fight.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046846743398072400/edac8fd3339d460f5d609cb738c4d1c5.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046846745943998564/OptimisticPlaintiveAidi-size_restricted.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046846752013164584/733898f1a9d33a3db97fcebbf49dbb82.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046846813648465990/giphy_5.gif"
            ]
        
        embed=discord.Embed(title=f"{ctx.author.name} and {user.name} are pillowfighting !",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed) 

    @bot.command(aliases=["Kill","KILL"])
    async def kill(ctx,user:discord.Member=None):
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        if user == None:
            humans = [m for m in ctx.guild.members if not m.bot]
            user = random.choice(humans)
        randomgifs = [
            "https://media.discordapp.net/attachments/949680123869814794/1046847843597549608/l55gmjfacebook.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046847850849513543/74c150a96ce7654c2131c7095dbfcc52.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046847852615303178/kill-me.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046847859510759494/kill-you-kill.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046847860165066833/giphy_6.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046847872529874944/kill-stab.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046848106035154964/cc87656cf72979fb8ee01c3eebc5cdff.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046848112565694534/among-us-kill-icegif.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046848114419581008/duck-mad.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046848121952542781/69649.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046848137723117618/804e237839129b79dd956eb9c2ec1803.gif"
            ]
        
        embed=discord.Embed(title=f"{ctx.author.name} killed {user.name} ! They definitely won't be able to type again",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)       

    @bot.command(aliases=["Nom","NOM"])
    async def nom(ctx,user:discord.Member=None):
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        if user == None:
            humans = [m for m in ctx.guild.members if not m.bot]
            user = random.choice(humans)
        randomgifs = [
            "https://media.discordapp.net/attachments/949680123869814794/1046876009003225158/sMP.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046876014762008646/45ba063ad9212afec9fed28e79fbfe09.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046876072601456681/PaltryMadKusimanse-max-1mb.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046876072991543408/fe8f2a77e1f3b100e81ee0f1f454542a.gif"
            ]
        
        embed=discord.Embed(title=f"{ctx.author.name} noms on {user.name} !!",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)  

    @bot.command(aliases=["Marry","MARRY"])
    async def marry(ctx,user:discord.Member=None):
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        if user == None:
            humans = [m for m in ctx.guild.members if not m.bot]
            user = random.choice(humans)
        randomgifs = [
            "https://media.discordapp.net/attachments/949680123869814794/1046885786601136138/sportsmanias-just-married.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046885794087960626/anineogray-wedding.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046885802166206564/marriage-marry.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046885806226276432/TerribleRemorsefulCottontail-size_restricted.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046885979367165962/804a7b8872de5db7d3dee11a94a89449.gif?width=606&height=606",
            "https://media.discordapp.net/attachments/949680123869814794/1046885984442269758/tumblr_mllx0atPDj1r1r3hjo1_500.gif"
            ]
        
        embed=discord.Embed(title=f"{ctx.author.name} married {user.name} !! Congratulations to the newly weds",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)   

    @bot.command(aliases=["Sex","SEX"])
    async def sex(ctx,user:discord.Member=None):
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        if user == None:
            humans = [m for m in ctx.guild.members if not m.bot]
            user = random.choice(humans)
        randomgifs = [
            "https://media.discordapp.net/attachments/949680123869814794/1046886531866034198/e89cdf5e38c450a2b16399eeb870a7f364587bd1r1-320-232_hq.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046886528661602484/cr1tikal-sex.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046886523611660338/no-sex-sex-meme.gif?width=523&height=606",
            "https://media.discordapp.net/attachments/949680123869814794/1046886523091570799/sex-meme.gif?width=606&height=606"
            ]
        
        embed=discord.Embed(title=f"{ctx.author.name} trying to e-sex {user.name}, The deed will only be done if {user.name} also does the command",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)      

    @bot.command(aliases=["Wave","WAVE","Waving","waving"])
    async def wave(ctx,user:discord.Member=None):
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        if user == None:
            humans = [m for m in ctx.guild.members if not m.bot]
            user = random.choice(humans)
        randomgifs = [
            "https://media.discordapp.net/attachments/949680123869814794/1046891679770230835/monkey-waving.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046891680093188298/kung-fu-panda-po-waving-ub3ic92611g1yvxk.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046891680407756821/d7i06j2-209054b9-be1e-46b0-aa61-ffbe4dc1ebda.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046891681255006328/hello-there-waving.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046891681640890398/200w.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046891682018369606/garfield-waving.gif"   
            ]
        
        embed=discord.Embed(title=f"{ctx.author.name} waves at {user.name}",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)  

    @bot.command(aliases=["Bonk","BONK"])
    async def bonk(ctx,user:discord.Member=None):
        if user.id == ctx.author.id:
            await ctx.send("Bro atleast find someone to do an interaction with ")
            return
        if user == None:
            humans = [m for m in ctx.guild.members if not m.bot]
            user = random.choice(humans)
        randomgifs = [
            "https://media.discordapp.net/attachments/949680123869814794/1046892437043429416/detcgjg-50c2474a-fbbb-44f1-9766-a89f7f8e8253.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046892437555130440/bonk_2.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046892437953593534/b0d270b7c07757cc6c3fb6efc60229e8.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046892438322688190/bonk-anime.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046892438654030045/bonk.gif",
            "https://media.discordapp.net/attachments/949680123869814794/1046892439060885646/giphy.gif"
            ]
        
        embed=discord.Embed(title=f"{ctx.author.name} bonks{user.name} for being horny",color = discord.Colour.purple())
        randomgif = random.choice(randomgifs)
        embed.set_image(url = randomgif)
        await ctx.send(embed=embed)                                         
        
    bot.help_command = MyHelp()
    bot.run(token)
    
    
if __name__ == '__main__':
    main()
