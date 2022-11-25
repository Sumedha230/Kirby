import os
import discord
from dotenv.main import load_dotenv
from discord.ext import commands
from discord.ext.commands import Bot

import random


def main():
    load_dotenv()

    token = "MTA0Mzg1ODk0MDk5MzIyODgwMA.GjcoGW.bPCb5Nthf_6mWLTM9VP2TrOwXZ-dA2fnZcLKmg"


    bot = commands.Bot(intents=discord.Intents.all() , command_prefix= "k!" , description='Cute Kirby!')

    @bot.event
    async def on_ready():
        print(f"{bot.user.name}has Connected")

    @bot.command()
    async def ping(ctx):
        """Checks for a response from the bot"""
        await ctx.send("Pong")        

    @bot.command()
    async def hello(ctx):
        await ctx.send(f"Hi {ctx.message.author.mention}!")    

    @bot.command()
    async def choose(ctx, *choices: str):
        await ctx.send(random.choice(choices)) 
    
    @bot.command()
    async def say(ctx, member: discord.Member, *, message=None):
        if message == None:
            await ctx.send('provide a message with that!')
            return

        webhook = await ctx.channel.create_webhook(name=member.name)
        await webhook.send(str(message), username=member.name, avatar_url=member.avatar.url)

        webhooks = await ctx.channel.webhooks()
        for webhook in webhooks:
            await webhook.delete()
    
    @bot.command()
    async def repeat(ctx, times: int, content='repeating...'):
        if 0<times<=20:
            for i in range(times):
                await ctx.send(content) 
        else:
            embed = discord.Embed(color = discord.Colour.purple(),description="Kirby is not a fool and won't spam the chat")
            embed.set_image(url ="https://media.discordapp.net/attachments/1042790120652275853/1045611042228666408/kirby-mad.gif")
            await ctx.send(embed=embed)
    
    @bot.command()
    async def avatar(ctx, *,  avamember : discord.Member=None):
        test = discord.Embed(title=f"{avamember.name}'s Avatar")
        test.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        test.set_image(url=ctx.author.avatar.url)
        await ctx.send(embed=test)

    @bot.command()
    async def banner(ctx, user:discord.Member = None):
        if not user:
            user = ctx.author
        user = await bot.fetch_user(user.id)  
        if user.banner:
            embed = discord.Embed(title = f"{user.name}'s Banner")
            embed.set_author(name=ctx.author.name,icon_url=ctx.author.avatar.url)
            embed.set_image(url = user.banner.url)
            await ctx.send(embed=embed)
        else:
            await ctx.send(f'this user has no banner')  

    bot.run(token)
if __name__ == '__main__':
    main()
