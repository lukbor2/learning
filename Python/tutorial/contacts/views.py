from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.core.urlresolvers import reverse
from . import forms

from contacts.models import Contact, Address

class ListContactView(ListView):
    model = Contact
    template_name = 'contact_list.html'

class CreateContactView(CreateView):
    model = Contact
    template_name = 'edit_contact.html'
    # fields = '__all__' #this is required in version of django I am using
    form_class = forms.ContactForm
    
    def get_success_url(self):
        return reverse('contacts-list')
    
    def get_context_data(self, **kwargs):
        
        context = super(CreateContactView, self).get_context_data(**kwargs)
        context['action'] = reverse('contacts-new')
        
        return context
        
class UpdateContactView(UpdateView):
    model = Contact
    template_name = 'edit_contact.html'
    # fields = '__all__' #this is required in version of django I am using
    form_class = forms.ContactForm
    
    def get_success_url(self):
        return reverse('contacts-list')
    
    def get_context_data(self, **kwargs):
        
        context = super(UpdateContactView, self).get_context_data(**kwargs)
        context['action'] = reverse('contacts-edit', kwargs = {'pk': self.get_object().id})
        
        return context
        
class DeleteContactView(DeleteView):
    model = Contact
    template_name = 'delete_contact.html'
    fields = '__all__' #this is required in version of django I am using
    
    def get_success_url(self):
        return reverse('contacts-list')
    
class ContactView(DetailView):
    model = Contact
    template_name = 'contact.html'
    
class EditContactAddressView(UpdateView): # TODO: Write a CreateView to create some addresses.
    model = Contact
    template_name = 'edit_addresses.html'
    forms_class = forms.ContactAddressFormSet
    fields = '__all__' #this is required in version of django I am using
    
    def get_success_url(self):
        # redirect to contact view
        return self.get_object().get_absolute_url()