import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import CommandTree
from discord.ui import Select,View

class help(commands.Cog,View):
    def __init__(self, bot):
        self.bot = bot
    @commands.group(invoke_without_command=True,aliases=["Help","HELP"])
    
    async def help(self,ctx):
        embed = discord.Embed(title="Help", description="Use k!help <command> for extended information on that command. The prefixes for the bot are : k!, K!, >",color = discord.Colour.purple())
        embed.add_field(name="Moderation Commands",value="clear/purge, warn, ban, kick, emoji_add, mute, unmute",inline=False)
        embed.add_field(name="User Commands", value = "avatar, guildavatar, banner, serverinfo, userinfo",inline=False)
        embed.add_field(name="Fun Commands",value = "dice, say, repeat, truthordare(tord), wouldyourather(wyr), paranoia, neverhaveiever(nhie), translate, translation", inline=False)
        embed.add_field(name= "Interaction Command", value = "block, bite, blush, bonk, boop, bored, cheer, choke, cope, cry, cuddle, dance, eating, fight, fuck, highfive, hug, judge, kill, kiss, laugh, liar, lick, love, marry, missing, nom, pat, pillowfight, pinch, poke, pray, punch, realkiss, salute, sip, sit, shock, slap, smirk, spank, stare, spit, stfu,threaten, tickle, touchgrass, twerk, vibe, wave, ,wink yawn",inline=False)
        await ctx.send(embed=embed)  
    @help.command()
    async def purge(self,ctx):
        embed = discord.Embed(title="Purge Command",description="This command deletes the given number of messages in a channel",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!purge for deleting a single message and k!purge number for deleting a specific number of messages, but it has a limit to the number of messages it can delete",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are clear/clr",inline=False)
        await ctx.send(embed=embed)  

    @help.command(aliases=['ava','av'])
    async def avatar(self,ctx):
        embed = discord.Embed(title="Avatar Command",description="This command shows the avatar of a user",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!avatar to get your avatar and k!avatar @user to get a user's avatar",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are ava/av",inline=False)
        await ctx.send(embed=embed)  

    @help.command(aliases=['ba'])
    async def banner(self,ctx):
        embed = discord.Embed(title="Banner Command",description="This command shows the banner of a user",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!banner to get your banner and k!banner @user to get a user's banner",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are ba",inline=False)
        await ctx.send(embed=embed)     

    @help.command(aliases=['ga','gava','avag','ag'])
    async def guildavatar(self,ctx):
        embed = discord.Embed(title="Guild Avatar Command",description="This command shows the server avatar of a user",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!guildavatar to get your server avatar and k!guildavatar @user to get a user's server avatar",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are gava / ga / avag / ag ",inline=False)
        await ctx.send(embed=embed)   

    @help.command(aliases=['ui','useri','uinfo'])
    async def userinfo(self,ctx):
        embed = discord.Embed(title="Userinfo Command",description="This command shows the info of a user",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!userinfo to get user server info and k!userinfo @user to get a user's server info",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are ui / uinfo / useri",inline=False)
        await ctx.send(embed=embed) 

    @help.command(aliases=['si','serveri','sinfo'])
    async def serverinfo(self,ctx):
        embed = discord.Embed(title="ServerInfo Command",description="This command shows the info of the server",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!serverinfo to get the info of the server",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are si / serveri / sinfo",inline=False)
        await ctx.send(embed=embed)  

    @help.command(aliases=['dices','Dice','Dices'])
    async def dice(self,ctx):
        embed = discord.Embed(title="Dice Command",description="This command rolls a dice of 6 or 12",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!dice 6 or k!dice 12 to get the dice rolling",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are dices",inline=False)
        await ctx.send(embed=embed)  

    @help.command(aliases=['imitate'])
    async def say(self,ctx):
        embed = discord.Embed(title="Imitate Command",description="This command makes the bot imitate as any user",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!say @user message",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are say / imitate",inline=False)
        await ctx.send(embed=embed) 

    @help.command(aliases=['sb','serverb','sboost'])
    async def serverbooster(self,ctx):
        embed = discord.Embed(title="Server Booster Command",description="This command shows the server booster",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!serverbooster",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are sb / serverb / sboost",inline=False)
        await ctx.send(embed=embed)                          
    
    @help.command(aliases=['tl','tr','tral'])
    async def translate(self,ctx):
        embed = discord.Embed(title="Translate Command",description="This command translates the text into english",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!translate sentence/word",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are tl / tr / tral",inline=False)
        await ctx.send(embed=embed) 

    @help.command(aliases=['translation','trion','tri','tli'])
    async def translating(self,ctx):
        embed = discord.Embed(title="Translating Command",description="This command translates the text into any given language (if it exists)",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!translation language sentence/word",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are translation / trion / tri / tli",inline=False)
        await ctx.send(embed=embed)     
    

    @help.command(aliases=['nhie','neverhie','neverhaveiever'])
    async def never_have_i_ever(self,ctx):
        embed = discord.Embed(title="Never Have I Ever Command",description="This command starts the game never have i ever",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!never_have_i_ever ",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are nhie / neverhie / neverhaveiever",inline=False)
        await ctx.send(embed=embed)    
    
    @help.command(aliases=['para','par','pn'])
    async def paranoia(self,ctx):
        embed = discord.Embed(title="Paranoia Questions Command",description="This command starts the game paranoia questions",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!paranoia ",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are para / par / pn",inline=False)
        await ctx.send(embed=embed) 

    @help.command(aliases=['rep'])
    async def repeat(self,ctx):
        embed = discord.Embed(title="Repeat Command",description="This command repeats what the user has said but it has a limit because no spamming the chat",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!repeat 2 hi",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are rep",inline=False)
        await ctx.send(embed=embed)      

    @help.command(aliases=['tord','truth','dare','truthordare' ])
    async def truth_or_dare(self,ctx):
        embed = discord.Embed(title="Truth or Dare Command",description="This command starts the game of truth or dare",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!truth_or_dare",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are tord / truth / dare / truthordare",inline=False)
        await ctx.send(embed=embed)     
    
    @help.command(aliases=["wyr",'wouldyourather','wouldyr'])
    async def would_you_rather(self,ctx):
        embed = discord.Embed(title="Would You Rather Command",description="This command starts the game of would you rather",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!would_you_rather",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are wyr / wouldyourather / wouldyr",inline=False)
        await ctx.send(embed=embed) 
    
    @help.command(aliases=['warning','warns'])
    async def warn(self,ctx):
        embed = discord.Embed(title="Warn Command",description="This command is an admin command and is used for warning members",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!warn @user",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are warning / warns",inline=False)
        await ctx.send(embed=embed) 

    @help.command(aliases=['bans','Ban'])
    async def ban(self,ctx):
        embed = discord.Embed(title="Ban Command",description="This command is an admin command and is used for banning members",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!ban @user",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are bans",inline=False)
        await ctx.send(embed=embed)     

    @help.command(aliases=['kicks'])
    async def kick(self,ctx):
        embed = discord.Embed(title="Kick Command",description="This command is an admin command and is used for kicking members",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!kick @user",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are kicks",inline=False)
        await ctx.send(embed=embed) 

    @help.command(aliases=['Kiss'])
    async def kiss(self,ctx):
        embed = discord.Embed(title="Kiss Command",description="This command is an interaction you can do with a user",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!kiss @user",inline=False)
        await ctx.send(embed=embed)

    @help.command(aliases=['Slap'])
    async def slap(self,ctx):
        embed = discord.Embed(title="Slap Command",description="This command is an interaction you can do with a user",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!slap @user",inline=False)
        await ctx.send(embed=embed)   

    @help.command(aliases=["Realkiss",'rk','rkiss','realk'])
    async def realkiss(self,ctx):
        embed = discord.Embed(title="RealKiss Command",description="This command is an nsfw interaction you can do with a user (Can only be done in a NSFW Channel)",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!realkiss @user",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are rk / rkiss / realk",inline=False)
        await ctx.send(embed=embed)  

    @help.command(aliases=['Hug'])
    async def hug(self,ctx):
        embed = discord.Embed(title="Hug Command",description="This command is an interaction you can do with a user",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!hug @user",inline=False)
        await ctx.send(embed=embed) 

    @help.command(aliases=['licks','licking'])
    async def lick(self,ctx):
        embed = discord.Embed(title="Lick Command",description="This command is an interaction you can do with a user",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!lick @user",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are licks / licking",inline=False)
        await ctx.send(embed=embed)  

    @help.command(aliases=['Fuck'])
    async def fuck(self,ctx):
        embed = discord.Embed(title="Fuck Command",description="This command is an interaction you can do with a user",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!fuck @user",inline=False)
        await ctx.send(embed=embed)      

    @help.command(aliases=['Love'])
    async def love(self,ctx):
        embed = discord.Embed(title="Love Command",description="This command is an interaction you can do with a user",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!love @user",inline=False)
        await ctx.send(embed=embed)   

    @help.command(aliases=["Missing","miss","Miss"])
    async def missing(self,ctx):
        embed = discord.Embed(title="Miss Command",description="This command is an interaction you can do with a user",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!missing @user",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are miss",inline=False)
        await ctx.send(embed=embed)     

    @help.command(aliases=['Tickle'])
    async def tickle(self,ctx):
        embed = discord.Embed(title="Tickle Command",description="This command is an interaction you can do with a user",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!tickle @user",inline=False)
        await ctx.send(embed=embed)   

    @help.command(aliases=['Spit'])
    async def spit(self,ctx):
        embed = discord.Embed(title="Spit Command",description="This command is an interaction you can do with a user",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!spit @user",inline=False)
        await ctx.send(embed=embed)   

    @help.command(aliases=['crying'])
    async def cry(self,ctx):
        embed = discord.Embed(title="Cry Command",description="This command is an interaction you can do with a user or without a user",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!cry @user or k!cry",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are crying",inline=False)
        await ctx.send(embed=embed)

    @help.command(aliases=['choking'])
    async def choke(self,ctx):
        embed = discord.Embed(title="Choke Command",description="This command is an interaction you can do with a user",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!choke @user",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are choking",inline=False)
        await ctx.send(embed=embed)
    
    @help.command(aliases=['eating'])
    async def eat(self,ctx):
        embed = discord.Embed(title="Eating Command",description="This command is an interaction you can do without a user",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!eating ",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are eat",inline=False)
        await ctx.send(embed=embed)    

    @help.command(aliases=['laughing'])
    async def laugh(self,ctx):
        embed = discord.Embed(title="Laugh Command",description="This command is an interaction you can do with a user or without a user",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!laugh @user or k!laugh",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are laughing",inline=False)
        await ctx.send(embed=embed)     

    @help.command(aliases=['pinching'])
    async def pinch(self,ctx):
        embed = discord.Embed(title="Pinch Command",description="This command is an interaction you can do with a user",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!pinch @user",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are pinching",inline=False)
        await ctx.send(embed=embed)      

    @help.command(aliases=['patting'])
    async def pat(self,ctx):
        embed = discord.Embed(title="Pat Command",description="This command is an interaction you can do with a user",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!pat @user",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are patting",inline=False)
        await ctx.send(embed=embed)     

    @help.command(aliases=['blocking'])
    async def block(self,ctx):
        embed = discord.Embed(title="Block Command",description="This command is an interaction you can do with a user",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!block @user",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are blocking",inline=False)
        await ctx.send(embed=embed)  

    @help.command(aliases=['Cope'])
    async def cope(self,ctx):
        embed = discord.Embed(title="Cope Command",description="This command is an interaction you can do with a user",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!cope @user",inline=False)
        await ctx.send(embed=embed)  

    @help.command(aliases=['sitting'])
    async def sit(self,ctx):
        embed = discord.Embed(title="Sit Command",description="This command is an interaction you can do with a user",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!sit @user",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are sitting",inline=False)
        await ctx.send(embed=embed)  

    @help.command(aliases=['punching'])
    async def punch(self,ctx):
        embed = discord.Embed(title="Punch Command",description="This command is an interaction you can do with a user",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!punch @user",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are punching",inline=False)
        await ctx.send(embed=embed)  

    @help.command(aliases=['vibing'])
    async def vibe(self,ctx):
        embed = discord.Embed(title="Vibe Command",description="This command is an interaction you can do with a user or without a user",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!vibe @user or k!vibe",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are vibing",inline=False)
        await ctx.send(embed=embed)  

    @help.command(aliases=['pillowfighting','pf','pillowf','pfight'])
    async def pillowfight(self,ctx):
        embed = discord.Embed(title="Pillowfight Command",description="This command is an interaction you can do with a user",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!pillowfight @user",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are pf / pillowf / pfight",inline=False)
        await ctx.send(embed=embed) 

    @help.command(aliases=['killing','Kill','Killing'])
    async def kill(self,ctx):
        embed = discord.Embed(title="Kill Command",description="This command is an interaction you can do with a user",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!kill @user",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are killing",inline=False)
        await ctx.send(embed=embed)      

    @help.command(aliases=['Nom'])
    async def nom(self,ctx):
        embed = discord.Embed(title="Nom Command",description="This command is an interaction you can do with a user",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!nom @user",inline=False)
        await ctx.send(embed=embed)  

    @help.command(aliases=['Marry'])
    async def marry(self,ctx):
        embed = discord.Embed(title="Marry Command",description="This command is an interaction you can do with a user",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!marry @user",inline=False)
        await ctx.send(embed=embed)    

    @help.command(aliases=['waving'])
    async def wave(self,ctx):
        embed = discord.Embed(title="Wave Command",description="This command is an interaction you can do with a user or without a user",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!wave @user or k!wave",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are waving",inline=False)
        await ctx.send(embed=embed)

    @help.command(aliases=['dancing','dances'])
    async def dance(self,ctx):
        embed = discord.Embed(title="Dance Command",description="This command is an interaction you can do with a user or without a user",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!dance @user or k!dance",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are dances / dancing",inline=False)
        await ctx.send(embed=embed)    

    @help.command(aliases=['stares','staring'])
    async def stare(self,ctx):
        embed = discord.Embed(title="Stare Command",description="This command is an interaction you can do with a user or without a user",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!stare @user or k!stare",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are stares / staring",inline=False)
        await ctx.send(embed=embed)     
    
    @help.command(aliases=['shocked','shocking'])
    async def shock(self,ctx):
        embed = discord.Embed(title="Shock Command",description="This command is an interaction you can do with a user or without a user",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!shock @user or k!shock",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are shocked / shocking",inline=False)
        await ctx.send(embed=embed)  

    @help.command(aliases=['twerking','twerks'])
    async def twerk(self,ctx):
        embed = discord.Embed(title="Twerk Command",description="This command is an interaction you can do with a user or without a user",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!twerk @user or k!twerk",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are twerking / twerks",inline=False)
        await ctx.send(embed=embed)         

    @help.command(aliases=['Bonk'])
    async def bonk(self,ctx):
        embed = discord.Embed(title="Bonk Command",description="This command is an interaction you can do with a user",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!bonk @user",inline=False)
        await ctx.send(embed=embed)    

    @help.command(aliases=['judging'])
    async def judge(self,ctx):
        embed = discord.Embed(title="Judge Command",description="This command is an interaction you can do with a user",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!judge @user",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are judging",inline=False)
        await ctx.send(embed=embed)  

    @help.command(aliases=['cheering'])
    async def cheer(self,ctx):
        embed = discord.Embed(title="Cheer Command",description="This command is an interaction you can do with a user or without a user",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!cheer @user or k!cheer",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are cheering",inline=False)
        await ctx.send(embed=embed)

    @help.command(aliases=['winking','winks'])
    async def wink(self,ctx):
        embed = discord.Embed(title="Wink Command",description="This command is an interaction you can do with a user or without a user",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!wink @user or k!wink",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are winking / winks",inline=False)
        await ctx.send(embed=embed)        

    @help.command(aliases=["Threaten","THREATEN",'threat'])
    async def threaten(self,ctx):
        embed = discord.Embed(title="Threaten Command",description="This command is an interaction you can do with a user",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!threaten @user",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are threat",inline=False)
        await ctx.send(embed=embed) 

    @help.command(aliases=["spanking","Spanking"])
    async def spank(self,ctx):
        embed = discord.Embed(title="Spank Command",description="This command is an interaction you can do with a user",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!spank @user",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are spanking",inline=False)
        await ctx.send(embed=embed) 

    @help.command(aliases=["STFU","shut","shutup","Shut"])
    async def stfu(self,ctx):
        embed = discord.Embed(title="ShutUp Command",description="This command is an interaction you can do with a user",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!stfu @user",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are shut / shutup",inline=False)
        await ctx.send(embed=embed)  

    @help.command(aliases=["Lie","lie","Liar","lying"])
    async def liar(self,ctx):
        embed = discord.Embed(title="Liar Command",description="This command is an interaction you can do with a user",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!liar @user",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are lie / lying",inline=False)
        await ctx.send(embed=embed)   

    @help.command(aliases=["sipping","slurp","sips","Sip"])
    async def sip(self,ctx):
        embed = discord.Embed(title="Sip Command",description="This command is an interaction you can do without a user",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!sip",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are sipping / slurp / sips / Sip",inline=False)
        await ctx.send(embed=embed)

    @help.command(aliases=["boring","bore"])
    async def bored(self,ctx):
        embed = discord.Embed(title="Bored Command",description="This command is an interaction you can do with or without a user",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!bored or k!bored @user",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are bore / boring",inline=False)
        await ctx.send(embed=embed)    

    @help.command(aliases=["prays","praying"])
    async def pray(self,ctx):
        embed = discord.Embed(title="Pray Command",description="This command is an interaction you can do with or without a user",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!pray @user or k!pray",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are praying / prays",inline=False)
        await ctx.send(embed=embed)     

    @help.command(aliases=["yawns","yawning"])
    async def yawn(self,ctx):
        embed = discord.Embed(title="Yawn Command",description="This command is an interaction you can do with or without a user",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!yawn @user or k!yawn",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are yawns / yawning",inline=False)
        await ctx.send(embed=embed) 

    @help.command(aliases=["smirks","smirking"])
    async def smirk(self,ctx):
        embed = discord.Embed(title="Smirk Command",description="This command is an interaction you can do with or without a user",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!smirk @user or k!smirk",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are smirks / smirking",inline=False)
        await ctx.send(embed=embed)    

    @help.command(aliases=["salutes","saluting"])
    async def salute(self,ctx):
        embed = discord.Embed(title="Salute Command",description="This command is an interaction you can do with a user",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!salute @user",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are salutes / saluting",inline=False)
        await ctx.send(embed=embed)

    @help.command(aliases=["cuddles","cuddling"])
    async def cuddle(self,ctx):
        embed = discord.Embed(title="Cuddle Command",description="This command is an interaction you can do with a user",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!cuddle @user",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are cuddles / cuddling",inline=False)
        await ctx.send(embed=embed)  

    @help.command(aliases=["hf","highf",'hfive'])
    async def highfive(self,ctx):
        embed = discord.Embed(title="Highfive Command",description="This command is an interaction you can do with a user",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!highfive @user",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are hf / highf / hfive",inline=False)
        await ctx.send(embed=embed)  

    @help.command(aliases=["blushes","blushing"])
    async def blush(self,ctx):
        embed = discord.Embed(title="Blush Command",description="This command is an interaction you can do with or without a user",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!blush @user or k!blush",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are blushes / blushing",inline=False)
        await ctx.send(embed=embed)   

    @help.command(aliases=["fights","fighting"])
    async def fight(self,ctx):
        embed = discord.Embed(title="Fight Command",description="This command is an interaction you can do with a user",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!fight @user",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are fights / fighting",inline=False)
        await ctx.send(embed=embed) 

    @help.command(aliases=["bites","biting"])
    async def bite(self,ctx):
        embed = discord.Embed(title="Fight Command",description="This command is an interaction you can do with a user",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!bite @user",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are bites / biting",inline=False)
        await ctx.send(embed=embed)       

    @help.command(aliases=["tg","touchg",'tgrass','touch'])
    async def touchgrass(self,ctx):
        embed = discord.Embed(title="Tough Grass Command",description="This command is an interaction you can do with or without a user",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!touchgrass @user or k!touchgrass",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are tg / touchg / tgrass / touch",inline=False)
        await ctx.send(embed=embed)     

    @help.command(aliases=["boops","bp"])
    async def boop(self,ctx):
        embed = discord.Embed(title="Boop Command",description="This command is an interaction you can do with a user",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!boop @user",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are boops / bp",inline=False)
        await ctx.send(embed=embed)   

    @help.command(aliases=["pokes","poking"])
    async def poke(self,ctx):
        embed = discord.Embed(title="Poke Command",description="This command is an interaction you can do with a user",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!poke @user",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are pokes / poking",inline=False)
        await ctx.send(embed=embed)            

    @help.command(aliases=["steal",'eadd'])
    async def emoji_add(self,ctx):
        embed = discord.Embed(title="Emoji Add Command",description="This command is a mod command that helps to add emojis",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!eadd :emotename: name_chosen_for_emote or k!eadd :emotename:",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are steal / eadd",inline=False)
        await ctx.send(embed=embed)  

    @help.command(aliases=["cr",'create'])
    async def createrole(self,ctx):
        embed = discord.Embed(title="Create Role Command",description="This command is a mod command that creates roles with or without icon",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!createrole role_name :emotename: or k!createrole role_name",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are cr / create",inline=False)
        await ctx.send(embed=embed) 

    @help.command(aliases=["ar",'add'])
    async def addrole(self,ctx):
        embed = discord.Embed(title="Add Role Command",description="This command is a mod command that add role to a user",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!addrole @user :rolename:",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are ar / add",inline=False)
        await ctx.send(embed=embed) 

    @help.command(aliases=["rr",'remove'])
    async def removerole(self,ctx):
        embed = discord.Embed(title="Remove Role Command",description="This command is a mod command that removes a role from a user",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!removerole @user :rolename:",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are rr / remove",inline=False)
        await ctx.send(embed=embed) 

    @help.command()
    async def mute(self,ctx):
        embed = discord.Embed(title="Mute Command",description="This command is a mod command that mutes a user",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!mute @user 7 d reason or k!mute @user that mutes the member for 1 min by default",inline=False)
        await ctx.send(embed=embed)

    @help.command(alises=['um'])
    async def unmute(self,ctx):
        embed = discord.Embed(title="UnMute Command",description="This command is a mod command that unmutes a user",color = discord.Colour.purple())
        embed.add_field(name="**Syntax**",value="k!unmute @user",inline=False)
        embed.add_field(name="Aliases",value="The aliases for this command are um",inline=False)
        await ctx.send(embed=embed)  


async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(help(bot))       
    print("help is loaded")    
    
