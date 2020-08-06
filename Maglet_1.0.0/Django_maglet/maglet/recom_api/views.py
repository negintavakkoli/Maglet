from django.shortcuts import render
from rest_framework import viewsets
from .serializers import JournalSerializer , QuerySerializer
from .models import journal_info
import requests as RQ
from urllib.parse import urlencode, quote
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from hazm import Normalizer, word_tokenize
import pickle
import math

# Create your views here.

global idf
with open("dic_IDF_upperthan6.MODEL", "rb") as idf_file:
    idf = pickle.load(idf_file)

global solr_version
try:
    r = RQ.get("http://127.0.0.1:8983/solr/admin/info/system?wt=json")
    response = r.json()
    ver = response["lucene"]['solr-spec-version']
    solr_version = int(ver.split(".")[0])
except:
    solr_version = 6

class JournalViewSet(viewsets.ModelViewSet):
    queryset = journal_info.objects.all().order_by('journal_id')
    serializer_class = JournalSerializer


@api_view(['GET', 'POST'])
def recommendation(request):
    """
    List all code snippets, or create a new snippet.

    if request.method == 'GET':
        snippets = journal_info.objects.all()
        serializer = JournalSerializer(snippets, many=True)
        return Response(serializer.data)"""

    if request.method == 'POST':
        try:
            serializer = QuerySerializer(data=request.data)
        except:
            return Response ( status = status.HTTP_400_BAD_REQUEST )
            pass
        if serializer.is_valid():
            try:
                abstract_query = serializer.data["abstract"]
            except:
                return Response (status = status.HTTP_400_BAD_REQUEST)
                pass
            try:
                normalizer = Normalizer ()
                abstract_query = normalizer.normalize(abstract_query)
                abstract_words = word_tokenize(abstract_query)

            except:
                abstract_words = abstract_query.split(" ")
            try:
                tfidf = {}

                for word in list(set(abstract_words)):
                    if word in " ?.!/;:)(1234567890۱۲۳۴۵۶۷۸۹۰":
                        continue
                    tf = abstract_words.count(word)
                    try:
                        idf_temp = idf[word]
                    except:
                        idf_temp = 10
                    idf_word = math.log2 ( 144000 / idf_temp )
                    tfidf[word] = tf * idf_word
                tfidf_sorted = sorted ( tfidf.items () , key = lambda x: x[1] , reverse = True )
                tfidf_sorted = " ".join([x[0] for x in tfidf_sorted[:20]])
            except:
                tfidf_sorted = abstract_query
            ####find similar journals
            u1 = "http://127.0.0.1:8983/solr/Maglet/select?q="
            u2 = "&fl=journal_id&rows=300&wt=json"
            base_url = "http://127.0.0.1:8983/solr/Maglet/select?"
            if solr_version > 6:
                try:
                    url_request = urlencode({"q":quote(tfidf_sorted,safe = ''),"df":"abstract","fl":"journal_id","rows":300,"wt":"json"})
                except:
                    url_request = urlencode({"q":tfidf_sorted,"df":"abstract","fl":"journal_id","rows":300,"wt":"json"})
                url_request = base_url + url_request
            else:
                try:
                    url_request = u1+quote ( tfidf_sorted , safe = '' )+u2
                except:
                    url_request = u1 + tfidf_sorted + u2
            re = RQ.get(url_request)
            if re.status_code != 200:
                serializer = JournalSerializer ( {} , many = True )
                return Response ( serializer.data )
            else:
                final_result = re.json()
                d = final_result["response"]["docs"]
                journal_counter = {}
                for item in d:
                    try:
                        journal_counter[item["journal_id"][0]] += 1
                    except KeyError:
                        journal_counter[item["journal_id"][0]] = 1
                try:
                    title_query = serializer.data["title"]

                    if solr_version > 6:
                        url_request = urlencode (
                        {"df": "title" , "fl": "journal_id" , "q": title_query , "rows": 300 , "wt": "json"} )
                        url_request = base_url + url_request
                    else:
                        u2 = "&fl=journal_id&rows=300&wt=json"
                        try:
                            url_request = u1 + quote ( title_query , safe = '' ) + u2
                        except:
                            url_request = u1 + title_query  + u2
                    re = RQ.get ( url_request )
                    if re.status_code != 200:
                        serializer = JournalSerializer ( {} , many = True )
                        return Response ( serializer.data )
                    else:
                        final_result = re.json ()
                        d = final_result["response"]["docs"]
                        for item in d:
                            try:
                                journal_counter[item["journal_id"][0]] += 1
                            except KeyError:
                                journal_counter[item["journal_id"][0]] = 1
                except:
                    pass

                journal_counter_sorted = sorted ( journal_counter.items () , key = lambda x: x[1] , reverse = True )
                journal_counter_sorted = [x[0] for x in journal_counter_sorted[:10]]
                c = journal_info.objects.filter(journal_id__in = journal_counter_sorted)
                serializer = JournalSerializer ( c  , many=True)
                return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)