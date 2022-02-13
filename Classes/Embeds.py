# Not a class but whatever cunt
from discord import Embed
from datetime import datetime


def embed_msg(description, footer):
    return Embed(
        title="",
        description=description,
        timestamp=datetime.utcnow(),
        colour=288429,
    ).set_footer(text=footer)