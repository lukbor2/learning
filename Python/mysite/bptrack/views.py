from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from bptrack.models import Patient, BP_Measure
# from . import forms

from django.core.urlresolvers import reverse, reverse_lazy

class PatientList(ListView):
    model = Patient
    template_name = 'bptrack_home.html'

    # Instead of using the standard context name object_list, I am setting my own name for clarity
    context_object_name = 'all_patients'



class PatientDetail(DetailView):
    # General Note: the detail view seems to automatically expect the primary key of the model passed via the url.
    # I don't have to do anything special to filter the object corresponding to the primary key.
    
    model = Patient
    template_name = 'bptrack_patient_detail.html'
    
    context_object_name = 'patient_detail'
    
class PatientBPMeasure(ListView):
    """
    In this view I show the list of the measures filtered on a patient whose id is passed via the URL.
    Furthermore I make the patient data available in the context, so I can show these data in the template.
    """
    
    template_name = 'bptrack_patient_measures.html'
    context_object_name = 'patient_measure'
    
    def get_queryset(self):
        # First I get the patient object, not just the foreign key.
        self.patient = get_object_or_404(Patient, id=self.args[0])
        # Then I filter the queryset using the patient I just got.
        return BP_Measure.objects.filter(patient = self.patient)
    
    def get_context_data(self, **kwargs):
        context = super(PatientBPMeasure, self).get_context_data(**kwargs)
        
        # Extend the context to include the patient object.
        context['patient'] = self.patient
        return context

class PatientCreate(CreateView):
    model = Patient
    fields = ['first_name', 'last_name','date_of_birth', 'age', 'email']
    # template_name = 'bptrack_patient_edit.html'
    # form_class = forms.PatientForm

    """
    def get_context_data(self, **kwargs):
        context = super(PatientCreate, self).get_context_data(**kwargs)
        
        # Extend the context to include the url of the patient-list view.
        context['home'] = reverse_lazy('patient-list')
        return context

   """
    # Learning - the CreateView class has a success_url attribute which is the url used if the creation is successful.
    # I had a lot of problems defining this attribute in a way which did not cause an error.
    # Eventually it is working in this way:
    success_url = reverse_lazy ('bptrack:patient-list')
   
    # I still do not understand why the same logic does not work using just reverse. In the tutorial reverse, not reverse_lazy is used and it works.
    # Maybe it is something to try to understand. 

    # Also using a hard coded url worked, but it is really not ideal:
    # success_url = '/bptrack'

def debug(request):
    pass

