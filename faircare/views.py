from django.shortcuts import render
from fhirclient import client
import fhirclient.models.medication as med
from django.template import loader
from django.http import HttpResponse, JsonResponse
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from .models import MedicationPrice, Medication
from .forms import MedicationDataSubmitForm, MedicationViewForm
from django.core import serializers
from django.db.models import Avg
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import logout


# Create your views here.



class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def home_view(request):

    if not request.user.is_authenticated:
        return redirect('/')


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
            messages.success(request, 'Medication Data Submitted Successfully.')
            medication_submit.save()





    medication_view_form = MedicationViewForm()
    medication_view =""
    if request.method == 'POST' and 'medication_view' in request.POST:
        medication_view_form = MedicationViewForm(request.POST)

        if medication_view_form.is_valid():
            medication_view=medication_view_form['medication_view'].value()


    context = {
        'medications': medications,
        'medication_submit_form': medication_submit_form,
        'medication_view_form': medication_view_form,
        'medication_view':medication_view,

    }


    return HttpResponse(template.render(context, request))

def medicine_data_view(request):
    medication = request.GET["medication_view"]
    return JsonResponse(list(MedicationPrice.objects.filter(medicine_name_id=medication).values('state').order_by('state').annotate(price=Avg('price'))), safe=False)


def logout_view(request):
    logout(request)
    return redirect('/')



