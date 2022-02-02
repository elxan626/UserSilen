'''
Bu kod yığılıb by https://t.me/muellime


pip install Pyrogram
https://github.com/pyrogram/pyrogram.git
'''

import os
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

app_id = int(os.environ.get("API_ID", 12345))
app_key = os.environ.get('API_HASH')
token = os.environ.get('BOT_TOKEN')

app = Client("remove", app_id, app_key, bot_token=token)


STARTED = 'proses başladı...'
FINISH = 'proses {} uğurla başa çatdırıldı'
ERROR = 'Xətta baş verdi!'
ADMIN_NEEDED = "mənə admin hüquqları verin!"
PRIVATE = '''Salam, mən sizə qrupun böyüməsində kömək edəcəm.

İndi isə məni qrupa əlavə edin və admin hüquqlarını verməyi unutmayın
Ondan sonra qrupa /baslat göndərın və mən prosesə başlayacam.'''

@app.on_message(filters.group & filters.command("baslat"))
def main(_, msg: Message):
    chat = msg.chat
    me = chat.get_member(app.get_me().id)
    if chat.get_member(msg.from_user.id).can_manage_chat and me.can_restrict_members and me.can_delete_messages:
        try:
            msg.reply(STARTED.format(chat.members_count))
            count_kicks = 0
            for member in chat.iter_members():
                if not member.can_manage_chat:
                    chat.kick_member(member.user.id)
                    count_kicks += 1
            msg.reply(FINISH.format(count_kicks))
        except Exception as e:
            msg.reply(ERROR.format(str(e)))
    else:
        msg.reply(ADMIN_NEEDED)


@app.on_message(filters.group & filters.service, group=2)
def service(c, m):
    m.delete()


@app.on_message(filters.private)
def start(_, msg: Message):
    msg.reply(PRIVATE, reply_markup=InlineKeyboardMarkup([[
        InlineKeyboardButton("Sahibim", url=https://t.me/refmoneybot")]]))


app.run()
