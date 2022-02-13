import json

from discord.ext import commands
from Classes.Scraper import Scraper
from Classes.Embeds import embed_msg


with open("./config.json", "r") as r:
    whitelist_role = json.load(r)["roles"]["hit"]


class Hit(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    
    @commands.command()
    @commands.has_role(whitelist_role)
    async def hit(self, ctx, host: str, port: str, time: str, method: str):
        pass


def setup(bot):
    bot.add_cog(Hit(bot))


