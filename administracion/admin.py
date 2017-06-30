from django.contrib import admin
from models import Servicios

class ServicioAdmin(admin.ModelAdmin):
	list_display = ['nombre', 'descripcion', 'precio', 'duracion', 'contrato']

admin.site.register(Servicios, ServicioAdmin)

# Register your models here.
