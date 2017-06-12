from django.contrib import admin
from models import Potenciales, Actividad
from django import forms 
from django.forms import ModelForm, CheckboxInput
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

class PotencialCheckboxFieldForm(forms.ModelForm):
	model = Potenciales
	widgets = {
	'adultos': CheckboxInput
	}


# MODIFICACIONES HECHAS EN EL ADMIN DE LOS INLINES DE LOS MODELOS
class ActividadInline(admin.TabularInline):
	model = Actividad
	extra = 0


# MODIFICACIONES HECHAS AL ADMIN DE LOS MODELOS

class ActividadAdmin(admin.ModelAdmin):
	list_display = ['cliente_registro', 'fecha_contacto', 'medio_contactado', 'fecha_prox_contacto', 'actividad_registrada','volver_contactar']
	search_fields = ['cliente_registro', 'medio_contactado']
	list_filter = ('fecha_contacto', 'fecha_prox_contacto', 'volver_contactar', 'medio_contactado')
	form = ActividadSelect2WidgetForm

class PotencialAdmin(admin.ModelAdmin):
	list_display = ['nombre', 'apellido', 'celular','telefono_h', ('valencia'), 'usuario']
	search_fields = ['nombre', 'apellido']
	fieldsets = [
	(None, {'fields': [()]}),
	('DATOS DEL CLIENTE POTENCIAL', {'fields': [('usuario', 'nombre', 'apellido'), ('celular', 'telefono_h'), 
		'personas', 'cantidad_p', 'adultos', ('valencia','zona'), 'medio_contactado']})]
	inlines = [ActividadInline]



# REGISTRO DE LOS MODELOS PARA SU PUBLICACION

admin.site.register(Potenciales, PotencialAdmin)
admin.site.register(Actividad, ActividadAdmin)