from django import forms
from company.models import Person
class InvestorForm(forms.ModelForm): 
    class Meta:
        model = Person
        exclude = []
