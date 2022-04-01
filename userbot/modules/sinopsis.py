"""
Sinopsis scraper.
t.me/erruuu
"""

import requests
from bs4 import BeautifulSoup as bs
import re
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^\.sinop ?(.*)")
async def _(event):
    url = event.pattern_match.group(1)
    if not url:
        await event.edit("Enter your anime url, see .help sinopsis")
    elif "https://" not in url:
        await event.edit("Enter url")
        return
    else:
        await event.edit("`please wait..`")
        msg = "<b>➲ Sinopsis</b>\n"
        msg += f"<b>From {url}</b>"
        msg += f"═════════════════"
        neourl = requests.get(url)
        neopage = bs(neourl.content, 'html.parser')
        neos = neopage.find("div", class_="contenidotv")
        neop = neos.find(itemprop="description")
        for sino in neop.find_all('p'):
        	msg += f"<b>{sino}</b>\n"

        await event.edit(msg, parse_mode="html")


CMD_HELP.update(
    {
        "sinopsis": "**Sinopsis**"
        "\n ➲`.sinop` url"
        "\n ➣ ex: `.sinop https://neonime.watch/episode/fantasy-bishoujo-juniku-ojisan-to-1x12-subtitle-indonesia/`"
    }
)
