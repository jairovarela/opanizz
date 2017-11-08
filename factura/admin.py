from django.contrib import admin
from models import Facturas
from forms import FacturaForm
from contratos.models import Contratado

# MODIFICACIONES HECHAS AL ADMIN DE LOS MODELOS


# Register your models here.

class FacturaInline(admin.StackedInline):
    model = Facturas
    extra = 1
    max_num = 1
    fieldsets= [
        (None, {'fields': [('fac_name')]}),
        (None, {'fields': [('fac_rif')]}),
        (None, {'fields': [('dir_fac')]}),
        (None, {'fields': [('fac_tlf')]}),

    ]

class FacturaAdmin(admin.ModelAdmin):
    list_display_links = ['num_fac', 'fac_cliente']
    list_display = ['num_fac', 'fac_cliente', 'fac_name', 'fac_rif', 'dir_fac', 'fac_tlf', 'servicio']
    search_fields = ['num_fact', 'dir_fac', 'fac_name', 'fac_rif', 'fac_tlf', 'fac_to', 'num_fac',
                     'fac_client_id__cliente__nombre', 'fac_client_id__cliente__apellido']
    fieldsets= [
    (None, {'fields': [()]}),
    ('ESCOJA CLIENTE PARA AGREGAR DATOS', {'fields': [('fac_cliente', 'fac_to')]}),
    ('DATOS DE FACTURACION', {'fields': ['fac_name', 'fac_rif', 'dir_fac', 'fac_tlf']})
    ]
    form = FacturaForm



admin.site.register(Facturas, FacturaAdmin)