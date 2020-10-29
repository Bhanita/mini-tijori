from django import forms
from company.models import Person
class PersonForm(forms.ModelForm): 
    class Meta:
        model = Person
        exclude = []
