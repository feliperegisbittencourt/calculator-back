from django.db import models
import datetime

# Create your models here.
class Calculator(models.Model):
    tag_pi = models.CharField('Tag PI', blank=True, max_length=200)
    TimeStamp = models.DateTimeField('TimeStamp', default=datetime.date.today)
    Value = models.FloatField('Value', default=0, blank=False)