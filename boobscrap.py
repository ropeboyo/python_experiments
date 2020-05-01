import requests
from tinydb import TinyDB, Query

start = 6399
target = 'Gifs'
db = TinyDB(f"{target}.json")
keep_going_senpai = True
fail_count = 0

while keep_going_senpai:
    test = str(hex(start)).replace('0x', '').upper()
    url = f"https://cdn.boob.bot/{target}/{test}.gif"
    r = requests.get(url)
    print(f"Target: {test} | Status code: {r.status_code}")
    
    if r.status_code == 200:
        db.insert({'url': url, 'source': 'boob-bot'})
        fail_count = 0
    else:
        fail_count = fail_count + 1

    if fail_count > 10:
        keep_going_senpai = False
    
    start = start + 1

