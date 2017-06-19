from django import forms 
from django.forms import ModelForm, CheckboxInput
from models import Potenciales, Actividad
from django import forms
from django.forms import ModelForm, Textarea
from django.forms.widgets import CheckboxInput
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
			'zona'
		]
		widgets = {
			'adultos': CheckboxInput(attrs={'class':'checkbox'})
		}

