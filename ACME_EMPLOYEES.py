from datetime import datetime
from itertools import count

txt_path = input("Write the path to the file: ")

people = {}

with open(txt_path) as d:
    d = d.readlines()

for i in d:
    i = i.strip()
    name = i.split("=")[0] 
    week = {}
    for x in i.split("=")[1].split(","):
        week[x[:2]] = {"in": datetime.strptime(x[2:].split("-")[0].strip(), "%H:%M").time(),
                       "out": datetime.strptime(x[2:].split("-")[1].strip(), "%H:%M").time()}
    people[name] = week

result = {}

for person in people.keys():
    for other in people.keys():
        if person != other:
            for day in people[person]:
                if day in people[other].keys():
                    combination = sorted(set([person, other]))
                    combination.append(day)
                    if not "-".join(combination) in result.keys():
                        if people[person][day]["in"] >= people[person][day]["in"] and people[person][day]["out"] <= people[other][day]["out"]:
                            result["-".join(combination)] = 1
                            
                        elif people[other][day]["in"] >= people[people][day]["in"] and people[other][day]["out"] <= people[people][day]["out"]:
                            result["-".join(combination)] = 1

counts = {}        

for key in result:
    if key[:-3] not in counts.keys():
        counts[key[:-3]] = 1
    else:
        counts[key[:-3]] += 1

print(counts)
