from django import forms 
from django.forms import ModelForm, CheckboxInput
from models import Potenciales, Actividad
from django import forms
from django.forms import ModelForm, Textarea
from django.forms.widgets import CheckboxInput, TextInput, NumberInput
from django_select2.forms import Select2Widget
from suit.widgets import SuitDateWidget, AutosizedTextarea, SuitTimeWidget, SuitSplitDateTimeWidget
# FORMULARIOS MODIFICADOS DE LOS MODELOS 

class ActividadSelect2WidgetForm(forms.ModelForm):
	class Meta:
		model = Actividad
		exclude = []
		field = ('cliente_registro',)
		widgets = {
		'fecha_contacto': SuitSplitDateTimeWidget,
		'accion_registrada': AutosizedTextarea(attrs={'rows': 4, 'class': 'input-xlarge'}),
		'fecha_prox_contacto': SuitSplitDateTimeWidget,
		'cliente_registro': Select2Widget,
		'volver_contactar': CheckboxInput,
		}

class PotencialesForm(ModelForm):
	class Meta:
		model = Potenciales
		fields =[
		    'nombre',
			'apellido',
			'medio_contactado',
			'celular',
			'telefono_h',
			'personas',
			'cantidad_p',
			'adultos',
			'valencia',
			'zona',
			'estado',
			'municipio',
			'parroquia',
		]
		widgets = {
			'zona': Select2Widget(attrs={'class':'django-select2 form-control'}),
			'estado': Select2Widget(attrs={'class':'django-select2 form-control'}),
			'municipio': Select2Widget(attrs={'class':'django-select2 form-control'}),
			'parroquia': Select2Widget(attrs={'class':'django-select2 form-control'}),
			'adultos': CheckboxInput(attrs={'class':'choice',}),
			'personas': CheckboxInput(attrs={'class':'choice'}),
			'nombre': TextInput(attrs={'class':'form-control', 'required':'True'}),
			'apellido': TextInput(attrs={'class':'form-control', 'required':'True'}),
			'celular': NumberInput(attrs={'class':'form-control'}),
			'telefono_h': NumberInput(attrs={'class': 'form-control'}),
			'valencia': CheckboxInput(attrs={'class':'choice'}),
			'cantidad_p': Select2Widget(attrs={'class':'django-select2 form-control'}),
		}

class PotencialesUpdateForm(ModelForm):
	class Meta:
		model = Potenciales
		fields =[
		    'nombre',
			'apellido',
			'medio_contactado',
			'celular',
			'telefono_h',
			'personas',
			'cantidad_p',
			'adultos',
			'valencia',
			'zona',
			'estado',
			'municipio',
			'parroquia',
		]
		widgets = {
			'zona': Select2Widget(attrs={'class':'django-select2 form-control'}),
			'estado': Select2Widget(attrs={'class':'django-select2 form-control'}),
			'municipio': Select2Widget(attrs={'class':'django-select2 form-control'}),
			'parroquia': Select2Widget(attrs={'class':'django-select2 form-control'}),
			'adultos': CheckboxInput(attrs={'class':'choice',}),
			'personas': CheckboxInput(attrs={'class':'choice'}),
			'nombre': TextInput(attrs={'class':'form-control'}),
			'apellido': TextInput(attrs={'class':'form-control'}),
			'celular': NumberInput(attrs={'class':'form-control'}),
			'telefono_h': NumberInput(attrs={'class': 'form-control'}),
			'valencia': CheckboxInput(attrs={'class':'choice'}),
			'cantidad_p': TextInput(attrs={'class':'form-control'}),
			'nombre': TextInput(attrs={'class':'form-control', 'required':'True'}),
			'apellido': TextInput(attrs={'class':'form-control', 'required':'True'}),
		}
		

