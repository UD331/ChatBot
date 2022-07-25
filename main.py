import Word_Analysis
import Songs

s = input("Please enter words\n")

analysis = Word_Analysis.interpreter(s)
print(analysis)
score = -1
feeling = ""
#Select highest score
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
print(payload)
response = Songs.lastfm_get(payload)
obj = Songs.jprint(response.json())
print(obj)
Songs.getSong(obj)


