# import glob
# import json
# from urllib.parse import urlparse
# g = glob.glob("../../data/*.abstract")
#
# with open ( "../../Journals_list_complete.json" , "r" ) as f:
#     j = json.load ( f )
# list_journal_name = []
# for files in g:
#     name_of_journal = files.split("/")[-1]
#     try:
#         #cleanr = re.compile ( '.abstract' )
#         #name_of_journal = re.sub ( cleanr , ' ' , name_of_journal )
#         name_of_journal = name_of_journal.replace(".abstract","")
#         list_journal_name.append(name_of_journal)
#     except:
#         raise Exception ( 'I know Python!' )
# print(list_journal_name)
# for item in j:
#     url_item = item["url"]
#     url_netloc = urlparse(url_item).netloc.replace("/","_")
#     #print(url_netloc)
#     if str(url_netloc) in list_journal_name:
#         Journal_id = item["ID"]
#         print(Journal_id)
#         print(url_item)
#         print("-------------------------")