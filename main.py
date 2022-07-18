import Word_Analysis
import Songs

s = input("Please enter words")

analysis = Word_Analysis.interpreter(s)
score = 2
feeling = ""

for i in analysis:
    if analysis.get(i) < score:
        score = analysis.get(i)
        feeling = i

payload = Songs.get_payload(feeling)

obj = Songs.jprint(payload)

Songs.getSong(obj)



