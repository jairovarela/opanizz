from __future__ import unicode_literals
from django.db import models
from contratos.models import Contratado
from administracion.models import Servicios



class Facturas(models.Model):
    num_fac = models.AutoField(primary_key = True, verbose_name = 'Numero de Factura', editable=False)
    fac_cliente = models.ForeignKey(Contratado, verbose_name = 'Contrato', on_delete=models.CASCADE)
    fac_to = models.BooleanField(default = False, verbose_name = 'Facturar a nombre del Cliente', help_text = 'Se tomaran los datos del Cliente para Facturar')
    fac_fecha= models.DateTimeField(max_length= 100, null=True, blank=True,verbose_name='Fecha de la Factura')
    fac_name = models.CharField(max_length = 100, blank = True, null = True, verbose_name = 'Nombre o Razon Social')
    fac_rif	= models.CharField(max_length = 15, blank = True, verbose_name = 'R.I.F')
    dir_fac = models.CharField(max_length = 150, blank = True, verbose_name = 'Direccion Fiscal')
    fac_tlf = models.IntegerField(blank = True, null = True, verbose_name = 'Telefono de Habitacion')
    servicio = models.ForeignKey(Servicios, blank=True, null=True,verbose_name='Servicio Contratado')
    base_imponible = models.FloatField(blank=True, null=True, verbose_name='Base Imponible de la Factura')
    iva = models.DecimalField(blank=True, null=True, max_digits=100, decimal_places=2, verbose_name='IVA de la Factura')
    total = models.DecimalField(blank=True, null=True,max_digits=100, decimal_places=2, verbose_name='Total de la Factura')

    class Meta:
        verbose_name = 'Factura'
        verbose_name_plural = 'Datos de la Facturacion'

    def __unicode__(self):
        return ' %s' % self.num_fac