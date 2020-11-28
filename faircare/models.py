from django.db import models

# Create your models here.



class Medication(models.Model):
    medicine_name = models.CharField(max_length=200)

    def __str__(self):
        return self.medicine_name


class Procedure(models.Model):
    procedure_name = models.CharField(max_length=200)

class MedicationPrice(models.Model):
    medicine_name = models.ForeignKey(
        Medication, related_name="medication_price", on_delete=models.CASCADE)
    price = models.FloatField(max_length=200)
    state = models.CharField(max_length=2)



class ProcedurePrice(models.Model):
    procedure_name = models.ForeignKey(
        Procedure, related_name="procedure_price", on_delete=models.CASCADE)
    procedure_price = models.FloatField(max_length=200)
    state = models.CharField(max_length=2)