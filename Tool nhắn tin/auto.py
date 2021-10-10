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

api_id = 8763319
api_hash = '28f53a40a4052cd950dab693a3a3c04c'
f = open('chat.txt','r',encoding='utf-8')
f = f.read()
f = f.split('||')
chatfist = f[0]
chatedit = f[1]
g = open('./data/name.txt','r',encoding='utf-8')
g = g.read()
nameuser = g.splitlines()
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
for accs in acc:
    print(accs)
    client = TelegramClient(accs, api_id, api_hash)
    async def main():
        me = await client.get_me()
        print(me)
    with client:
        client.loop.run_until_complete(main())
print('Đã đăng nhập '+str(len(acc))+' acc trên hệ thống, vui lòng đọc hướng dẫn chi tiết bên trên.\n')
link_gr = input('Nhập link group(vd: https://t.me/laucua) :')
time_acc = int(input('Thời gian chat cách nhau của các acc(giây) :'))
time_edit = int(input('Thời gian nghỉ để sửa nội dung(giây) :'))


history_id = []



        
for accs in acc:
    try:
        client = TelegramClient(accs, api_id, api_hash)
        async def main():
            me = await client.get_me()
            await client(JoinChannelRequest(link_gr))
            refust = await client(SendMessageRequest(link_gr,random.choice(chatfist.split(';'))))
            refust = str(refust).split(',')[0]
            refust = refust.split('=')[2]
            history = accs +'='+refust
            history_id.append(history)
        with client:
            client.loop.run_until_complete(main())
        time.sleep(time_acc)
    except:
        pass
time.sleep(time_edit)
for accs in acc:
    try:
        client = TelegramClient(accs, api_id, api_hash)
        async def main1():
            me = await client.get_me()
            for id in history_id:
                id = id.split('=')
                if id[0] == accs:
                    nb_id = id[1]
            await client.edit_message(link_gr,int(nb_id),chatedit)
            await client(UpdateProfileRequest(
            
            first_name = random.choice(nameuser)
        ))
            
            await client(UploadProfilePhotoRequest(
                await client.upload_file('./data/avatar/avatar.png')))
            
        with client:
            client.loop.run_until_complete(main1())
    except:
        pass
