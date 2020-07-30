import random
import json
import pickle

# with open("Journals_list_complete.json", "r") as n:
#     nn = json.load(n)
# random.shuffle(nn)
# print(nn[-5:])


with open("Journals_XML/10001.ABSTRACT", "rb") as file:

    Abstract_list = pickle.load(file)
    print(Abstract_list)