from django.db import models

# Create your models here.


class SampleTable(models.Model):
    sampleid = models.CharField(max_length=90)
    sample_name = models.CharField(max_length=60)
