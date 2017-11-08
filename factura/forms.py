from django.forms import ModelForm, CheckboxInput
from models import Facturas
from django import forms
from django.forms import ModelForm, Textarea
from django.forms.widgets import CheckboxInput, TextInput, NumberInput, SelectDateWidget, DateInput, DateTimeInput
from django.contrib.admin.widgets import AdminDateWidget
from django_select2.forms import Select2Widget
from suit.widgets import SuitDateWidget, AutosizedTextarea, SuitTimeWidget, SuitSplitDateTimeWidget



class FacturaForm(ModelForm):
    class Meta:
        model = Facturas
        fields = [
            'fac_cliente',
            'fac_fecha',
            'fac_name',
            'fac_rif',
            'fac_tlf',
            'dir_fac',
            'servicio',
            'base_imponible',
            'iva',
            'total'

        ]
        widgets = {
            'fac_cliente': Select2Widget(attrs={'class': 'django-seles2 form-control'}),
            'fac_fecha': DateTimeInput(attrs={'class': 'form-control'}),
            'fac_name': TextInput(attrs={'class': 'form-control'}),
            'fac_rif': TextInput(attrs={'class': 'form-control'}),
            'fac_tlf': TextInput(attrs={'class': 'form-control'}),
            'dir_fac': TextInput(attrs={'class': 'form-control'}),
            'servicio': Select2Widget(attrs={'class': 'django-seles2 form-control'}),
            'base_imponible' : Select2Widget(attrs={'class': 'django-seles2 form-control'}),

        }