from __future__ import unicode_literals

from django.db import models

class Servicios(models.Model):
	nombre = models.CharField(max_length=20, verbose_name='Nombre')
	descripcion = models.CharField(max_length=200, blank=True, verbose_name='Descripcion del Servicio')
	precio = models.IntegerField(null=True)
	contrato = models.BooleanField(default=False, verbose_name='Contrato', help_text='Marque si el el servicio lleva contrato')


	class Meta:
		verbose_name='Servicio'
		verbose_name_plural='Servicios'

	def __unicode__(self):
		return '%s - %s' % (self.nombre, self.descripcion)
