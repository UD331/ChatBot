import Word_Analysis
import Songs

s = input("Please enter words\n")

analysis = Word_Analysis.interpreter(s)
print(analysis)
score = 2
feeling = ""
#Select highest score
for i in analysis:
    if analysis.get(i) < score:
        score = analysis.get(i)
        feeling = i

payload = Songs.get_payload(feeling)
print(payload)
obj = Songs.jprint(payload)
print(obj)
Songs.getSong(obj)

