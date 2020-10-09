import json

#Read parks.json file and store it as parks
with open('parks.json', 'r') as f:
    parks = json.load(f)

print(parks)