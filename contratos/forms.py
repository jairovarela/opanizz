from django import forms 
from django.forms import ModelForm, CheckboxInput
from models import Contratado, Beneficiario
from django import forms
from django.forms import ModelForm, Textarea
from django.forms.widgets import CheckboxInput, TextInput, NumberInput, SelectDateWidget, DateInput
from django.contrib.admin.widgets import AdminDateWidget
from django_select2.forms import Select2Widget
from suit.widgets import SuitDateWidget, AutosizedTextarea, SuitTimeWidget, SuitSplitDateTimeWidget
from betterforms.multiform import MultiModelForm



class BeneficiarioForm(forms.ModelForm):
	class Meta:
		model = Beneficiario
		exclude = []
		field = ('contratado',)
		widgets = {
		'contratado': Select2Widget,
		}


class ContratosForm(ModelForm):
	class Meta:
		model = Contratado
		fields =[
		    'cedula',
			'edad',
			'fecha_n',
			'rif',
			'telefono_o',
			'estado',
			'municipio',
			'parroquia',
			'sector',
			'nombre_sector',
			'ubicacion',
			'nombre_ubicacion',
			'vivienda',
			'nombre_vivienda',
			'piso',
			'numero',
			'domicilio_laboral',
			'punto_referencia',
			'servicio',
			'cancer', 
			'diabetes',
			'enfermedad_corazon',
			'presion_arterial', 
			'enfermedad_renal', 
			'enfermendad_mental', 
			'enfermedades_importantes',
			'salud',
			'peso',
			'estatura', 
			'enfermedad_respiratoria', 
			'indique_respiratoria', 
			'enfermedad_digestivo', 
			'indique_digestivo', 
			'enfermedad_circulatorio', 
			'indique_circulatorio', 
			'otras_enfermedades',
			'indique_otras', 
		]
		widgets = {
			'fecha_n': DateInput(attrs={'class':'form-control', 'placeholder':'dd/mm/aaaa'}),
			'cedula': TextInput(attrs={'class':'form-control'}),
			'edad': TextInput(attrs={'class':'form-control'}),
			'telefono_o': TextInput(attrs={'class':'form-control'}),
			'rif': TextInput(attrs={'class':'form-control'}),
			'estado': Select2Widget(attrs={'class':'django-seles2 form-control'}),
			'municipio': Select2Widget(attrs={'class':'django-seles2 form-control'}),
			'parroquia': Select2Widget(attrs={'class':'django-seles2 form-control'}),
			'sector': Select2Widget(attrs={'class':'django-seles2 form-control'}),
			'nombre_sector': TextInput(attrs={'class':'form-control'}),
			'ubicacion': Select2Widget(attrs={'class':'django-seles2 form-control'}),
			'nombre_ubicacion': TextInput(attrs={'class':'form-control'}),
			'vivienda': Select2Widget(attrs={'class':'django-seles2 form-control'}),
			'nombre_vivienda': TextInput(attrs={'class':'form-control'}),
			'piso': TextInput(attrs={'class':'form-control'}),
			'numero': TextInput(attrs={'class':'form-control'}),
			'punto_referencia': Textarea(attrs={'class':'form-control input-xlarge','rows': 4}),
			'salud': Select2Widget(attrs={'class':'django-seles2 form-control'}),
			'enfermedad_corazon': Select2Widget(attrs={'class':'django-seles2 form-control'}),
			'diabetes': Select2Widget(attrs={'class':'django-seles2 form-control'}),
			'cancer': Select2Widget(attrs={'class':'django-seles2 form-control'}),
			'presion_arterial': Select2Widget(attrs={'class':'django-seles2 form-control'}),
			'enfermedad_renal': Select2Widget(attrs={'class':'django-seles2 form-control'}),
			'enfermendad_mental': Select2Widget(attrs={'class':'django-seles2 form-control'}),
			'enfermedades_importantes': TextInput(attrs={'class':'form-control'}),
			'peso': TextInput(attrs={'class':'form-control'}),
			'estatura': TextInput(attrs={'class':'form-control'}),
			'enfermedad_respiratoria': Select2Widget(attrs={'class':'django-seles2 form-control'}),
			'indique_respiratoria': TextInput(attrs={'class':'form-control'}),
			'enfermedad_digestivo': Select2Widget(attrs={'class':'django-seles2 form-control'}),
			'indique_digestivo': TextInput(attrs={'class':'form-control'}),
			'enfermedad_circulatorio': Select2Widget(attrs={'class':'django-seles2 form-control'}),
			'indique_circulatorio': TextInput(attrs={'class':'form-control'}),
			'otras_enfermedades': Select2Widget(attrs={'class':'django-seles2 form-control'}),
			'indique_otras': TextInput(attrs={'class':'form-control'}),
			'servicio': Select2Widget(attrs={'class':'django-seles2 form-control'}),
		}


