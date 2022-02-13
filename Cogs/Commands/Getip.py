import json

from discord.ext import commands
from Classes.Scraper import Scraper
from Classes.Embeds import embed_msg


with open("./config.json", "r") as r:
    whitelist_role = json.load(r)["roles"]["getip"]


class Getip(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    
    @commands.command()
    @commands.has_role(whitelist_role)
    async def getip(self, ctx, link: str):
        if "www.roblox.com/games/" not in link:
            return
        placeid = link.split("/")[4]    
        
        if placeid.isdigit() == False:
            return

        scraper = Scraper(placeid)
        scraper.set_placeid(placeid)
        information = await scraper.get_information()

        string = ""
        pack = information["package"]

        for i in range(len(pack)):
            info = pack[i]
            string += "[ Server {} ({}/{}) | {}:{} | {}ms ]\n".format(
                str(i + 1).zfill(2),
                info["players"],
                info["maxPlayers"],
                info["ip"],
                info["port"],
                info["ping"]
            )

        if len(string) == 0:
            return await ctx.send("Failed to fetch any server information.", delete_after=5.0)

        return await ctx.send(embed=embed_msg(f"```ini\n{string}\n```", ctx.message.author))

        
def setup(bot):
    bot.add_cog(Getip(bot))
