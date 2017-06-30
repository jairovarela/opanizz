from django.contrib import admin
from models import Contratado, Beneficiario
from django import forms 
from django.forms import ModelForm, CheckboxInput
from django_select2.forms import Select2Widget
from suit.widgets import SuitDateWidget, AutosizedTextarea, SuitTimeWidget, SuitSplitDateTimeWidget
# Register your models here.

# MODIFICACIONES A LOS INLINES DE LOS MODELOS DE LAS APPS

class BeneficiarioInline(admin.StackedInline):
	model = Beneficiario
	extra = 0


# MODIFICACIONES A LOS FORM DE LOS ADMINS DE LAS APPS

class ContratadoSelect2widgetForm(forms.ModelForm):
	class Meta:
		model = Contratado
		exclude = []
		field = ('cliente', )
		widgets = {
		'cliente': Select2Widget,
		'fecha_n': SuitDateWidget,
		'direccion': AutosizedTextarea(attrs={'rows': 6, 'class': 'input-xlarge'}),
		'punto_referencia': AutosizedTextarea(attrs={'rows': 6, 'class': 'input-'}),

		}

class BeneficiarioForm(forms.ModelForm):
	class Meta:
		model = Beneficiario
		exclude = []
		field = ('contratado',)
		widgets = {
		'contratado': Select2Widget,
		}

# MODIFICACIONES A LOS MODELOS DE LOS ADMIN DE LAS APPS

class ContratadoAdmin(admin.ModelAdmin):
	search_fields = ['cedula', 'cliente_id__nombre', 'cliente_id__apellido', 'edad']
	list_display_links = ['cliente']	
	list_display = ['numcontrato', 'cliente', 'edad','cedula', 'telefono_o']
	fieldsets= [ 
		(None, {'fields': [()]}),
		('CLIENTE A CONTRATAR', {'fields': ['cliente']}),
		('DATOS PERSONALES DEL CLIENTE', {'fields': [('cedula', 'fecha_n'), 'edad', 'telefono_o', 'rif']}),
		('DATOS DE BUSQUEDA', {'fields': [('estado', 'municipio', 'parroquia'), ('sector', 'nombre_sector'), ('ubicacion', 'nombre_ubicacion'),
			('vivienda', 'nombre_vivienda'),('piso', 'numero'), ('punto_referencia'), ]}),
		(None, {'fields': [()]}),
		('DATOS DE SALUD', {'fields': [('cancer', 'diabetes'), ('enfermedad_corazon', 'presion_arterial'),('enfermedad_renal',
			'enfermendad_mental'),'enfermedades_importantes',('salud','peso','estatura'),('enfermedad_respiratoria',
			'enfermedad_digestivo'),('enfermedad_circulatorio','otras_enfermedades')]}),
		('SERVICIO A CONTRATAR', {'fields': ['servicio' ]}),
			]
	
	inlines = [BeneficiarioInline]
	form = ContratadoSelect2widgetForm

class BeneficiaarioAdmin(admin.ModelAdmin):
	list_display = ['contratado', 'nombre', 'apellido', 'fecha_n']
	form = BeneficiarioForm
	fieldsets= [ 
		(None, {'fields': [()]}),
		('CLIENTE DEL CONTRATO', {'fields': ['contratado']}),
		('DATOS PERSONALES DEL BENEFICIARIO', {'fields': [('nombre', 'apellido', 'cedula'), ('fecha_n', 'edad'),('telefono','email')]}),
		(None, {'fields': [()]}),
		('DATOS DE SALUD DEL BENEFICIARIO', {'fields': [('beneficiario_cancer', 'beneficiario_diabetes'), ('beneficiario_enfermedad_corazon', 'beneficiario_presion_arterial'),('beneficiario_enfermedad_renal',
			'beneficiario_enfermendad_mental'),'beneficiario_enfermedades_importantes',('beneficiario_salud','beneficiario_peso','beneficiario_estatura'),('beneficiario_enfermedad_respiratoria',
			'beneficiario_enfermedad_digestivo'),('beneficiario_enfermedad_circulatorio','beneficiario_otras_enfermedades')]}),
			]


admin.site.register(Contratado, ContratadoAdmin)
admin.site.register(Beneficiario, BeneficiaarioAdmin)