from django.db import models



class locations(models.Model):
    station_name=models.CharField(max_length=250)
    latitude=models.FloatField()
    longitude=models.FloatField()
    def __str__(self):
        return self.title
# Create your models here.
