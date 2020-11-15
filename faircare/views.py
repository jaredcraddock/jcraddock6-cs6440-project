from django.shortcuts import render
from fhirclient import client
import fhirclient.models.procedure as p
import fhirclient.models.medication as med
from django.template import loader
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
# Create your views here.



class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def home_view(request):

    settings = {
        'app_id': 'faircare',
        'api_base': 'http://hapi.fhir.org/baseR4/'
    }
    smart = client.FHIRClient(settings=settings)

    search = med.Medication.where(struct={'_include': '*'})
    medications = search.perform_resources(smart.server)

    for m in medications:
        m.as_json()


    template = loader.get_template('home.html')

    context = {
        'medications': len(medications)

    }

    return HttpResponse(template.render(context, request))

