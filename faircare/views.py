from django.shortcuts import render
from fhirclient import client
import fhirclient.models.procedure as proced
import fhirclient.models.medication as med
from django.template import loader
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from .models import ProcedurePrice, MedicationPrice
from .forms import MedicationDataSubmitForm, ProcedureDataSubmitForm
# Create your views here.



class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def home_view(request):

    settings = {
        'app_id': 'faircare',
        'api_base': 'http://hapi.fhir.org/v/r4/fhir'
    }
    smart = client.FHIRClient(settings=settings)

    search = med.Medication.where(struct={'_include': '*'})
    medications = search.perform_resources(smart.server)

    for m in medications:
        m.as_json()



    template = loader.get_template('home.html')



    medication_submit_form = MedicationDataSubmitForm()
    if request.method == 'POST':



        medication_submit = MedicationPrice(medication_name=request.procedure_name,
                                          medication_price=request.procedure_price, city=request.city)
        medication_submit.save()

    procedure_submit_form = ProcedureDataSubmitForm()
    if request.method == 'POST':



        procedure_submit = ProcedurePrice(procedure_name=request.procedure_name, procedure_price=request.procedure_price,city=request.city)
        procedure_submit.save()

    context = {
        'medications': medications,
        'medication_submit_form': medication_submit_form,
        'procedure_submit_form': procedure_submit_form

    }

    return HttpResponse(template.render(context, request))



