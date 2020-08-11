import sqlite3
import json


counter = 0
with open('Journals_list_complete.json', 'r') as journals_list:
    dic = json.load (  journals_list )

conn = sqlite3.connect ( '../Django_maglet/maglet/db.sqlite3' )
c = conn.cursor ()


for item in dic:
    c.execute ( '''INSERT INTO recom_api_journal_info(journal_id,title,owner,release_period,general_subject,exclusive_subject,url,cover_address,rank_status,organizer)
                 VALUES(?,?,?,?,?,?,?,?,?,?)''', (item["ID"],item["title"],item["owner"],item["release_period"],item["general_subject"],item["exclusive_subject"],item["url"],item["cover_address"],item["rank_status"],item["organization"],) )
    conn.commit ()
    counter += 1
    print(counter)

# close the connection
conn.close ()
