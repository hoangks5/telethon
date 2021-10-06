from telethon import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
import time
api_id = 8763319
api_hash = '28f53a40a4052cd950dab693a3a3c04c'

with TelegramClient(str(input('Nhập số STT acc (ví dụ acc1,acc2,v.v...): ')), api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message('me', 'Đăng nhập thành công'))
    time.sleep(5)