import xml.etree.ElementTree as ET
import os
import glob
elemList = []
g = glob.glob("Journals_XML/*/*.xml")
i = 1
counter = 1
for files in g:
    with open ( os.path.join ( files ) , "r" ) as data_file:
        try:
            xmlTree = ET.parse ( data_file )
            i += 1
        except:
            print ( os.path.join ( files ) )
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
            print(abstract)
        except AttributeError:
            try:
                abstract = elem.find ( 'OtherAbstract' ).text
                print(abstract)
            except AttributeError:
                try:
                    abstract = elem.find('ABSTRACTS').text
                    print(abstract)
                except AttributeError:
                    try:
                        abstract = elem.find('abstract').text
                        print(abstract)
                    except AttributeError:
                        try:
                            abstract = elem.find('Abstract').text
                            print ( abstract )
                        except AttributeError:
                             try:
                                 abstract = elem.find('ABSTRACTS').text
                                 print ( abstract )
                             except AttributeError:
                                pass

 
    #Find Title of All XML files with the variety structure
    for elem in xmlTree.iter ():
        try:
            title = elem.find ( 'VernacularTitle' ).text
            print ( title )
        except AttributeError:
            try:
                title = elem.find ( 'article-title' ).text
                print ( title )
            except AttributeError:
                try:
                    title = elem.find ( 'title_fa' ).text
                    print ( title )
                except AttributeError:
                    pass




    """Find Keywords of All XML files with the variety structure"""

    for elem in xmlTree.iter ():
        try:
            keyword = elem.find ( 'KEYWORD' ).text
            print ( keyword )
        except AttributeError:
            try:
                keyword = elem.find ( 'keyword' ).text
                print ( keyword )
            except AttributeError:
                try:
                    keyword = elem.find ( './/Object[@Type="Keyword"]' ).text
                    print ( keyword )
                except AttributeError:
                    pass

'''


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
            elemList = list ( set ( elemList ) )"""
            
            
            
    abstract_tag = ['abstract_fa', 'OtherAbstract','OtherAbstract','ABSTRACTS','abstract','ABSTRACTS']
    for elem in xmlTree.iter ():
        try:
            abstract = elem.find( abstract_tag).text
            print(abstract)
        except AttributeError:
            pass
print( i , counter )

'''
