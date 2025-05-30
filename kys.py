import requests
import json
import time

config = []

with open('config.json', 'r') as f:
    config = json.loads(f.read())

print(f'scanning for {len(config['scanna'])} person(s??)')

true = True

for person in config['scanna']:
    r = requests.post("https://www.ratsit.se/api/search/combined", headers={
        "Content-Type": "application/json",
        "User-Agent": "whore"
    }, json={
        "who": f"{person}",
        "age": ["16", "120"],
        "phoneticSearch": true,
        "companyName": "",
        "orgNr": "",
        "firstName": "",
        "lastName": "",
        "personNumber": "",
        "phone": "",
        "address": "",
        "postnr": "",
        "postort": "",
        "kommun": "",
        "page": 1
    })
    rj = r.json()

    print(f"{'we hidden lmao' if rj['person']['hits'][0]['hidden'] else 'lmao we doxed sadge'}")

    if (not rj['person']['hits'][0]['hidden']):
        rz = requests.post(f"{config['discord']['webhook_url']}", json={
            "content": f"{config['discord']['ping']}",
            "embeds": [
                {
                "author": {
                    "name": "anti-sweden dox",
                    "icon_url": "https://cdn.7tv.app/emote/01J5W1A5ZG000CF26Z25SJ7JF8/3x.avif"
                },
                "description": "Swedish government has successfully doxxed us!!!",
                "fields": [
                    {
                    "name": "who?",
                    "value": f"{person}"
                    }
                ],
                "thumbnail": {
                    "url": "https://cdn.7tv.app/emote/01J5W1A5ZG000CF26Z25SJ7JF8/3x.avif"
                },
                "color": "12590120"
                }

        ]
        })