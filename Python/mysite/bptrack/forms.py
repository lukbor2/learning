from django import forms

class PatientForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    date_of_birth = forms.DateField()
    age = forms.IntegerField()
    email = forms.EmailField()

