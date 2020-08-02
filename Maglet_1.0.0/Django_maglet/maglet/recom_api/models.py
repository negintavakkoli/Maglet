from django.db import models

# Create your models here.


class journal_info(models.Model):
    journal_id = models.IntegerField()
    title = models.CharField(null = True, max_length = 200)
    owner = models.CharField(null = True, max_length = 200)
    release_period = models.CharField(null = True, max_length = 200)
    general_subject = models.CharField(null = True, max_length = 200)
    exclusive_subject = models.CharField(null = True, max_length = 200)
    url = models.URLField(null = True, max_length = 200)
    cover_address = models.CharField(null = True, max_length = 200)
    rank_status = models.CharField(null = True, max_length = 50)
    organizer = models.CharField(null = True, max_length = 100)