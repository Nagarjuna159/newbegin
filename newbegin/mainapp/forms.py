from django import forms
from .models import Contact_Model

class Contact_form(forms.ModelForm):
    class Meta:
        model = Contact_Model
        fields = ("full_name","email","phone","contacting_for","message")