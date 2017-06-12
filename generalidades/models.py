from __future__ import unicode_literals

from django.db import models

class MedioContacto(models.Model):
	medio_cliente = models.CharField(max_length=30)

	class Meta:
		verbose_name = 'Medio de Contacto'
		verbose_name_plural = 'Medios de Contacto'

	def __unicode__(self):
		return self.medio_cliente

class MediosActividad(models.Model):
	medio_actividad = models.CharField(max_length=200)

	class Meta:
		verbose_name = 'Medio de contacto para Actividad'
		verbose_name_plural = 'Medios de Contacto para Actividades'

	def __unicode__(self):
		return self.medio_actividad

class ZonasValencia(models.Model):
	zonas = models.CharField(max_length=25)

	class Meta:
		verbose_name='Zona de Valencia'
		verbose_name_plural='Zonas de Valencia'

	def __unicode__(self):
		return self.zonas

class Estado(models.Model):
	estado = models.CharField(max_length=20)

	class Meta:
		verbose_name='Estado'
		verbose_name_plural='Estados'

	def __unicode__(self):
		return self.estado

class Municipio(models.Model):
	estado = models.ForeignKey(Estado)
	municipio = models.CharField(max_length=30)

	class Meta:
		verbose_name='Municipio'
		verbose_name_plural='Municipios'

	def __unicode__(self):
		return self.municipio

class Parroquia(models.Model):
	municipio = models.ForeignKey(Municipio)
	parroquia = models.CharField(max_length=100)

	class Meta:
		verbose_name='Parroquia'
		verbose_name_plural='Parroquias'

	def __unicode__(self):
		return self.parroquia

class Sector(models.Model):
	sector = models.CharField(max_length=30, blank=True)

	class Meta:
		verbose_name='Sector'
		verbose_name_plural='Sectores'

	def __unicode__(self):
		return self.sector

class Vivienda(models.Model):
	tipo = models.CharField(max_length=30, blank=True)

	class Meta:
		verbose_name='Vivienda'
		verbose_name_plural='Viviendas'

	def __unicode__(self):
		return self.tipo

class Ubicacion(models.Model):
	ubicacion = models.CharField(max_length=50)

	class Meta:
		verbose_name='Ubicacion'
		verbose_name_plural='Ubicaciones'

	def __unicode__(self):
		return self.ubicacion