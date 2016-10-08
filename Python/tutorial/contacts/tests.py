from django.test import TestCase

from contacts.models import Contact

class ContactsTests(TestCase):
    """Contact Model Tests"""
    
    def test_str(self):
        contact = Contact(first_name='John', last_name='Smith')
        
        self.assertEquals(
            str(contact),
            'John Smith'
            )