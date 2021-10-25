import telethon
import time
import datetime
import config

with telethon.TelegramClient('me', 2173040, 34c0274ce8b5868268204aa3c885cd96) as client:
    async def do():
        while True:
            n = datetime.datetime.now()
            if n.second == 0:
                print(n)
                nowstr = "⏱ Now: " + datetime.datetime.now().strftime('%H:%M') + " ⏱"
                try:
                    await client(telethon.functions.account.UpdateProfileRequest(about=nowstr))
                except telethon.errors.rpcerrorlist.FloodWaitError as e:
                    print('Flood waited for', e.seconds)
                    time.sleep(e.seconds + 1)
            time.sleep(1)
    client.loop.run_until_complete(do())
