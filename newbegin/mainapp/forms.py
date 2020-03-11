from django import forms
from .models import Contact_Model, Enquire_Course_Model

class Contact_form(forms.ModelForm):
    class Meta:
        model = Contact_Model
        fields = ("full_name","email","phone","contacting_for","message")

class Enquire_Course_Form(forms.ModelForm):
    class Meta:
        model = Enquire_Course_Model
        fields = "__all__"