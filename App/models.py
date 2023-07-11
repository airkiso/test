from django.db import models



class locations(models.Model):
    station_name=models.CharField(max_length=250)
    latitude=models.FloatField()
    longitude=models.FloatField()
    def __str__(self):
        return self.title
class PersonSalary(models.Model):
    age=models.PositiveBigIntegerField()
    salary=models.FloatField()
    education=models.CharField(max_length=128)
    def __str__(self):
        return self.title

# Create your models here.
