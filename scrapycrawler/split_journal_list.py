import json

with open("Journals_list_complete.json", "r") as journals_list:
    journals_list = json.load(journals_list)



chunks = [journals_list[x:x+100] for x in range(0, len(journals_list), 100)]
print(len(chunks),len(journals_list))
print(len(chunks[-1]))
counter =1
for index , item in enumerate(chunks):
    with open("Journal_lists/Journals_list_complete_"+str(index)+".json" , "w") as f:
        json.dump(item,f)
