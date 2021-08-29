# We will use "dislash.py" package for slash commands and buttons.
from dislash import *
import discord
from discord.ext import commands
import json


async def load_tags_list():
    with open("tags.json", "r") as f:
        load = json.load(f)

    return load.keys()


async def get_tag(tag):
    with open("tags.json", "r") as f:
        load = json.load(f)

    try:
        response = load[tag]
    except KeyError:
        response = "not found"

    return response


class Tags(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @slash_command(
        description="Got a question? Check if it there's a tag for it!",
        name="tag",
        options=[
            Option(name="tag",
                   description="The tag you want.",
                   type=Type.STRING,
                   required=True
                   )
        ]

    )
    async def tag(self, inter, tag):
        response = await get_tag(tag.lower())
        if response == "not found":
            return await inter.respond("Couldn't find the tag you are looking for! Use `/tags` to view a list of available tags.", ephemeral=True)

        embed = discord.Embed(color=inter.author.color,
                              title=tag.title(), description=response)

        await inter.respond(embed=embed)

    @slash_command(name="tags", description="List of available tags.")
    async def tags(self, inter):
        tags = await load_tags_list()
        embed = discord.Embed(color=inter.author.color,
                              title="Tags", description="\n".join(tags))

        await inter.respond(embed=embed, ephemeral=True)


def setup(bot):
    bot.add_cog(Tags(bot))
