import json

with open(r"C:\Users\306\Downloads\ranking.json", "r", encoding="utf-8") as file:
    data = json.load(file)

for i in data["series"]:
    print(i["ranking"], ":", i["titulo"])

print("-------------")

for i in data["peliculas"]:
    print(i["ranking"], ":", i["titulo"])