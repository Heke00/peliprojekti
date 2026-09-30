import json

with open('t1.json', 'r') as tiedosto:
    data_luettu = json.load(tiedosto)

print(data_luettu)