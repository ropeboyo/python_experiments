import requests
from tinydb import TinyDB, Query

start = 51347
target = 'nsfw'
db = TinyDB(f"{target}.json")
keep_going_senpai = True
fail_count = 0
format_options = ['jpg','png']
factor = 1
fail_tolerance = 128
fc = 0

while keep_going_senpai:
    test = str(hex(start)).replace('0x', '').upper()
    found = False

    for option in format_options:
        url = f"https://cdn.boob.bot/{target}/{test}.{option}"
        r = requests.get(url)
        print(f"Target: {test} | Format: {option} | Status code: {r.status_code}")
        if r.status_code == 200:
            db.insert({'url': url, 'source': 'boob-bot'})
            found = True
            """ fc = fc + 1
            if fc >= 2:
                keep_going_senpai = False """
    
    if found:
        fail_count = 0
    else:
        fail_count = fail_count + 1

    if fail_count > fail_tolerance:
        keep_going_senpai = False
    
    start = start + factor

