from django.db import models


# Create your models here.
class Interval(models.Model):
    id_interval = models.AutoField(primary_key=True)
    time_start = models.TimeField()
    time_end = models.TimeField()


class Cabinet(models.Model):
    id_cabinet = models.AutoField(primary_key=True)
    numder = models.IntegerField()
    special = models.CharField(max_length=50)
    doctor = models.CharField(max_length=100)


class Patient(models.Model):
    id_patient = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    snils = models.CharField(max_length=16)
    polis = models.CharField(max_length=16)
