from django.test import TestCase
from django.test.client import Client
from django.test.client import RequestFactory

from contacts.models import Contact
from contacts.views import ListContactView
from contacts import forms
from rebar.testing import flatten_to_dict # rebar is a library I installed with pip3. It is used to test forms.

class ContactsTests(TestCase):
    """Contact Model Tests"""
    
    def test_str(self):
        contact = Contact(first_name='John', last_name='Smith')
        
        self.assertEquals(
            str(contact),
            'John Smith'
            )
            
            
class EditContactFormTest(TestCase):
    
    def test_mismatch_email_is_invalid(self):

        form_data = flatten_to_dict(forms.ContactForm())
        form_data['first_name'] = 'Foo'
        form_data['last_name'] = 'Bar'
        form_data['email'] = 'foo@example.com'
        form_data['confirm_email'] = 'bar@example.com'

        bound_form = forms.ContactForm(data=form_data)
        self.assertFalse(bound_form.is_valid())
        
    def test_same_email_is_valid(self):

        form_data = flatten_to_dict(forms.ContactForm())
        form_data['first_name'] = 'Foo'
        form_data['last_name'] = 'Bar'
        form_data['email'] = 'foo@example.com'
        form_data['confirm_email'] = 'foo@example.com'

        bound_form = forms.ContactForm(data=form_data)
        self.assert_(bound_form.is_valid())