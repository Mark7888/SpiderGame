import json
with open('./bin/config.json') as json_file:
    data = json.load(json_file)
print(data)
with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)
