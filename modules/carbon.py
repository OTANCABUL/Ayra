# Ayra - UserBot
# Copyright (C) 2021-2022 senpai80
#
# This file is a part of < https://github.com/senpai80/Ayra/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/senpai80/Ayra/blob/main/LICENSE/>.

"""
✘ **Bantuan Untuk Carbon**

๏ **Perintah:** `carbon` <berikan pesan/balas pesan>
◉ **Keterangan:** Carbonise teks.
"""

from . import *

_colorspath = "resources/colorlist.txt"

if os.path.exists(_colorspath):
    with open(_colorspath, "r") as f:
        all_col = f.read().split()
else:
    all_col = []


@ayra_cmd(
    pattern="(rc|c)arbon",
)
async def crbn(event):
    xxxx = await event.eor(get_string("com_1"))
    te = event.pattern_match.group(1)
    col = random.choice(all_col) if te[0] == "r" else "White"
    if event.reply_to_msg_id:
        temp = await event.get_reply_message()
        if temp.media:
            b = await event.client.download_media(temp)
            with open(b) as a:
                code = a.read()
            os.remove(b)
        else:
            code = temp.message
    else:
        try:
            code = event.text.split(" ", maxsplit=1)[1]
        except IndexError:
            return await eor(xxxx, get_string("carbon_2"))
    xx = await Carbon(code=code, file_name="ayra", backgroundColor=col)
    await xxxx.delete()
    await event.client.send_file(
        f"Carbonised by {OWNER_NAME}",
        file=xx,
    )


@ayra_cmd(
    pattern="ccarbon( (.*)|$)",
)
async def crbn(event):
    match = event.pattern_match.group(1).strip()
    if not match:
        return await event.eor(get_string("carbon_3"))
    msg = await event.eor(get_string("com_1"))
    if event.reply_to_msg_id:
        temp = await event.get_reply_message()
        if temp.media:
            b = await event.client.download_media(temp)
            with open(b) as a:
                code = a.read()
            os.remove(b)
        else:
            code = temp.message
    else:
        try:
            match = match.split(" ", maxsplit=1)
            code = match[1]
            match = match[0]
        except IndexError:
            return await eor(msg, get_string("carbon_2"))
    xx = await Carbon(code=code, backgroundColor=match)
    await msg.delete()
    await event.client.send_file(
        f"Carbonised by {OWNER_NAME}",
        file=xx,
    )


RaySoTheme = [
    "meadow",
    "breeze",
    "raindrop",
    "candy",
    "crimson",
    "falcon",
    "sunset",
    "midnight",
]

@ayra_cmd(pattern="rayso")
async def pass_on(kaz):
    spli = kaz.text.split()
    theme, dark, title, text = None, True, get_display_name(kaz.chat), None
    if len(spli) > 2:
        if spli[1] in RaySoTheme:
            theme = spli[1]
        dark = spli[2].lower().strip() in ["true", "t"]
    elif len(spli) > 1:
        if spli[1] in RaySoTheme:
            theme = spli[1]
        elif spli[1] == "list":
            text = "**List of Rayso Themes:**\n" + "\n".join(
                [f"- `{th_}`" for th_ in RaySoTheme]
            )

            await kaz.eor(text)
            return
        else:
            try:
                text = kaz.text.split(maxsplit=1)[1]
            except IndexError:
                pass
    if not theme:
        theme = random.choice(RaySoTheme)
    if kaz.is_reply:
        msg = await kaz.get_reply_message()
        text = msg.text
        title = get_display_name(msg.sender)
    await kaz.reply(
        file=await Carbon(text, rayso=True, title=title, theme=theme, darkMode=dark)
    )