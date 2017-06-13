from __future__ import unicode_literals
from django.db import models
from clientes.models import Potenciales
from generalidades.models import Estado, Municipio, Parroquia, Sector, Vivienda, Ubicacion
from administracion.models import Servicios

def incremental():
	ultimo_contratado= Contratado.objects.all().order_by('id').last()
	if not ultimo_contratado:
		return 'OPA-' + '0001'
	else:
		numcontrato = Contratado.objects.all().count()
		numcontrato = numcontrato + 0001
		return 'OPA-' + str(numcontrato)


class Contratado(models.Model):
	numcontrato = models.CharField(max_length=20, default=incremental, editable=False)
	cliente = models.ForeignKey(Potenciales)
	cedula = models.IntegerField(unique=True)
	edad = models.IntegerField(null = True)
	fecha_n = models.DateField(blank = True, verbose_name = 'Fecha de Nacimiento')
	rif = models.CharField(max_length = 15, verbose_name = 'R.I.F.', blank = True, help_text = 'Opcional si posee' )
	telefono_o = models.IntegerField(null = True, verbose_name = 'Telefono Oficina')
	estado = models.ForeignKey(Estado, verbose_name='Estado')
	municipio = models.ForeignKey(Municipio, verbose_name='Municipio')
	parroquia = models.ForeignKey(Parroquia, verbose_name='Parroquia')
	sector = models.ForeignKey(Sector, null=True, verbose_name='Sector')
	nombre_sector = models.CharField(max_length=50, blank=True, verbose_name='Nombre del Sector')
	ubicacion = models.ForeignKey(Ubicacion, verbose_name='Ubicacion', null=True)
	nombre_ubicacion = models.CharField(max_length=60, verbose_name='Nombre de la Ubicacion', blank=True)
	vivienda = models.ForeignKey(Vivienda, verbose_name='Vivienda', null=True)
	nombre_vivienda = models.CharField(max_length=100, blank=True, verbose_name='Nombre de la Vivienda')
	piso = models.CharField(max_length=10, blank=True)
	numero = models.IntegerField(null=True, blank=True)
	domicilio_laboral = models.CharField(max_length=200, blank=True)
	punto_referencia = models.CharField(max_length=250, blank=True, verbose_name='Punto de Referencia de busqueda')
	servicio = models.ManyToManyField(Servicios, verbose_name='Servicio a Contratar')
	meses = models.BooleanField(default=False, verbose_name='Contrato por 6 meses', help_text='Marque si el cliente desea contratacion semestral')
	ano = models.BooleanField(default=False, verbose_name='Contrato por 1 ano', help_text='Marque si el cliente desea contratacion anual')

	class Meta:
		verbose_name = 'Cliente a Contratar'
		verbose_name_plural = 'Contratos Generados'

	def __unicode__(self):
		return str(self.cliente)

class Beneficiario(models.Model):
	contratado = models.ForeignKey(Contratado, null = True)
	nombre = models.CharField(max_length = 255)
	apellido = models.CharField(max_length = 255)
	cedula = models.IntegerField(blank = True, null = True)
	email = models.EmailField(null=True, blank=True)
	edad = models.IntegerField(null=True, blank=True)
	fecha_n = models.DateField(verbose_name = 'Fecha de Nacimiento')
	telefono = models.IntegerField(blank = True, null = True)

	class Meta:
		verbose_name = 'Beneficiario'
		verbose_name_plural = 'Beneficiarios'

	def __unicode__(self):
		return '%s %s' % (self.nombre, self.apellido)
