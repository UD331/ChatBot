import Word_Analysis
import Songs

s = input("Please enter words\n")

analysis = Word_Analysis.interpreter(s)
score = -1
feeling = ""
for i in analysis:
    if analysis.get(i) > score:
        score = analysis.get(i)
        feeling = i

genre = ''
if feeling == 'Happy':
    genre = 'Jazz'
elif feeling == 'Angry':
    genre = 'Punk'
elif feeling == 'Surprise':
    genre = 'Pop'
elif feeling == 'Sad':
    genre = 'Blues'
elif feeling == 'Fear':
    genre = 'Rock'

payload = Songs.get_payload(genre)
response = Songs.lastfm_get(payload)
obj = Songs.jprint(response.json())
Songs.getSong(obj)


