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




Salud = (
    ('Buena', 'Buena'),
    ('Regular', 'Regular'),
    ('Mala', 'Mala'),
)

Respiratorio = (
				('Bronquitis', 'Bronquietes Cronica'),
				('Tuberculosis', 'Tuberculosis'),
				('Asma', 'Asma'),
				('Otras', 'Otras' )
				)
Circulatorio = (
				('Trastorno en la presion arterial','Trastorno en la presion arterial '),
				('Alteraciones cardiacas','Alteraciones cardiacas'),
				('Angina de pecho','Angina de pecho '),
				('Infarto de miocardio','Infarto de miocardio'),
				('Otras enfermedades relacionados','Otras enfermedades relacionados:')
				)
Digestivo = (
			('Enfermedades del higado','Enfermedades del higado'),
			('Ulcera gastroduodenal','Ulcera gastroduodenal'),
			('Dispepcia','Dispepcia'),
			('Gastritis','Gastritis'),
			('Otras enfermedades','Otras enfermedades'),
			)
Otras = (
		('Reumatismo','Reumatismo'),
		('Artritis','Artritis'),
		('Hemorragias de cualquier indole','Hemorragias de cualquier indole'),
		('Perdida del conocimiento','Perdida del conocimiento'),
		('Enfermedades en los huesos','Enfermedades en los huesos'),
		('Convulsiones','Convulsiones'),
		('Paralisis','Paralisis'),

		)

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
	servicio = models.ForeignKey(Servicios, null=True, verbose_name='Servicio a Contratar')
	cancer = models.CharField(max_length=20, blank=True, verbose_name='Cancer')
	diabetes = models.CharField(max_length=20, blank=True, verbose_name='Diabetes')
	enfermedad_corazon = models.CharField(max_length=20, blank=True, verbose_name='Enfermedades del Corazon')
	presion_arterial = models.CharField(max_length=20, blank=True, verbose_name='Presion Arterial Alta')
	enfermedad_renal = models.CharField(max_length=20, blank=True, verbose_name='Enfermedades Renales')
	enfermendad_mental = models.CharField(max_length=20, blank=True, verbose_name='Enfermedades Mentales')
	enfermedades_importantes = models.CharField(max_length=250, blank=True, verbose_name='Otras Importantes')
	salud = models.CharField(max_length=7, choices=Salud, verbose_name='Estado de Salud', blank=True)
	peso = models.CharField(max_length=4, blank=True, verbose_name='Indique su peso')
	estatura = models.CharField(max_length=5, blank=True, verbose_name='Indique su Estatura')
	enfermedad_respiratoria = models.CharField(max_length=50, blank=True, choices=Respiratorio, verbose_name='Enfermedades Respiratorias', help_text='Indique si Padece')
	indique_respiratoria = models.CharField(max_length=150, blank=True, verbose_name='Indique', help_text='Especifique enfermedad Respirarotia')
	enfermedad_digestivo = models.CharField(max_length=50, blank=True, choices=Digestivo, verbose_name='Enfermedades Digestivas', help_text='Indique si Padece')
	indique_digestivo = models.CharField(max_length=150, blank=True, verbose_name='Indique', help_text='Especifique Enfermedad Digestiva')
	enfermedad_circulatorio = models.CharField(max_length=50, blank=True, choices=Circulatorio, verbose_name='Enfermedades Circulatorias', help_text='Indique si Padece')
	indique_circulatorio = models.CharField(max_length=150, blank=True, verbose_name='Indique', help_text='Especifique Enfermedad Circulatoria')
	otras_enfermedades = models.CharField(max_length=50, blank=True, choices=Otras, verbose_name='Otras Enfermedades', help_text='Indique si Padece')
	indique_otras = models.CharField(max_length=150, verbose_name='Indique', help_text='Especifique la enfermedad')
	


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
