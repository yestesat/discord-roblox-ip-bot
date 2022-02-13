from discord.ext import commands
from Classes.Embeds import embed_msg
from main import bot_prefix


class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    
    @commands.command()
    async def help(self, ctx):
        getip = f"[ {bot_prefix}getip link: ]"
        hit = f"[ {bot_prefix}hit host: port: time: method: ]"
        kill = f"[ {bot_prefix}kill link: time: ]"
        plr = f"[ {bot_prefix}plr username: ]"
        universe = f"[ {bot_prefix}universe link: ]"


        help_msg = f"```ini\n; Help Embed ;\n{getip}\n{hit}\n{kill}\n{plr}\n{universe}\n```"
        return await ctx.send(embed=embed_msg(help_msg, ctx.message.author))


def setup(bot):
    bot.add_cog(Help(bot))
