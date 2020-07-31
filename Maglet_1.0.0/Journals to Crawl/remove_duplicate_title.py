# -*- coding: utf-8 -*-

import glob
import pickle
import os
import sys


counter = 0
similarity_threshould = 0.9


# Globe TITLE files
title_file = glob.glob ( "Journals_XML/*.TITLE" )

for filename in title_file:

    # Create new TITLE directory as saving new list without duplicate
    name_of_directory = filename.split ( "/" )[-1]
    title_uniqe_address = name_of_directory + ".UNIQE"
    print ( title_uniqe_address )
    title_uniqe_list = []

    #Read TITLE files
    with open ( filename , "rb" ) as tmp:
        try:
            title_item = pickle.load ( tmp )
        except:
            print ( "Error. Couldn't open the pickle file" )
            continue

    # Identify duplicate TITLE by jaccard rate

    for i in range ( len ( title_item ) ):
        set_title_main = set ( title_item[i].split ( " " ) )
        flag = 0

        for j in range ( i + 1 , len ( title_item ) ):
            set_title = set ( title_item[j].split ( " " ) )
            set_title_intersection = set_title_main.intersection ( set_title )
            set_title_intersection_len = len ( set_title_main.intersection ( set_title ) )
            set_title_union = set_title_main.union ( set_title )
            set_title_union_len = len ( set_title_main.union ( set_title ) )
            title_jaccard_rate = set_title_intersection_len / set_title_union_len

            if  title_jaccard_rate > similarity_threshould:

                flag = 1
                break
        if flag == 0:
           title_uniqe_list.append(title_item[i])
    print(len(title_uniqe_list))

    #Save UNIQE titles
    with open(os.path.join("Journals_XML", title_uniqe_address), "wb") as tempfile:
        pickle.dump(title_uniqe_list,tempfile)
