# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 21:31:30 2018

@author: Asus
"""
import urllib.parse
import requests
import json
#import os
from bs4 import BeautifulSoup
import glob
fff=open("Journals_Behdasht.txt",'w')
g=glob.glob("research/*.txt")
with open('Journals_list.json', 'r') as journals_list:
    healthcare_dic = json.load ( journals_list )
print(type(healthcare_dic))
j = 20000

while len(g)>0:
    files=g.pop(0)
    f=open(files,'r')
    s=f.read()
    f.close()
    soup=BeautifulSoup(s)
    for tag in soup.findAll("div",{"class":"Tbl"}):
        title=tag.findNext("div",{"class":"TblCel col_19 rtl right"})
        if(title is None):
            title=tag.findNext("div",{"class":"TblCel col_19 ltr left f15"})
        title=title.text.strip().lstrip().rstrip()
        #print(title)
        owner=tag.findNext("div",{"class":"TblCel col_19 hide_small"})
        owner=owner.text.strip().lstrip().rstrip()
        #print(owner)
        publisher=tag.findNext("div",{"class":"TblCel col_18 hide_small"})
        publisher=publisher.text.strip().lstrip().rstrip()
        #print(publisher)
        last_issue=tag.findNext("div",{"class":"TblCel col_10 persian pad1"})
        last_issue=last_issue.text.strip().lstrip().rstrip()
        #ss334=tag.findNext("img",{"class":"cover"})
        sstemp=tag.findNext("div",{"class":"TblBlock col_17"})
        cover_address=sstemp.findNext("img")
        try:
            q = cover_address["src"]
            tq= urllib.parse.urljoin("https://journals.msrt.ir/",q)
            cover_address=tq.split("/")[-1]
            """with open('covers/'+cover_address, 'wb') as handle:
                response = requests.get(tq, stream=True)
                if not response.ok:
                    print response
                for block in response.iter_content(1024):
                    if not block:
                        break
                    handle.write(block)"""
            #print "!!!!!!"
        except:
            cover_address = "-"
        #print(cover_address)
        #ss4=tag.findNext("a",href=True)  
        url=tag.findNext("div",{"class":"InfoBar rounded"})
        url=url.find("a")
        try:
            url=url["href"]
        except:
            url="-"
        #ss4=ss4.findNext("div",{"class":"InfoBarTxt"})
        sstemp=tag.findNext("div",{"class":"TblBlock col_30 left ltr ftahoma"})
        sstemp=sstemp.text
        
        
        pissn=sstemp.split("P-ISSN: ")[1].split("E-ISSN")[0].strip().lstrip().rstrip()
        eissn=sstemp.split("E-ISSN: ")[1].split("Indexing")[0].strip().lstrip().rstrip()
        indexing=sstemp.split("Indexing: ")[1].strip().lstrip().rstrip()
        
        
        sstemp1=tag.findNext("div",{"class":"TblBlock col_25 right"})
        rightcolumn = sstemp1.text.replace("\t","").replace("\n\n","\n").replace("\n\n","\n").replace("\n\n","\n").lstrip().rstrip()
        items1=rightcolumn.split("\n")
        #7 Baraye Pezeshki va 6 baraye oloom

        rank_status=items1[0].split(":")[1].strip().lstrip().rstrip()
        release_period=items1[1].split(":")[1].strip().lstrip().rstrip()
        director=items1[2].split(":")[1].strip().lstrip().rstrip()
        chief_editor=items1[3].split(":")[1].strip().lstrip().rstrip()
        approval_date=items1[4].split(":")[1].strip().lstrip().rstrip()
        validity_date=items1[5].split(":")[1].strip().lstrip().rstrip()
        general_subject=items1[6].split(":")[1].strip().lstrip().rstrip()

        sstemp2=sstemp1.findNext("div",{"class":"TblBlock col_25 right"})
        leftcolumn = sstemp2.text.replace("\t","").replace("\n\n","\n").replace("\n\n","\n").replace("\n\n","\n").lstrip().rstrip()
        items2=leftcolumn.split("\n")
        #if(len(items2)!=5):
        #    items2.pop(4)
        #if((len(items2)!=5) or (len(items1)!=6)):
        #    print title
        #    print rightcolumn
        #    print leftcolumn
        #Bish az 5 bood khane 4 bayad hazf shavad

        language=items2[0].split(":")[1].strip().lstrip().rstrip()
        software=items2[1].split(":")[1].strip().lstrip().rstrip()
        partner=items2[2].split(":")[1].strip().lstrip().rstrip()
        address=items2[3].split(":")[1].strip().lstrip().rstrip()
        exclusive_subject=items2[-1].split(":")[1].strip().lstrip().rstrip()
        ministry="2"

        healthCare_journal = {
            "ID": j ,
            "title": title ,
            "owner": owner ,
            "release_period": release_period ,
            "general_subject": general_subject ,
            "exclusive_subject": exclusive_subject ,
            "url": url ,
            "cover_address": cover_address ,
            "organization": "HealthCare"
        }
        healthcare_dic.append ( healthCare_journal )
        j += 1
        if(url=="-"):
            pass
        #else:
          #  fff.write(url+"\t"+language.encode("utf8")+"\t"+software.encode("utf8")+"\n")
fff.close()
with open('Journals_list_complete.json', 'w') as journals_list:
    healthcare_dic = json.dump ( healthcare_dic , journals_list )
