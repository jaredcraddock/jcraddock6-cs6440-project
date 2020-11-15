from django.db import models

# Create your models here.



class Medication(models.Model):
    medicine_name = models.CharField(max_length=200)

