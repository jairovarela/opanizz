from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from generalidades.models import MedioContacto, MediosActividad, ZonasValencia, Estado, Municipio, Parroquia

class Potenciales(models.Model):
	usuario = models.OneToOneField(User, verbose_name='Tu usuario', unique=True)
	nombre = models.CharField(max_length=255, verbose_name='Nombres', help_text = 'Nombres Completos', blank=True)
	apellido = models.CharField(max_length=255, verbose_name='Apellidos', help_text = 'Apellidos Completos', blank=True)
	medio_contactado = models.ForeignKey(MedioContacto, null=True, blank=True)
	celular = models.IntegerField(null=True, blank=True, verbose_name='Telefono Celular')
	telefono_h = models.IntegerField(null=True, blank=True, verbose_name='Telefono de Habitacion', help_text='Opcional si posee')
	personas = models.BooleanField(default=False, verbose_name='Posee personas a su cargo', help_text='Marque en caso de poseer')
	cantidad_p = models.IntegerField(default=0, null=True, verbose_name='Cantidad de personas a su cargo', blank=True)
	adultos = models.BooleanField(default = False, verbose_name='Adulto Mayor a su cargo', help_text='Marque en caso de poseer')
	valencia = models.BooleanField(default = False, verbose_name='Reside en Valencia', help_text='Marque de ser correcto')
	zona = models.ForeignKey(ZonasValencia, null=True, blank=True, verbose_name='Seleccione la zona donde reside')
	estado = models.ForeignKey(Estado, null=True, blank=True, verbose_name='Estado')
	municipio = models.ForeignKey(Municipio, null=True, blank=True, verbose_name='Municipio')
	parroquia = models.ForeignKey(Parroquia, null=True, blank=True, verbose_name='Parroquia')

	class Meta:
		verbose_name = 'Cliente Potencial'
		verbose_name_plural = 'Clientes Potenciales'

	def __unicode__(self):
		return '%s %s' % (self.nombre, self.apellido)

class Actividad(models.Model):
	cliente_registro = models.ForeignKey(Potenciales, verbose_name='Cliente Potencial')
	fecha_contacto = models.DateTimeField(null=True)
	medio_contactado = models.ForeignKey(MediosActividad, null=True, blank=True)
	actividad_registrada = models.CharField(max_length=255)
	volver_contactar = models.BooleanField(default=False, verbose_name='Volver a Contactar', help_text='Marcar en caso de volver a contactar a futuro')
	fecha_prox_contacto = models.DateTimeField(null=True)

	class Meta:
		verbose_name = 'Actividad de Cliente'
		verbose_name_plural = 'Actividades de Clientes'

	def __unicode__(self):
		return str(self.cliente_registro)
		