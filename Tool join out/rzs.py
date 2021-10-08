from asyncio import events
from os import name
import re
from telethon import TelegramClient, events, hints
from telethon.tl.functions.channels import JoinChannelRequest, LeaveChannelRequest
import time
from telethon.tl.functions.messages import SendMessageRequest
import random
from telethon.tl.types import messages
from telethon.tl.functions.account import UpdateUsernameRequest
from telethon.tl.functions.photos import UploadProfilePhotoRequest
from telethon.tl.functions.account import UpdateProfileRequest
import os
import threading

acc = []
os.chdir('./')
list = os.listdir()
for accs in list:
    if accs[:3] == 'acc':
        acc.append(accs.split('.')[0])
api_id = 8763319
api_hash = '28f53a40a4052cd950dab693a3a3c04c'
def xinchao():
    xinch = open('setting/hello.txt','r',encoding='utf-8')
    xinch = xinch.read()
    xinch = xinch.splitlines()
    for iz in xinch:
        print(iz)
xinchao()
for accs in acc:
    print(accs)
    client = TelegramClient(accs, api_id, api_hash)
    async def main():
        me = await client.get_me()
    with client:
        client.loop.run_until_complete(main())
name_tt = input('Nhập tên muốn đổi: ')
about_tt = input('Nhập tiểu sử muốn đổi: ')
link_gr = input('Nhập link group(vd: https://t.me/laucua) :')
time_edit = int(input('Sau thời gian sẽ out nhóm :'))

for accs in acc:
    try:
        client = TelegramClient(accs, api_id, api_hash)
        async def main():
            # Getting information about yourself
            me = await client.get_me()
            await client(UpdateProfileRequest(
            first_name = name_tt,
            about = about_tt
        ))
            await client(UploadProfilePhotoRequest(
                await client.upload_file('./data/avatar/avatar.png')))
            
        with client:
            client.loop.run_until_complete(main())
    except:
        pass


while True:
    try:
        client = TelegramClient(accs, api_id, api_hash)
        async def main():
            await client(JoinChannelRequest(link_gr))
            time.sleep(time_edit)
            await client(LeaveChannelRequest(link_gr))
        with client:
            client.loop.run_until_complete(main())
    except:
        print('Không tham gia được, xin kiểm tra lại chế độ riêng tư của group hoặc của nick ')
