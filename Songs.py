import requests
import json


def lastfm_get(payload):
    # define headers and URL
    headers = {'user-agent': 'Udayan Pandey'}
    url = 'https://ws.audioscrobbler.com/2.0/'

    # Add API key and format to the payload
    payload['api_key'] = '7921b4b4bfa5aa3d685c70de8a3eefc6'
    payload['format'] = 'json'

    response = requests.get(url, headers=headers, params=payload)
    return response


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    return text

r = lastfm_get({'method': 'tag.getTopTracks',
                'tag': 'happy'})
text = jprint(r.json()['tracks']['track'])

t = text.split("url")
n = 2
l = list()
while(n < len(t)):
    b = t[n].split('"')
    l.append(b[2])
    n+=2

print(l)
