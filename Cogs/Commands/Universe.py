import json

from discord.ext import commands
from numpy import void
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
        if "www.roblox.com/games/" not in link:
            return
        placeid = link.split("/")[4]    
        
        if placeid.isdigit() == False:
            return

        scraper = Scraper(placeid)
        scraper.set_placeid(placeid)

        universe_information = await scraper.get_universe_from_placeid()
        universe_places = await scraper.get_places_in_universe(universe_information["UniverseId"])

        if len(universe_places["data"]) == 0:
            return await ctx.send("Failed to fetch any server information.", delete_after=5.0)

        for _,v in enumerate(universe_places["data"]):
            scraper.set_placeid(v["id"])
            string = "; {} ;\n".format(
                v["name"]
            )
            
            information = await scraper.get_basic_information()

            if len(information["package"]) == 0:
                continue

            embed = embed_msg(f"```ini\n{string}\n```", ctx.message.author)
            msg = await ctx.send(embed=embed)

            for l,k in enumerate(information["package"]):
                server_information = await scraper.information_from_jobid(k["jobId"])
                pack = server_information["package"]

                string += "[ Server {} ({}/{}) | {}:{} | {}ms ]\n".format(
                    str(l + 1).zfill(2),
                    k["players"],
                    k["maxPlayers"],
                    pack["ip"],
                    pack["port"],
                    k["ping"]
    
                )

                embed = embed_msg(f"```ini\n{string}\n```", ctx.message.author)
                await msg.edit(embed=embed)


def setup(bot):
    bot.add_cog(Universe(bot))
