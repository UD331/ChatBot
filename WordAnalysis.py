import requests

url = "https://api.apilayer.com/text_to_emotion"

payload = "Hey it's me Mario!".encode("utf-8")
headers= {
  "apikey": "zJuUtZiohldxWr07OrtL3ZCXwgon3YIE"
}

response = requests.request("POST", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text
print(result.split())
print(result)
