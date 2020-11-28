from django.shortcuts import render
from fhirclient import client
import fhirclient.models.procedure as proced
import fhirclient.models.medication as med
from django.template import loader
from django.http import HttpResponse, JsonResponse
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from .models import ProcedurePrice, MedicationPrice, Medication
from .forms import MedicationDataSubmitForm, ProcedureDataSubmitForm, MedicationViewForm
from django.core import serializers
from django.db.models import Avg
# Create your views here.



class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def home_view(request):

    settings = {
        'app_id': 'faircare',
        'api_base': 'https://launch.smarthealthit.org/v/r3/fhir'
    }
    smart = client.FHIRClient(settings=settings)

    search = med.Medication.where(struct={'_include': '*'})
    medications = search.perform_resources(smart.server)

    for m in medications:
        m.as_json()
        # Medication.objects.create(medicine_name=m.code.text)



    template = loader.get_template('home.html')



    medication_submit_form = MedicationDataSubmitForm()
    if request.method == 'POST':
        medication_submit_form = MedicationDataSubmitForm(request.POST)


        if medication_submit_form.is_valid():
            medication_submit = MedicationPrice(medicine_name=medication_submit_form.cleaned_data.get(
                'medication'),
                price=medication_submit_form.cleaned_data.get(
                'medication_price'), state=medication_submit_form.cleaned_data.get(
                'medication_state'))
            medication_submit.save()




    # procedure_submit_form = ProcedureDataSubmitForm()
    # if request.method == 'POST':
    #
    #
    #
    #     procedure_submit = ProcedurePrice(procedure_name=request.procedure_name, procedure_price=request.procedure_price,city=request.city)
    #     procedure_submit.save()

    medication_view_form = MedicationViewForm()
    medication =""
    if request.method == 'POST':
        medication_view_form = MedicationViewForm(request.POST)

        if medication_view_form.is_valid():
            medication=medication_view_form['medication'].value()


    context = {
        'medications': medications,
        'medication_submit_form': medication_submit_form,
        'medication_view_form': medication_view_form,
        'medication':medication
        # 'procedure_submit_form': procedure_submit_form

    }


    return HttpResponse(template.render(context, request))

def medicine_data_view(request):
    medication = request.GET["medication"]
    return JsonResponse(list(MedicationPrice.objects.filter(medicine_name_id=medication).values('state').order_by('state').annotate(price=Avg('price'))), safe=False)





