from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse, reverse_lazy

from bptrack.models import Patient, BP_Measure
from . import forms


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

    #Adding home to the context which holds the link to the home page so I can use it in the html template.
    #Instead of doing this, I could have used the url tag directly in the html template.
    def get_context_data(self, **kwargs):
        context = super(PatientDetail, self).get_context_data(**kwargs)
        context['home_page'] = reverse('bptrack:patient-list') 
        return context

    
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
    fields = ['first_name', 'last_name','date_of_birth', 'email'] # I don't need the age field because it will be calculated.
    # template_name = 'bptrack_patient_edit.html'
    # form_class = forms.PatientForm
       
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

class PatientDelete(DeleteView):
    """
    Things learn about the DeleveView:
    - the class has the object in the context, but not a form .
    - unless specified via template_name attribute, the class is using a default template called modelname_confirm_delete.hmtl (in this case patient_confirm_delete.html).
      The template must be stored in a folder named appname/templates/appname (in this case bptrack/templates/bptrack).

    """
    model = Patient
    success_url = reverse_lazy('bptrack:patient-list')

def debug(request):
    pass

class PatientUpdate(UpdateView):
    """
    The logic of the UpdateView is very similar to the one of the Create View.
    It needs the model and the fields to be used.
    By default it uses the same template as the CreateView (i.e. modelname_form.hmtl, in this case patient_form.html, and
    the template must be located in folder appname/templates/appname, in this case bptrack/templates/bptrack).
    By default the success url is the get_absolute_url of the model.
    I have defined that in the Patient so it works.

    """


    model = Patient
    fields = ['first_name', 'last_name','date_of_birth','email'] # I don't need the age field because it will be calculated.

class PatientCreate_v2(CreateView):
    """
    v2 of the PatientCreate view.
    In this version I am using a ModelForm which performs some custom validation.
    """
    model = Patient
    
    # As I am using the forom_class, fields must NOT be specified.
    #fields = ['first_name', 'last_name','date_of_birth', 'age', 'email']
    
    # template_name = 'bptrack_patient_edit.html'
    
    form_class = forms.PatientForm

    #TODO: understand how to trigger and use the validation of the form in these class based views.
    #Check if / how to use the form_valid method.

class PatientListSearch(ListView):
    model = Patient
    template_name = 'bptrack_PatientSearch.html'

    """
    In order to access the request.GET I need to use self. But self can be used only inside a method.
    In this case the method is queryset, which works well because it is the method where I filter the objects to display.

    """

    def queryset(self):
        errors = []
        # q is the name given to the search parameter. When the search page is loaded for the first time with url /search
        # there is no parameter, therefore I just return all the patients.

        if 'q' in self.request.GET:
            q = self.request.GET['q']
            if not q:
                errors.append('Enter a search term.')
                return Patient.objects.all()
            else:
                return Patient.objects.filter(last_name__icontains=q)
        else:
            return Patient.objects.all()
