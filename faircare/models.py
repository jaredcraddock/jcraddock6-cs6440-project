from django.db import models

# Create your models here.



class Medication(models.Model):
    medicine_name = models.CharField(max_length=200)

class Procedure(models.Model):
    procedure_name = models.CharField(max_length=200)

class City(models.Model):
    city = models.CharField(max_length=200)


class MedicationPrice(models.Model):
    medicine_name = models.ForeignKey(
        Medication, related_name="medication_price", on_delete=models.CASCADE)
    price = models.CharField(max_length=200)
    city = models.ForeignKey(
        City, related_name="medication_city", on_delete=models.CASCADE)

class ProcedurePrice(models.Model):
    procedure_name = models.ForeignKey(
        Procedure, related_name="procedure_price", on_delete=models.CASCADE)
    procedure_price = models.CharField(max_length=200)
    city = models.ForeignKey(
        City, related_name="procedure_city", on_delete=models.CASCADE)