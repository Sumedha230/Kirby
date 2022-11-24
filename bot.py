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

    answers = ["patch", "mark", "cat", "dog", "elephant", "frog", "gun"]

    @bot.command(pass_context=True)  
    async def choose(ctx, k: int):
        """Chooses from multiple choices."""
        if 0 <= k <= 10:
            await ctx.send("This is your random {} pick, {}".format(k, ctx.message.author.mention))
            embed = discord.Embed(description='\n'.join(random.choices(answers, k=k)))
            await ctx.send(embed=embed)
        else:
            await ctx.send("Invalid number")    

    bot.run(token)
if __name__ == '__main__':
    main()
