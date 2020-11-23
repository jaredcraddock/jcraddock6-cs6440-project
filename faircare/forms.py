from django import forms
from .models import Medication, Procedure

class MedicationDataSubmitForm(forms.Form):
    medication = forms.ModelChoiceField(
        queryset=Medication.objects.all(),
        empty_label="Select Medication")
    medication_price = forms.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        super(MedicationDataSubmitForm, self).__init__(*args, **kwargs)




class ProcedureDataSubmitForm(forms.Form):

    procedure = forms.ModelChoiceField(
        queryset=Medication.objects.all(),
        empty_label="Select Procedure")


    procedure_price = forms.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        super(ProcedureDataSubmitForm, self).__init__(*args, **kwargs)

