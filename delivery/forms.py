from django import forms
from .models import Demand
from address.models import AddressField
from django.forms import ModelForm
from address.forms import AddressField
from ckeditor.widgets import CKEditorWidget
from django.utils.translation import ugettext_lazy as _
from phone_field import PhoneField

class DemandForm(ModelForm):
    class Meta:
        model = Demand
        fields = ['service', 'name', 'phone', 'autocomplete', 'email', 'description']

SERVICE_CHOICES =(
        ("Normal","Normal"),
        ("Express","Express"))

class DemandForm(forms.ModelForm):

    service = forms.ChoiceField(label=_('Type of delivery'), choices=SERVICE_CHOICES, widget=forms.Select(attrs={
        'placeholder': 'Service type',
        'class': 'form-control',
        'name': 'service',
    }))
    
    name = forms.CharField(label=_('Consignee name'), widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control',  
        'name': 'title', 
        'placeholder': 'Full name'
    }))
    
    
    phone = forms.CharField(label=_('Consignee phone'), widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control',  
        'name': 'phone', 
        'placeholder': 'Phone'
    }))

    
    autocomplete = AddressField(label=_('Consignee address'), widget=forms.TextInput(attrs={
        'class': 'form-control',  
        'name': "autocomplete", 
        'id':"autocomplete",
        'placeholder': 'Address'
    }))
    
    email =forms.EmailField(label=_('Consignee email'), widget=forms.TextInput(attrs={
        'class': 'form-control',  
        'name': "email", 
        'id':"email",
        'placeholder': 'Email'
    }))

    description = forms.CharField(widget=CKEditorWidget(attrs={
        'type': 'text',
        'class': 'form-controltext',  
        'name': 'description', 
        'placeholder': 'Description'
    }))

    class Meta:
        model = Demand
        fields = ['service', 'name', 'phone', 'autocomplete' , 'email', 'description']



