import requests

headers = {
    'user-agent': 'Udayan Pandey'
}

payload = {
    'api_key': '7921b4b4bfa5aa3d685c70de8a3eefc6',
    'method': 'chart.gettopartists',
    'format': 'json'
}

r = requests.get('https://ws.audioscrobbler.com/2.0/', headers=headers, params=payload)
print(r.status_code)
