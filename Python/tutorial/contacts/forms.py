from django import forms
from django.core.exceptions import ValidationError
from django.forms.models import inlineformset_factory

from contacts.models import (Contact, Address,)

ContactAddressFormSet = inlineformset_factory(Contact, Address, fields = '__all__' )

class ContactForm(forms.ModelForm):
    
    confirm_email = forms.EmailField(
        label = "Confirm email",
        required=True,
        )
        
    class Meta:
        model = Contact
        fields = '__all__' #this is required in version of django I am using
    def __init__(self, *args, **kwargs):
            
        if kwargs.get('instance'):
            email = kwargs['instance'].email
            kwargs.setdefault('initial', {})['confirm_email'] = email
        
        return super(ContactForm, self).__init__(*args, **kwargs)
        
    def clean(self):
        if(self.cleaned_data.get('email') != self.cleaned_data.get('confirm_email')):
            raise ValidationError("Emails must match!!")
        return self.cleaned_data