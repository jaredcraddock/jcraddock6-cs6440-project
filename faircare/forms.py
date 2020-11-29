from django import forms
from .models import Medication, Procedure

from localflavor.us.us_states import US_STATES

class MedicationViewForm(forms.Form):

    #medication_view = forms.ModelChoiceField(queryset=Medication.objects.all())
    medication_view = forms.ModelChoiceField(queryset=Medication.objects.distinct('medicine_name'))

    def __init__(self, *args, **kwargs):
        super(MedicationViewForm, self).__init__(*args, **kwargs)





class MedicationDataSubmitForm(forms.Form):

    #medication = forms.ModelChoiceField(queryset=Medication.objects.all())
    medication = forms.ModelChoiceField(queryset=Medication.objects.distinct('medicine_name'))



    medication_price = forms.CharField(max_length=100)
    state_choices = US_STATES
    medication_state = forms.ChoiceField(choices=state_choices)

    def __init__(self, *args, **kwargs):
        super(MedicationDataSubmitForm, self).__init__(*args, **kwargs)

