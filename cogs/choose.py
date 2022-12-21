import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import CommandTree
import random

class choice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.hybrid_command(name="choose",aliases=["choice"])
    async def choose(self,ctx,option1=None,option2=None,option3=None,option4=None,option5=None):
        choic = []
        for i in range(1,6):
            if i==1:
                if option1!=None:
                    choic.append(option1)
                else:
                    await ctx.send("you have not given any option")
                return        
            if i==2:
                if option2 !=None:
                    choic.append(option2)
            if i==3:
                if option3 != None:
                    choic.append(option3)
            if i==4:
                if option4 != None:
                    choic.append(option4)
            if i==5:
                if option5 != None:
                    choic.append(option5)
        await ctx.send(f"I choose, {random.choice(choic)}")            

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(choice(bot))       
    print("choice is loaded")    
    
