from django.contrib import admin
from django import forms 
from django.forms import ModelForm, CheckboxInput
from django_select2.forms import Select2Widget
from suit.widgets import SuitDateWidget, AutosizedTextarea, SuitTimeWidget, SuitSplitDateTimeWidget
from models import MedioContacto, MediosActividad, ZonasValencia, Estado, Municipio, Parroquia,	Sector, Vivienda, Ubicacion

# Register your models here.

class MunicipioAdmin(admin.ModelAdmin):
	list_display = ['estado', 'municipio']
	search_fields = ['municipio', 'estado__estado']

admin.site.register(MedioContacto)
admin.site.register(MediosActividad)
admin.site.register(ZonasValencia)
admin.site.register(Estado)
admin.site.register(Municipio, MunicipioAdmin)
admin.site.register(Parroquia)
admin.site.register(Sector)
admin.site.register(Vivienda)
admin.site.register(Ubicacion)


