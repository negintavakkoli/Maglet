import random
import json

with open("Journals_list_complete.json", "r") as n:
    nn = json.load(n)
random.shuffle(nn)
print(nn[-5:])