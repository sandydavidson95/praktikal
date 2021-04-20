import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class newsStory(models.Model):
    heading = models.CharField(max_length= 50)
    pub_date = models.DateTimeField('date published')
    story_text = models.TextField('')


    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)