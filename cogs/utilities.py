from dislash import *
import discord
from discord.ext import commands

class Utilities(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
    @slash_command(name="invite", description="Get the invite link to this server.")
    async def invite(self, inter):
        await inter.respond("https://discord.gg/DaR54pXmJU")
        
    @slash_command(name="ping", description="Get the ping of the bot.")
    async def ping(self, inter):
        await inter.respond(f"Running on `{round(self.bot.latency*1000)}ms`.", ephemeral=True)
        
def setup(bot):
    bot.add_cog(Utilities(bot))
