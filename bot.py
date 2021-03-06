import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
# We will use "dislash.py" package for slash commands and buttons.
from dislash import *

load_dotenv()

TOKEN = os.getenv("TOKEN")
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

inter_client = InteractionClient(bot, test_guilds=[881149182210093057])


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(
        type=discord.ActivityType.listening, name="/ commands"
    ))
    for cog in os.listdir(r"cogs"):
        if cog.endswith(".py"):
            try:
                cog = f"cogs.{cog[:-3]}"
                bot.load_extension(cog)
                print(f"Loaded extension: {cog}")
            except Exception as e:
                print(f"{cog} failed to load:")
                raise e

    print(f"Logged in as {bot.user}")

bot.run(TOKEN)
