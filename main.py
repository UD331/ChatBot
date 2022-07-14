import Word_Analysis
import Songs

s = input()

analysis = Word_Analysis.interpreter(s)

#Select highest score

payload = Songs.get_payload()

obj = Songs.jprint(payload)

Songs.getSong(obj)



