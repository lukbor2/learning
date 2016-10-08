from django.test import TestCase
from django.test.client import Client
from django.test.client import RequestFactory

from contacts.models import Contact
from contacts.views import ListContactView

class ContactsTests(TestCase):
    """Contact Model Tests"""
    
    def test_str(self):
        contact = Contact(first_name='John', last_name='Smith')
        
        self.assertEquals(
            str(contact),
            'John Smith'
            )