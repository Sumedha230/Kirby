import discord
from discord.ext import commands

class Afk(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.data = []

    @commands.command()
    async def afk(self,ctx,*args:str):
        msg = " ".join(args)
        self.data.append(ctx.author.id)
        self.data.append(args)
        await ctx.send("afk set")

    @commands.Cog.listener()
    async def on_message(self,message):
        for i in range(len(self.data)):
            if (f"<@{self.data[i]}>" in message.content) and (not message.author.bot):
                await message.channel.send(f"<@{self.data[i]}> is afk, they said - {self.data[i+1]}")
                return None
                break
    @commands.Cog.listener()
    async def on_typing(self,channel,user,when):
        if user.id in self.data:
            i = self.data.index(user.id)
            self.data.remove(self.data[i+1])
            self.data.remove(user.id)
            await channel.send(f"{user.mention} has returned ")

def setup(bot):
    bot.add_cog(Afk(bot))                         
