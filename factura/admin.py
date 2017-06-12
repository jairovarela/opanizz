from django.contrib import admin
from models import Factura

# Register your models here.

class FacturaInline(admin.StackedInline):
	model = Factura
	extra = 1
	max_num = 1
	fieldsets= [
	(None, {'fields': [('fac_name')]}),
	(None, {'fields': [('fac_rif')]}),
	(None, {'fields': [('dir_fac')]}),
	(None, {'fields': [('fac_tlf')]}),
		
		]

class FacturaAdmin(admin.ModelAdmin):
	search_fields =  ['dir_fac', 'fac_name', 'fac_rif', 'fac_tlf', 'fac_to', 'num_fact', 
						'fac_client_id__cliente__nombre', 'fac_client_id__cliente__apellido']
	list_display = ['fac_client', 'fac_to', 'fac_name', 'fac_rif', 'dir_fac', 'fac_tlf']
	fieldsets= [ 
		(None, {'fields': [()]}),
		('ESCOJA CLIENTE PARA AGREGAR DATOS', {'fields': [('fac_client', 'fac_to')]}),
		('DATOS DE FACTURACION', {'fields': ['fac_name', 'fac_rif', 'dir_fac', 'fac_tlf']})
				]

	def save_model(self, request, obj, form, change):
		if obj.fac_client_id and obj.fac_to:
			datos = Contratado.objects.get(cliente = obj.fac_client_id)
			obj.fac_name = str(datos.cliente)
			obj.fac_rif = datos.cedula
			obj.dir_fac = datos.direccion
			obj.fac_tlf = datos.telefono_h
			obj.save()
		else:
			obj.save()

admin.site.register(Factura)