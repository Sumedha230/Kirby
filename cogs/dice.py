import discord
from discord.ext import commands
import random
from discord import app_commands


class dice(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.hybrid_command(name="dice",aliases=['dices','Dice','DICE'])
    async def dice(self,ctx:commands.Context,num:int):
        if num==6 or num==12:
            await ctx.send(f"{random.randint(1,int(num))}")       
        else:
            await ctx.send("Invalid Choice = Choose between 6 or 12")
    
         
async def setup(bot):
    await bot.add_cog(dice(bot))       
    print("dice is loaded")    

       
