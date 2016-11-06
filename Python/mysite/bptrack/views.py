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
    """
    In summary, these are the key things I learnt about the CreateView class-based view:
    - You need to declare the model and the fields of the model you want to use.
    - If nothing else is specified, the view will use as a default a template called modelname_form.hmtl (in this case patient_form.html).
      The template must be stored in a folder named appname/templates/appname (in this case bptrack/templates/bptrack).
    - The success_url attribute defines the URL to redirect to when the form is successfully processed.
    - I can specify a success_url in the view (see below). If not specified the view will use get_absolute_url() on the model object if available.
    - Like for any other view, an entry in urls.py must be specified.

    - The view automatically creates a ModelForm (in this example based on the model I specified) and the form is passed to the context which is usable in the html template without the need for me to do anything.
      Look at the docs here https://docs.djangoproject.com/en/1.10/topics/class-based-views/generic-editing/ where it explains something more about this step.

    """

    model = Patient
    fields = ['first_name', 'last_name','date_of_birth', 'age', 'email']
    # template_name = 'bptrack_patient_edit.html'
    # form_class = forms.PatientForm

    
    def get_context_data(self, **kwargs):
        context = super(PatientCreate, self).get_context_data(**kwargs)
        
        # Extend the context to include the url of the patient-list view.
        context['action'] = reverse('bptrack:patient-add')
        return context

   
    """
    Learning - the CreateView class has a success_url attribute which is the url used if the creation is successful.
    I had a lot of problems defining this attribute in a way which did not cause an error.
    Eventually it is working in this way:
    
    success_url = reverse_lazy ('bptrack:patient-list')
   
    I still do not understand why the same logic does not work using just reverse. In the tutorial reverse, not reverse_lazy is used and it works.
    Maybe it is something to try to understand. 

    Also using a hard coded url worked, but it is really not ideal:
    
    success_url = '/bptrack'
   
    """

def debug(request):
    pass

