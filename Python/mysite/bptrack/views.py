from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#from django.core.urlresolvers import reverse, reverse_lazy
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.views import View


from bptrack.models import Patient, BP_Measure
from . import forms


class PatientList(ListView):
    model = Patient
    template_name = 'bptrack_home.html'

    # Instead of using the standard context name object_list, I am setting my
    # own name for clarity
    context_object_name = 'all_patients'

class PatientDetail(DetailView):
    # General Note: the detail view seems to automatically expect the primary
    # key of the model passed via the url.
    # I don't have to do anything special to filter the object corresponding to
    # the primary key.

    model = Patient
    template_name = 'bptrack_patient_detail.html'

    context_object_name = 'patient_detail'

    #Adding home to the context which holds the link to the home page so I can
    #use it in the html template.
    #Instead of doing this, I could have used the url tag directly in the html
    #template.
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

    # As I am defining the queryset, the queryset superseds the model (which is not even specified).
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
    Things learnt about the DeleveView:
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

    #TODO: understand how to trigger and use the validation of the form in
    #these class based views.
    #Check if / how to use the form_valid method.

class PatientListSearch(ListView):
    model = Patient
    template_name = 'bptrack_PatientSearch_v2.html'

    """
    In order to access the request.GET I need to use self. But self can be used only inside a method.
    In this case the method is queryset, which works well because it is the method where I filter the objects to display.
    """

    def queryset(self):
        errors = []
        # q is the name given to the search parameter.  When the search page is
        # loaded for the first time with url /search
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

    def post(self, request):
        selected_ids = request.POST.getlist('selected_for_action')
        object_list = Patient.objects.filter(pk__in = selected_ids)
        # getlist always returns a list of value.  It makes sense to use it
        # here because all checkboxes in the html file have the same name.
        # Therefore, selected_ids is a list of the ids of the patients and
        # using the __in works.
        count = object_list.count()
        if object_list.count() < 1:
            return HttpResponse('No record selected.')
        else:
            object_list.delete()
            return render(request, 'bptrack_PatientSearch.html', {'object_list': Patient.objects.all()})
            # Note how I use the same template used by the list view, but I
            # render it with the list of patients after the one(s) selected
            # have been deleted.
            # I use render and I pass object_list in the context because that's
            # what the template expects.

class SelectedPatientDelete(View):
    """
    Problems so far. The views is called as expected, but the get method, not the post, is used.
    I have to figure out how to change the html so the post method is used.
    """
    def post(self, request):
        return HttpResponse('Hi, from SelectedPatientDelete View!! This is POST method')

    def get(self, request):
        return HttpResponse('Hi, from SelectedPatientDelete View!! This is GET method')

class PatientBPMeasureCreate(CreateView):
    """
    Implementing this CreateView without using a form because I don't need any specific validation, so I keep it simple.
    """

    model = BP_Measure
    # In the fields I do not include patient (the foreign key) because I take it from the parameter in the URL.
    fields = ['bp_measure_date','bp_measure_min', 'bp_measure_max', 'bp_measure_pulse', 'bp_measure_time_of_day', 'bp_measure_note']

    def get_context_data(self, **kwargs):
        context = super(PatientBPMeasureCreate, self).get_context_data(**kwargs)

        # Extend the context to include the patient object.
        context['selected_patient_id'] = self.kwargs['fk']
        return context
    # I overwrite the form_valid method to set the patient foreign key equal to the patient the user has selected which is represented
    # by the fk parameter in the url.
    # In other words, this is how I don't ask the user to specify a patient when the form is filled in, because the patient comes from the url.
    def form_valid(self, form):
        form.instance.patient = Patient.objects.get(pk = int(self.kwargs['fk']))
        return super(PatientBPMeasureCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('bptrack:patient-bpmeasures', args={self.kwargs['fk']})
