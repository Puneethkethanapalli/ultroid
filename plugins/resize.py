# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

"""
✘ Commands Available -

•`{i}size <reply to media>`
   To get size of it.

•`{i}resize <number> <number>`
   To resize image on x, y axis.
   eg. `{i}resize 690 960`
"""

from PIL import Image

from . import *


@ultroid_cmd(pattern="size$")
async def size(e):
    r = await e.get_reply_message()
    if not (r and r.media):
        return await eor(e, "`Reply To image`")
    if hasattr(r.media, "document"):
        img = await ultroid_bot.download_media(r, thumb=-1)
    else:
        img = await ultroid_bot.download_media(r.media)
    im = Image.open(img)
    x, y = im.size
    await eor(e, f"Dimension Of This Image Is {x} : {y}")
    os.remove(img)


@ultroid_cmd(pattern="resize ?(.*)")
async def size(e):
    r = await e.get_reply_message()
    if not (r and r.media):
        return await eor(e, "`Reply To image`")
    sz = e.pattern_match.group(1)
    if not sz or (len(sz.split()) == 3):
        return await eor("Give Some Size To Resize, Like `{i}resize 720 1080` ")
    if hasattr(r.media, "document"):
        img = await ultroid_bot.download_media(r, thumb=-1)
    else:
        img = await ultroid_bot.download_media(r.media)
    sz = sz.split()
    x, y = int(sz[1]), int(sz[2])
    im = Image.open(img)
    ok = im.resize((x, y))
    ok.save(img, format="PNG", optimize=True)
    await ultroid_bot.send_file(e.chat_id, img)
    os.remove(img)


HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})
