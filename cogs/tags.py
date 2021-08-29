from dislash import *
import discord
from discord.ext import commands
import json


async def load_tags_list():
    with open("jsons/tags.json", "r") as f:
        load = json.load(f)

    return load.keys()


async def get_tag(tag):
    with open("jsons/tags.json", "r") as f:
        load = json.load(f)

    try:
        response = load[tag]
    except KeyError:
        response = "not found"

    return response


async def create_tag(tag, response):
    with open("jsons/tags.json", "r") as f:
        load = json.load(f)

    result = await get_tag(tag)
    if result != "not found":
        return "exists"

    load[tag] = response

    with open("tags.json", "w") as f:
        json.dump(load, f, indent=4)

    return "created"


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

    @slash_command(name="create_tag", description="Create a new tag.", options=[
        Option("tag", "The tag's title.", Type.STRING, True),
        Option("response", "The tag's response.", Type.STRING, True)
    ])
    @commands.has_permissions(administrator=True)
    async def create_tag(self, inter, tag, response):
        result = await create_tag(tag.lower(), response)
        if result == "exists":
            return await inter.respond("This tag already exists!", ephemeral=True)
        else:
            await inter.respond(f'Tag "**{tag}**" created!')


def setup(bot):
    bot.add_cog(Tags(bot))
