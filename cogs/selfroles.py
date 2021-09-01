import dislash
from dislash import *
import discord
from discord.ext import commands


class SelfRoles(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @slash_command(
        name="getrole",
        description="Grab a role for yourself!",
        options=[
            Option(name="role", description="The role you want.",
                   choices=[
                       OptionChoice(name="partnership-ping",
                                    value=882578885684899850),
                       OptionChoice(name="vote-reminder",
                                    value=881274995312037909),
                       OptionChoice(name="supdates",
                                    value=881275063041654845)
                   ],
                   required=True
                   )
        ]
    )
    async def getrole(self, inter, role):
        role = inter.guild.get_role(role)
        if role in inter.author.roles:
            return await inter.reply(f"You already have the role **{role.name}**! If you want to remove it, use `/removerole {role.name.lower()}`.", ephemeral=True)
        else:
            await inter.author.add_roles(role)
            await inter.reply(f"I gave you the role **{role.name}**!")

    @slash_command(
        name="removerole",
        description="Remove your self assigned roles!",
        options=[
            Option(name="role", description="The role you want to remove.",
                   choices=[
                       OptionChoice(name="partnership-ping",
                                    value=882578885684899850),
                       OptionChoice(name="vote-reminder",
                                    value=881274995312037909),
                       OptionChoice(name="supdates",
                                    value=881275063041654845)
                   ],
                   required=True
                   )
        ]
    )
    async def removerole(self, inter, role):
        role = inter.guild.get_role(role)
        if role not in inter.author.roles:
            return await inter.reply(f"You don't have the role **{role.name}**! If you want to get it, use `/getrole {role.name.lower()}`.", ephemeral=True)
        else:
            await inter.author.remove_roles(role)
            await inter.reply(f"I removed the role **{role.name}** from you!")


def setup(bot):
    bot.add_cog(SelfRoles(bot))
