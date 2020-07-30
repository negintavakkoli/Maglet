import xml.etree.ElementTree as ET
import os
import glob
import pickle
from Regular_text import cleanhtml
from parsivar import Normalizer
import parsivar
import re
import random

elemList = []
g = glob.glob("Journals_XML/*/*.xml")
i = 1
counter = 1
#random.shuffle(g)
text_normalizer = Normalizer()
for files in g:
    name_of_directory = files.split( "/" )[-2]
    abstract_address = name_of_directory+".ABSTRACT"
    title_address = name_of_directory + ".TITLE"
    keyword_address = name_of_directory + ".KEYWORD"



    #Check ABSTRACT files
    try:
        with open(os.path.join("Journals_XML",abstract_address), "rb") as pickelfile:
            abstract_list = pickle.load(pickelfile)
    except:
        abstract_list = []



    #Check TITLE files
    try:
        with open(os.path.join("Journals_XML", title_address), "rb") as titlefile:
            title_list = pickle.load(titlefile)
    except:
        title_list =[]

    #Check KEYWORD files
    try:
        with open(os.path.join("Journals_XML",keyword_address), "rb") as keywordsfile:
            keywords_list = pickle.load(keywordsfile)
    except:
        keywords_list = []

    with open (  files  , "r" ) as data_file:
        try:
            xmlTree = ET.parse ( data_file )
            i += 1
        except:
            print ( files )
            counter += 1
            continue



    # Show all Tags in XMLs files

    for elem in xmlTree.iter ():
        try:

            elemList.append ( elem.tag )
            elemList = list ( set ( elemList ) )
            #print(elemList)
        except:
            continue



    # Find Abstract of All XML files with the variety structure
    
    for elem in xmlTree.iter():
        try:
            abstract = elem.find ( 'abstract_fa').text
            try:
                abstract = cleanhtml(abstract)
                abstract_list.append(abstract)
            except:
                continue
        except AttributeError:
            try:
                abstract = elem.find ( 'OtherAbstract' ).text
                try:
                    abstract = cleanhtml ( abstract )
                    # abstract = abstract.normalize(abstract)
                    abstract_list.append ( abstract )
                except:
                    continue
            except AttributeError:
                try:
                    abstract = elem.find('ABSTRACTS').text
                    try:
                        abstract = cleanhtml ( abstract )
                        # abstract = text_normalizer.normalize(abstract)
                        abstract_list.append(abstract)
                    except:
                        continue
                except AttributeError:
                    try:
                        abstract = elem.find('abstract').text
                        try:
                            abstract = cleanhtml ( abstract )
                            # abstract = text_normalizer.normalize ( abstract )
                            abstract_list.append(abstract)
                        except:
                            continue
                    except AttributeError:
                        try:
                            abstract = elem.find('Abstract').text
                            try:
                                abstract = cleanhtml ( abstract )
                                # abstract = text_normalizer.normalize ( abstract )
                                abstract_list.append(abstract)
                            except:
                                continue
                        except AttributeError:
                             try:
                                 abstract = elem.find('ABSTRACTS').text
                                 try:
                                    abstract = cleanhtml ( abstract )
                                    # abstract = text_normalizer.normalize ( abstract )
                                    abstract_list.append(abstract)
                                 except:
                                    continue
                             except AttributeError:
                                pass
    print("--------------------")
    print(len(abstract_list))
    abstract_list = list(set(abstract_list))
    print(len(abstract_list))
    print ( "--------------------" )


    #Find Title of All XML files with the variety structure
    for elem in xmlTree.iter ():
        try:
            title = elem.find ( 'VernacularTitle' ).text
            try:

                title = cleanhtml(title)
                title_list.append(title)
            except:
                continue
        except AttributeError:
            try:
                title = elem.find ( 'article-title' ).text
                try:
                    title = cleanhtml ( title )
                    title_list.append(title)
                except:
                    continue
            except AttributeError:
                try:
                    title = elem.find ( 'title_fa' ).text
                    try:
                        title = cleanhtml ( title )
                        title_list.append(title)
                    except:
                        continue
                except AttributeError:
                    try:
                        title = elem.find('ArticleTitle').text
                        try:
                            title = cleanhtml ( title )
                            title_list.append ( title )
                        except:
                            continue
                    except AttributeError:
                        pass


    #
    # """Find Keywords of All XML files with the variety structure"""
    #
    # for elem in xmlTree.iter ():
    #     try:
    #         keyword = elem.find('KEYWORD').text
    #         keywords_list.append(keyword)
    #     except AttributeError:
    #         try:
    #             keyword = elem.find('Keywords').text
    #             keywords_list.append(keyword)
    #         except AttributeError:
    #             try:
    #                 keyword = elem.find ( './/Object[@Type="Keyword"]' ).text
    #                 keywords_list.append(keyword)
    #             except AttributeError:
    #                 pass

    #Creat ABSTRACT files
    with open(os.path.join ( "Journals_XML" , abstract_address ) , "wb") as pickelfile:
        pickle.dump ( abstract_list , pickelfile )


    #Creat TITLE files
    with open ( os.path.join ( "Journals_XML" , title_address ) , "wb" ) as titlefile:
        pickle.dump ( title_list , titlefile )


    # #Creat KEYWORDS files
    # with open( os.path.join("Journals_XML",keyword_address)) as keywordsfile:
    #     pickle.dump(keywords_list, keywordsfile)



"""for root, dirs, files in os.walk("Journals_XML"):
    for file in files:
        if file.endswith(".xml"):
            with open ( os.path.join(root, file) , "r" ) as data_file:
                try:
                    xmlTree = ET.parse ( data_file )
                except:
                    print(os.path.join(root, file))
                    continue
            for elem in xmlTree.iter ():
                elemList.append ( elem.tag )
            elemList = list ( set ( elemList ) )
            
            
            
   
            
print( i , counter )
"""

