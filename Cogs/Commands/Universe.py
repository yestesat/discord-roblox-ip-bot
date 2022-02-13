import json

from discord.ext import commands
from Classes.Scraper import Scraper
from Classes.Embeds import embed_msg


with open("./config.json", "r") as r:
    whitelist_role = json.load(r)["roles"]["universe"]


class Universe(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    
    @commands.command()
    @commands.has_role(whitelist_role)
    async def universe(self, ctx, link: str):
        pass


def setup(bot):
    bot.add_cog(Universe(bot))
