import requests
import json

def lastfm_get(payload):
    headers = {'user-agent': 'Udayan Pandey'}
    url = 'https://ws.audioscrobbler.com/2.0/'
    
    payload['api_key'] = '7921b4b4bfa5aa3d685c70de8a3eefc6'
    payload['format'] = 'json'

    response = requests.get(url, headers=headers, params=payload)
    return response


r = lastfm_get({'method': 'chart.gettopartists'})


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(r.json())
jprint(r.json()['artists']['@attr'])

import time

responses = []

page = 1
total_pages = 99999 # this is just a dummy number so the loop starts

while page <= total_pages:
    payload = {
        'method': 'chart.gettopartists',
        'limit': 500,
        'page': page
    }

    # print some output so we can see the status
    print("Requesting page {}/{}".format(page, total_pages))
    # clear the output to make things neater

    # make the API call
    response = lastfm_get(payload)

    # if we get an error, print the response and halt the loop
    if response.status_code != 200:
        print(response.text)
        break

    # extract pagination info
    page = int(response.json()['artists']['@attr']['page'])
    total_pages = int(response.json()['artists']['@attr']['totalPages'])

    # append response
    responses.append(response)

    # if it's not a cached result, sleep
    if not getattr(response, 'from_cache', False):
        time.sleep(0.25)

    
    page += 1

r = lastfm_get({
    'method': 'artist.getTopTags',
    'artist':  'Lana Del Rey'
})

jprint(r.json())
