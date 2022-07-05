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
    print(text)

r = lastfm_get({'method': 'tag.getTopTracks',
                'tag': 'happy'})
jprint(r.json())
