from django.forms import ModelForm, ValidationError
from bptrack.models import Patient

class PatientForm(ModelForm):
    """
    I am created a form based on the class ModelForm so I can re-use the fields defined
    in the corresponding model.
    Furthermore, with the form I can implement some custom validation.
    Custom validation is not really required in this app, but I wanted to try something.
    """
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'date_of_birth', 'age', 'email'] 

    def clean_last_name(self):
        """
        In order to validate a specific field I must override the method named clean_<fieldname>.
        The method shall always return the field's data whether it's correct or not.
         """
        data = self.cleaned_data['last_name'] #Remember that cleaned_data is a dictionary and returns a Python object, not the string which was entered in the form.
        if "Borghi" not in data:
            raise ValidationError("Patient must be a Borghi") #Stupid validation, just to try something....
        return data