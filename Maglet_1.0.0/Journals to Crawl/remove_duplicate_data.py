# -*- coding: utf-8 -*-

import glob
import pickle

abstract_files = glob.glob("Journals_XML/*.ABSTRACT")

for x in abstract_files:
    with open( x, "rb") as tmp:

        abstract_item = pickle.load(tmp)

    for i in range (len(abstract_item)):
        set_abstract_main = set(abstract_item[i].split(" "))

        for j in range (i+1,len(abstract_item)):
            set_abstract = set(abstract_item[j].split(" "))
            set_abstract_intersection = set_abstract_main.intersection(set_abstract)
            set_abstract_intersection_len = len(set_abstract_main.intersection(set_abstract))
            set_abstract_union = set_abstract_main.union(set_abstract)
            set_abstract_union_len = len(set_abstract_main.union(set_abstract))
            abstract_jaccard_rate = set_abstract_intersection_len/set_abstract_union_len


            if abstract_jaccard_rate > 0.7:

                print("------------------------")
                print(abstract_jaccard_rate)
                print(abstract_item[i])
                print(abstract_item[j])
                print("------------------------")


