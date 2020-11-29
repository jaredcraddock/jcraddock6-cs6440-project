from django import forms
from .models import Medication, Procedure

from localflavor.us.forms import USStateSelect

class MedicationViewForm(forms.Form):

    medication = forms.ModelChoiceField(queryset=Medication.objects.distinct('medicine_name'))


    def __init__(self, *args, **kwargs):
        super(MedicationViewForm, self).__init__(*args, **kwargs)





class MedicationDataSubmitForm(forms.Form):

    medication = forms.ModelChoiceField(queryset=Medication.objects.distinct('medicine_name'))



    medication_price = forms.CharField(max_length=100)
    medication_state = forms.CharField(widget=USStateSelect)

    def __init__(self, *args, **kwargs):
        super(MedicationDataSubmitForm, self).__init__(*args, **kwargs)




class ProcedureDataSubmitForm(forms.Form):

    procedure = forms.ModelChoiceField(
        queryset=Medication.objects.all(),
        empty_label="Select Procedure")


    procedure_price = forms.CharField(max_length=100)
    procedure_state = forms.CharField(max_length=200)

    def __init__(self, *args, **kwargs):
        super(ProcedureDataSubmitForm, self).__init__(*args, **kwargs)

