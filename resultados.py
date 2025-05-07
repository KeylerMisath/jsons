import json 

with open("C:\\Users\\306\\Downloads\\champions.json", "r", encoding="utf-8") as file:
    data = json.load(file)

for i in data[0]["Partidos"]:
    print(i["local"], "vs", i["visitante"], i["goles"])
    print(i["resultado"])

