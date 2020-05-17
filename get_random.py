import requests
import random
from tinydb import TinyDB, Query

databases = [
    'anal.json',
    'blowjob.json',
    'Gifs.json',
    'nsfw.json',
    'hentai.json'
]
keep_going_senpai = True

while keep_going_senpai:
    target = TinyDB(random.choice(databases))
    target_size = len(target)
    index = random.randint(0, target_size)
    test = target.all()
    print(test[index]['url'])

    opt = input('Another one pervy perv? (Y/n)')
    if opt.upper() == 'Y' or opt == '':
        pass
    else:
        keep_going_senpai = False    


