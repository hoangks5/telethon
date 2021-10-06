from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
import csv
import pandas
import time

api_id = 8763319
api_hash = '28f53a40a4052cd950dab693a3a3c04c'
phone = '+84358259167'        
client = TelegramClient(phone, api_id, api_hash)
async def main():
    # Now you can use all client methods listed below, like for example...
    await client.send_message('me', 'Hello !!!!')
with client:
    client.loop.run_until_complete(main())
client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter verification code: '))


chats = []
last_date = None
chunk_size = 200
groups=[]

result = client(GetDialogsRequest(
             offset_date=last_date,
             offset_id=0,
             offset_peer=InputPeerEmpty(),
             limit=chunk_size,
             hash = 0
         ))
chats.extend(result.chats)

for chat in chats:
    try:
        if chat.megagroup== True:
            groups.append(chat)
    except:
        continue

print('Danh Sách Group: ')
i=0
for g in groups:
    print(str(i) + '- ' + g.title)
    i+=1

g_index = input("Chọn Group để quét danh sách thành viên: ")
target_group=groups[int(g_index)]

print('Đang quét...')
all_participants = []
all_participants = client.get_participants(target_group, aggressive=True)

print('Đang lưu thông tin vào file info.csv')
with open("info.csv","w",encoding='UTF-8') as f:#Enter your file name.
    writer = csv.writer(f,delimiter=",",lineterminator="\n")
    writer.writerow(['Username','ID', 'Access Hash','Tên','Group', 'Group id'])
    for user in all_participants:
        if user.username:
            username= user.username
        else:
            username= ""
        if user.first_name:
            first_name= user.first_name
        else:
            first_name= ""
        if user.last_name:
            last_name= user.last_name
        else:
            last_name= ""
        name= (first_name + ' ' + last_name).strip()
        writer.writerow([username,user.id,user.access_hash,name,target_group.title, target_group.id])
import pandas
df = pandas.read_csv('info.csv')
print(df)
print('Đã quét thành công')
time.sleep(1000)