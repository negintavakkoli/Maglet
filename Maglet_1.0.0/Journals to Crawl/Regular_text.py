# -*- coding: utf-8 -*-


import re
import pickle
import bs4



def cleanhtml(raw_text):
    try:
        cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
        cleantext = re.sub ( cleanr , ' ' , raw_text )
        return cleantext
    except:
        raise Exception('I know Python!')


#
# my_normalizer = Normalizer()
# print(my_normalizer.normalize(Abstract_list[0]))

# for abstract in Abstract_list:
#     abstract_text = abstract
#     try:
#         # cleaned_abstract_text = cleanhtml(abstract_text)
#          cleaned_abstract_tex = abstract_text.normalize(abstract_text)
#     except Exception as rr:
#         continue
#     print(abstract_text)
#     print("**********")
#     print(cleaned_abstract_tex )
#     print("____")
# print(abstract_text)






    # for e in abstract_text:
    #     h = abstract_text.find("br")
    #     abstract_text = h.extract()

    # pattern = "(?:<style.+?>.+?</style>|<script.+?>.+?</script>|<(?:!|/?[a-zA-Z]+).*?/?>)"
    # g = re.search ( pattern , abstract_text )
    # #g = g.group ( 2 )
    # print(g)