from __future__ import unicode_literals

from django.db import models

class DuracionServicios(models.Model):
	nombre= models.CharField(max_length=20 ,verbose_name='Cantidad de Tiempo')

	class Meta:
		verbose_name = 'Duracion del Servicio'
		verbose_name_plural = 'Duraciones de los Servicios'

	def __unicode__(self):
		return str(self.nombre)

class Servicios(models.Model):
	nombre = models.CharField(max_length=20, verbose_name='Nombre')
	descripcion = models.CharField(max_length=200, blank=True, verbose_name='Descripcion del Servicio')
	precio = models.IntegerField(null=True, blank=True, verbose_name='Precio del Servicio')
	precio_beneficiario = models.IntegerField(null=True, blank=True, verbose_name='Precio por cada Beneficiario')
	contrato = models.BooleanField(default=False, verbose_name='Contrato', help_text='Marque si el el servicio lleva contrato')
	duracion = models.ManyToManyField(DuracionServicios, verbose_name='Duracion del servicio')

	class Meta:
		verbose_name='Servicio'
		verbose_name_plural='Servicios'
	def __unicode__(self):
		return '%s - %s' % (self.nombre, self.descripcion)


