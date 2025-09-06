from django import forms
from .models import Patient, Visit

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['iin', "first_name", "last_name", "phone", "birth_date"]

class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = ['date', 'doctor', 'description', 'cost', 'is_paid']