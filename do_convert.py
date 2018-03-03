from datetime import datetime
import pprint


def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')


with open('buzzers.csv') as data:
    ignore = data.readline()
    flights = {}
    for line in data:
        k,v = line.strip().split(',')
        flights[k] = v
    
pprint.pprint(flights)
print()

fts = {convert2ampm(k): v.title() for k, v in flights.items()}
pprint.pprint(fts)

for dest in set(fts.values()):
    print(dest, '->', [k for k, v in fts.items() if v == dest])

when = {}
for dest in set(fts.values()):
    when[dest] = [k for k, v in fts.items() if v == dest]
pprint.pprint(when)

when = {dest: [k for k, v in fts.items() if v == dest] for dest in set(fts.values())}
pprint.pprint(when)

vowels = {'a', 'e', 'i', 'o', 'u'}
message = "Don't forget to pack your towel."

found = set()
for v in vowels:
    if v in message:
        found.add(v)
print(found)

found = {v for v in vowels if v in message}
print(found)