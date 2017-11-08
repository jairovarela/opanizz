from django.contrib import admin
from models import Servicios
from models import DuracionServicios

# Register your models here.

class ServicioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion', 'precio', 'precio_beneficiario', 'contrato']
    search_fields = ['cliente_registro', 'medio_contactado']

class DuracionServicioAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre']

admin.site.register(Servicios, ServicioAdmin)
admin.site.register(DuracionServicios, DuracionServicioAdmin)
