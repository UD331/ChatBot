import requests

def interpreter(load):
  url = "https://api.apilayer.com/text_to_emotion"

  payload = load.encode("utf-8")
  headers= {
    "apikey": "zJuUtZiohldxWr07OrtL3ZCXwgon3YIE"
  }

  response = requests.request("POST", url, headers=headers, data = payload)
  print(response.text)

  result = response.text
  result = result.replace('"', '')
  result = result.replace('{', '')
  result = result.replace('}', '')
  result = result.replace(',', '')
  r = result.split()
  c = 0
  d = dict()
  while(c < 10):
    d[r[c]] = float(r[c+1])
    c += 2
  return(d)

