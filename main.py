import discord
import json

from discord.ext import commands


# Edit this how you want
activity = discord.Streaming(name="Subject Testing..", url="https://www.twitch.tv/testing")
bot_prefix = "$"

booter_api = "http://booter.com/key={api-key}&host={host}&port={port}&time={time}&method={method}".format
kill_method = "roblox"
#

# No touching under this :)
bot = commands.Bot(command_prefix=bot_prefix, case_insensitive=True, activity=activity, help_command=None)

# Cogs
## Commands
bot.load_extension("Cogs.Commands.Getip")
bot.load_extension("Cogs.Commands.Help")
bot.load_extension("Cogs.Commands.Hit")
bot.load_extension("Cogs.Commands.Kill")
bot.load_extension("Cogs.Commands.Plr")
bot.load_extension("Cogs.Commands.Universe")

## Events
bot.load_extension("Cogs.Events.Events")

# I understand I could've just done dir loops, but for accessabilities sake I chose this.

## Error Handling
# bot.load_extension("Cogs.ErrorHandling.Global")


if __name__ ==  "__main__":
    with open("config.json", "r") as r:
        token = json.load(r)["discord"]["token"]

    bot.run(token)
