from django import forms
from .models import *
class itemForms(forms.ModelForm):
    class Meta:
        model= Items
        fields=['name','price']

class storeForms(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['name']

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name']

class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['name']


