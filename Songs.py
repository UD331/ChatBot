import requests

def lastfm_get(payload):
    # define headers and URL
    headers = {'user-agent': 'Udayan Pandey'}
    url = 'https://ws.audioscrobbler.com/2.0/'

    # Add API key and format to the payload
    payload['api_key'] = ''
    payload['format'] = 'json'

    response = requests.get(url, headers=headers, params=payload)
    return response
