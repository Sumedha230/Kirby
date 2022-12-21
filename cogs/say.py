import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import CommandTree


class say(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.hybrid_command(name="say",aliases=['imitate'])
    async def imitate(self,ctx, member: discord.Member, *, message=None):
        if message == None:
            await ctx.send('provide a message with that!')
            return
        webhook = await ctx.channel.create_webhook(name=member.name)
        await webhook.send(str(message), username=member.name, avatar_url=member.avatar.url)
        webhooks = await ctx.channel.webhooks()
        for webhook in webhooks:
            await webhook.delete()   

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(say(bot))       
    print("say is loaded")    
