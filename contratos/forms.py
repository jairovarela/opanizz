from django import forms 
from django.forms import ModelForm, CheckboxInput
from models import Contratado
from django import forms
from django.forms import ModelForm, Textarea
from django.forms.widgets import CheckboxInput
from django_select2.forms import Select2Widget
from suit.widgets import SuitDateWidget, AutosizedTextarea, SuitTimeWidget, SuitSplitDateTimeWidget

class ContratosForm(ModelForm):
	class Meta:
		model = Contratado
		fields =[
			'cliente',
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
		]
		widgets = {
			
		}

