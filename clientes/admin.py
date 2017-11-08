from django.contrib import admin
from models import Potenciales, Actividad
from forms import PotencialesForm, ActividadSelect2WidgetForm

#Inlines

class ActividadInline(admin.TabularInline):
	model = Actividad
	extra = 0


# MODIFICACIONES HECHAS AL ADMIN DE LOS MODELOS

class ActividadAdmin(admin.ModelAdmin):
	list_display = ['cliente_registro', 'fecha_contacto', 'medio_contactado', 'fecha_prox_contacto', 'actividad_registrada','volver_contactar']
	search_fields = ['cliente_registro', 'medio_contactado']
	list_filter = ('fecha_contacto', 'fecha_prox_contacto', 'volver_contactar', 'medio_contactado')
	form = ActividadSelect2WidgetForm

class PotencialesAdmin(admin.ModelAdmin):
	list_display = ['user','nombre', 'apellido', 'celular','telefono_h']
	search_fields = ['nombre', 'apellido', 'user']
	fieldsets = [
		(None, {'fields': [()]}),
		('USUARIO DEL CLIENTE POTENCIAL', {'fields': ['user']}),
		('DATOS DEL CLIENTE POTENCIAL', {'fields': [('nombre', 'apellido'), ('celular', 'telefono_h')]}),
		('DATOS FAMILIARES', {'fields': [('personas', 'cantidad_p', 'adultos')]}),
		('DATOS DE UBICACION', {'fields': [('estado','municipio','parroquia')]})
	]
	form = PotencialesForm
	inlines = [ActividadInline]

admin.site.register(Potenciales, PotencialesAdmin)
admin.site.register(Actividad)