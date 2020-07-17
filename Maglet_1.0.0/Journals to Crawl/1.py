import json
pp = open('Journals_list.json', 'r')

j = json.load(pp)
print(type(j))
for item in j:
    print(item["owner"])