import requests
import json
import random

def get_payload(text):
    return {'method': 'tag.getTopTracks',
                'tag': text}

def lastfm_get(payload):
    # define headers and URL
    headers = {'user-agent': 'Udayan Pandey'}
    url = 'https://ws.audioscrobbler.com/2.0/'

    payload['api_key'] = '7921b4b4bfa5aa3d685c70de8a3eefc6'
    payload['format'] = 'json'

    response = requests.get(url, headers=headers, params=payload)
    return response


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    return text


def getSong(text):
    t = text.split("url")
    n = 2
    l = list()
    while(n < len(t)):
        b = t[n].split('"')
        l.append(b[2])
        n+=2
    print(l)
    m = str(random.sample(l,1))
    m = m.replace('[', '').replace(']', '').replace("'", '')
    print(m)
