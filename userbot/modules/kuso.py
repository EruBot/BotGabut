"""
Kuso search.
t.me/erruuu
"""

import requests
from bs4 import BeautifulSoup as bs
import re
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern=r"^\.kuso ?(.*)")
async def _neonime(event):
    await event.edit("`please wait...`")
    urll = "https://kusonime.com/?s="
    url = event.pattern_match.group(1)
    url = url.replace(" ", "+")
    ht_ = requests.get(urll + url).text
    _bs = bs(ht_, "html.parser")
    bd_ = _bs.findAll("h2", class_="episodeye")
    out = "<b>➲ Kusonime > Search Batch:</b>\n═════════════════\n"
    for kntl_ in bd_:
        _lucu = kntl_.find("a")
        if not _lucu:
            _lucu = "none"
        else:  # FKTnK3aKtFvMSUiWLZrTuAp4g93VSjbXcR5zGmqWAijuAuYgR2ACP8WNot2ZyTRVECks1uV5WWW7muWz5SZkY2P8YbWW6AYLUFTsmFU1oW9Y2GP4
            tt_ = _lucu.get_text()
            _tt = re.sub(r"\s+Subtitle\s+Indonesia\s+Season.\d+", "", tt_)
            link = _lucu["href"]
            out += f"➣ <a href='{link}'>{_tt}</a>\n"
            if len(out) > 2048:
                break
            await event.edit(out, parse_mode="html")

CMD_HELP.update(
    {
        "kusonime": "**Kusonime**"
        "\n ➲`.kuso` keyword"
        "\n ➣ ex: `.kuso boruto`"
    }
)
