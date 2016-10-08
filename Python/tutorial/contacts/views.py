from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.core.urlresolvers import reverse

from contacts.models import Contact

class ListContactView(ListView):
    model = Contact
    template_name = 'contact_list.html'

class CreateContactView(CreateView):
    model = Contact
    template_name = 'edit_contact.html'
    fields = '__all__' #this is required in version of django I am using
    
    def get_success_url(self):
        return reverse('contacts-list')