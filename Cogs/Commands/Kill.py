import json

from discord.ext import commands
from Classes.Scraper import Scraper
from Classes.Embeds import embed_msg


with open("./config.json", "r") as r:
    whitelist_role = json.load(r)["roles"]["kill"]


class Kill(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.method = "ROBLOX"

    
    @commands.command()
    @commands.has_role(whitelist_role)
    async def kill(self, ctx, link: str, time: str):
        if "www.roblox.com/games/" not in link:
            return
        placeid = link.split("/")[4]    
        
        if placeid.isdigit() == False:
            return

        scraper = Scraper(placeid)
        scraper.set_placeid(placeid)


def setup(bot):
    bot.add_cog(Kill(bot))
