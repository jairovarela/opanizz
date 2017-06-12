from __future__ import unicode_literals
from django.db import models
from contratos.models import Contratado

class Factura(models.Model):
	num_fact = models.AutoField(primary_key = True, verbose_name = 'Numero de Factura')
	fac_client = models.ForeignKey(Contratado, verbose_name = 'Cliente')
	fac_to = models.BooleanField(default = False, verbose_name = 'Facturar a nombre del Cliente', help_text = 'Se tomaran los datos del Cliente para Facturar')
	fac_name = models.CharField(max_length = 100, blank = True, null = True, verbose_name = 'Nombre o Razon Social')
	fac_rif	= models.CharField(max_length = 15, blank = True, verbose_name = 'R.I.F')
	dir_fac = models.CharField(max_length = 150, blank = True, verbose_name = 'Direccion Fiscal')
	fac_tlf = models.IntegerField(blank = True, null = True, verbose_name = 'Telefono de Habitacion')

	class Meta:
		verbose_name = 'Dato'
		verbose_name_plural = 'Datos de Facturacion'

	def __unicode__(self):
		return ' %s' % (self.fac_client)