from django.shortcuts import render
from rest_framework import viewsets
from .serializers import JournalSerializer , QuerySerializer
from .models import journal_info
# Create your views here.

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response





class JournalViewSet(viewsets.ModelViewSet):
    queryset = journal_info.objects.all().order_by('journal_id')
    serializer_class = JournalSerializer

def lookup(request):
    if request.method == "GET":
        ss = request.GET['title']
    else:
        print("POST")
    c = journal_info.objects.get(title = ss)
    return render(request,"firstpage.html",{"data":c})

def t1(request):
    return render ( request , "firstpage.html" )


@api_view(['GET', 'POST'])
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = journal_info.objects.all()
        serializer = JournalSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = QuerySerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.data["abstract"])
            ####find similar journals

            ###let's assume the similar journal is 10010
            c = journal_info.objects.get(journal_id = 10010)
            serializer = JournalSerializer ( c  )
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)