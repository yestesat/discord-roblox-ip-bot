import json

from discord.ext import commands


class Global(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_command_error(self, ctx, error: str):

        # Lots of room for expansion. But this is basically all we need for this.
        if isinstance(error, commands.CommandNotFound):
            return
        else:
            print(f"{ctx.message.author} ({ctx.message.author.id}) | {error}")


def setup(bot):
    bot.add_cog(Global(bot))
