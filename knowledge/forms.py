from dataclasses import field
from pyexpat import model
from django import forms
from .models import Manufacturer



class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = ["name"]



