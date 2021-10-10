from asyncio import events
from os import name
import re
from telethon import TelegramClient, events, hints
from telethon.tl.functions.channels import JoinChannelRequest
import time
from telethon.tl.functions.messages import SendMessageRequest
import random
from telethon.tl.types import messages
from telethon.tl.functions.account import UpdateUsernameRequest
from telethon.tl.functions.photos import UploadProfilePhotoRequest
from telethon.tl.functions.account import UpdateProfileRequest
import os
import threading

f = open('chat.txt','r',encoding='utf-8')
f = f.read()
f = f.split('||')
acc = []
os.chdir('./')
list = os.listdir()
for accs in list:
    if accs[:3] == 'acc':
        acc.append(accs.split('.')[0])
def xinchao():
    xinch = open('setting/hello.txt','r',encoding='utf-8')
    xinch = xinch.read()
    xinch = xinch.splitlines()
    for iz in xinch:
        print(iz)
xinchao()
print('Đã đăng nhập '+str(len(acc))+' acc trên hệ thống, vui lòng đọc hướng dẫn chi tiết bên trên.\n')
link_gr = input('Nhập link group(vd: https://t.me/laucua) :')
try:
    list_grs = link_gr.split(';')
except:
    list_grs = link_gr

time_acc = int(input('Thời gian chat cách nhau của các acc(giây) :'))
api_id = 8763319
api_hash = '28f53a40a4052cd950dab693a3a3c04c'
for accs in acc:
    print('Đăng nhập '+accs)
    client = TelegramClient(accs, api_id, api_hash)
    async def main():
                            # Getting information about yourself
                        me = await client.get_me()
    with client:
                        client.loop.run_until_complete(main())
print('Đăng nhập thành công '+str(len(acc))+' acc')
def ok():
    while True:
        for az in list_grs:
            for chat in f:
                try:
                    client = TelegramClient(random.choice(acc), api_id, api_hash)
                    async def main():
                            # Getting information about yourself
                        me = await client.get_me()
                        await client(JoinChannelRequest(az))
                        await client(SendMessageRequest(az,chat))
                    with client:
                        client.loop.run_until_complete(main())
                    time.sleep(time_acc)
                except:
                    pass
                
ok()


