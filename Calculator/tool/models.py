from django.db import models

# Create your models here.
class Calculator(models.Model):
    result = models.CharField(max_length=30)

