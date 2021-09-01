import dislash
from dislash import *
import discord
from discord.ext import commands, tasks
import json


class VoteReminder(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.remind.start()

    @slash_command(name='votereminder', description='I will DM you every 12 hours to vote for Scopes!', options=[
        Option(name="action", description="Whether you want to enable or disable.", required=True, choices=[
            OptionChoice("enable", "enable"),
            OptionChoice("disable", "disable")
        ])
    ])
    async def votereminder(self, inter, action):
        with open("jsons/voteremind.json", "r") as f:
            load = json.load(f)

        if action == "enable":
            if inter.author.id in load["users"]:
                return await inter.reply("You already asked me to remind you to vote!", ephemeral=True)
            else:
                load["users"].append(inter.author.id)
                with open("jsons/voteremind.json", "w") as f:
                    json.dump(load, f, indent=4)

                await inter.reply("I will remind you to vote for Scopes every 12 hours!")

        if action == "disable":
            if inter.author.id not in load["users"]:
                return await inter.reply("You never asked me to remind you to vote!", ephemeral=True)
            else:
                load["users"].remove(inter.author.id)
                with open("jsons/voteremind.json", "w") as f:
                    json.dump(load, f, indent=4)

                await inter.reply("I will not remind you to vote for Scopes!")

    @tasks.loop(hours=12)
    async def remind(self):
        channel = self.bot.get_channel(882588101900378162)
        await channel.send("<@&881274995312037909> Time to vote! https://scopes.cf/vote.html")
        with open("jsons/voteremind.json", "r") as f:
            load = json.load(f)

        users = load["users"]
        for user_id in users:
            user = self.bot.get_user(user_id)
            await user.send("Time to vote for Scopes! https://scopes.cf/vote.html")


def setup(bot):
    bot.add_cog(VoteReminder(bot))
