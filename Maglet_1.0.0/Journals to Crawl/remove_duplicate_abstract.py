
# -*- coding: utf-8 -*-
import glob
import pickle
import os
import sys

similary_threshould = 0.6
#Globe ABSTRAC files
abstract_files = glob.glob("Journals_XML/*.ABSTRACT")

for filename in abstract_files:
    # Create new ABSTRACT files as saving new list without duplicate
    name_of_directory = filename.split( "/" )[-1]
    abstract_uniqe_address = name_of_directory+".UNIQE"
    print(abstract_uniqe_address)
    abstract_uniqe_list = []

    #Read ABSTRACT files
    with open( filename, "rb" ) as tmp:
        try:
            abstract_item = pickle.load(tmp)
        except:
            print("Error. Couldn't open the pickle file")
            continue

    #Identify duplicate ABSTRACT by jaccard rate
    for i in range (len(abstract_item)):
        set_abstract_main = set(abstract_item[i].split(" "))
        flag = 0

        for j in range (i+1,len(abstract_item)):
            set_abstract = set(abstract_item[j].split(" "))
            set_abstract_intersection = set_abstract_main.intersection(set_abstract)
            set_abstract_intersection_len = len(set_abstract_main.intersection(set_abstract))
            set_abstract_union = set_abstract_main.union(set_abstract)
            set_abstract_union_len = len(set_abstract_main.union(set_abstract))
            abstract_jaccard_rate = set_abstract_intersection_len/set_abstract_union_len

            if  abstract_jaccard_rate > similary_threshould:
                flag = 1
                break
        if flag == 0:
            abstract_uniqe_list.append(abstract_item[i])
    print(len(abstract_uniqe_list))
            # print("------------------------")
            # print(abstract_jaccard_rate)
            # print(abstract_item[i])
            # print(abstract_item[j])
            # print("------------------------")
    with open(os.path.join("Journals_XML",abstract_uniqe_address),"wb") as tempfile:
        pickle.dump(abstract_uniqe_list,tempfile)


