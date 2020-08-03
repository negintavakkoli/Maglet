from rest_framework import serializers
from .models import journal_info

class JournalSerializer(serializers.Serializer):
    title = serializers.CharField ( required = False , allow_blank = True , max_length = 200 )
    owner = serializers.CharField ( required = False , allow_blank = True , max_length = 200 )
    general_subject = serializers.CharField ( required = False , allow_blank = True , max_length = 200 )
    exclusive_subject = serializers.CharField ( required = False , allow_blank = True , max_length = 200 )
    organizer = serializers.CharField ( required = False , allow_blank = True , max_length = 200 )
    rank_status = serializers.CharField ( required = False , allow_blank = True , max_length = 200 )
    url = serializers.CharField ( required = False , allow_blank = True , max_length = 200 )
    """class Meta:
        model = journal_info
        fields = ('journal_id', 'title', 'owner')"""


class QuerySerializer(serializers.Serializer):
    abstract = serializers.CharField(max_length = 5000)
    title = serializers.CharField(max_length = 50 , required = False)
