# -*- coding: utf-8 -*-

import xml.etree.cElementTree as ET
import glob
import pickle
import os
from hazm import Normalizer

counter = 1
folder_name = "XML_Solr"
tag_name = "abstract"
address_to_search = "Journals_XML/*.ABSTRACT.UNIQE"
#Globe ABSTRAC files
abstract_files = glob.glob(address_to_search)


for filename in abstract_files:
    with open(filename, "rb") as temp:
        abstract_list = pickle.load(temp)

    # Create new ABSTRACT files as saving new list without duplicate
    journal_id = filename.split("/")[1].split(".")[0]

    for item in abstract_list:
        try:
            root = ET.Element ( "add" )
            doc = ET.SubElement ( root , "doc" )

            ET.SubElement ( doc , "field" , name = "journal_id" ).text = journal_id
            normalizer = Normalizer ()
            item = normalizer.normalize(item)
            ET.SubElement ( doc , "field" , name = tag_name ).text = item

            tree = ET.ElementTree ( root )
            tree.write ( os.path.join("Journals_XML",folder_name, str(counter)+".xml" ) , "UTF-8")
            counter += 1
        except Exception as rr:
            print(rr)
            print ( "Cannot create xml file" )
            pass


