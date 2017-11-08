from __future__ import unicode_literals
from django.db import models
from clientes.models import Potenciales
from generalidades.models import Estado, Municipio, Parroquia, Sector, Vivienda, Ubicacion
from administracion.models import Servicios

def incremental():
    ultimo_contratado= Contratado.objects.all().order_by('id').last()
    if not ultimo_contratado:
        return 'OPA-' + '1'
    else:
        numcontrato = Contratado.objects.all().count()
        numcontrato = numcontrato + 0001
        return 'OPA-' + str(numcontrato)


Respiratorio = (
    ('Bronquitis', 'Bronquitis Cronica'),
    ('Tuberculosis', 'Tuberculosis'),
    ('Asma', 'Asma'),
    ('Ninguna', 'Ninguna')
)

Circulatorio = (
    ('Trastorno en la presion arterial','Trastorno en la presion arterial '),
    ('Alteraciones cardiacas','Alteraciones cardiacas'),
    ('Angina de pecho','Angina de pecho '),
    ('Infarto de miocardio','Infarto de miocardio'),
    ('Ninguna', 'Ninguna')
)

Digestivo = (
    ('Enfermedades del higado','Enfermedades del higado'),
    ('Ulcera gastroduodenal','Ulcera gastroduodenal'),
    ('Dispepcia','Dispepcia'),
    ('Gastritis','Gastritis'),
    ('Ninguna', 'Ninguna')
)

Opciones = (
    ('No','No'),
    ('Si','Si'),
)

Otras = (
    ('Reumatismo','Reumatismo'),
    ('Artritis','Artritis'),
    ('Hemorragias de cualquier indole','Hemorragias de cualquier indole'),
    ('Perdida del conocimiento','Perdida del conocimiento'),
    ('Enfermedades en los huesos','Enfermedades en los huesos'),
    ('Convulsiones','Convulsiones'),
    ('Paralisis','Paralisis'),
    ('Ninguna', 'Ninguna')
)

Salud = (
    ('Buena', 'Buena'),
    ('Regular', 'Regular'),
    ('Mala', 'Mala'),
)

ModoCuotas = (
    ('Contado', '1' ),
    ('Bianual', '2' ),
    ('Trimestral', '4'),
    ('Mensual', '12' )
)

ModoPago = (
    ('Tarjeta de Credito', 'Tarjeta de Credito'),
    ('Transferencia', 'Transferencia')
)

class Contratado(models.Model):
    numcontrato = models.CharField(max_length=20, default=incremental, editable=False)
    estatus= models.BooleanField(verbose_name='Estatus')
    cliente = models.ForeignKey(Potenciales)
    cedula = models.IntegerField(unique=True)
    edad = models.IntegerField(null = True)
    fecha_n = models.DateField(null = True, verbose_name = 'Fecha de Nacimiento')
    rif = models.CharField(max_length = 20, verbose_name = 'R.I.F.', blank = True, help_text = 'Opcional si posee' )
    telefono_o = models.IntegerField(null = True, verbose_name = 'Telefono Oficina', blank=True)
    estado = models.ForeignKey(Estado, verbose_name='Estado')
    municipio = models.ForeignKey(Municipio, verbose_name='Municipio')
    parroquia = models.ForeignKey(Parroquia, verbose_name='Parroquia')
    sector = models.ForeignKey(Sector, null=True, verbose_name='Sector')
    nombre_sector = models.CharField(max_length=150, null=True, blank=True, verbose_name='Nombre del Sector')
    ubicacion = models.ForeignKey(Ubicacion, verbose_name='Ubicacion', null=True, blank=True)
    nombre_ubicacion = models.CharField(max_length=100, verbose_name='Nombre de la Ubicacion', blank=True, null=True)
    vivienda = models.ForeignKey(Vivienda, verbose_name='Vivienda', null=True, blank=True)
    nombre_vivienda = models.CharField(max_length=100, blank=True, verbose_name='Nombre de la Vivienda')
    piso = models.CharField(max_length=15, blank=True)
    numero = models.CharField(max_length=15, null=True, blank=True)
    punto_referencia = models.CharField(max_length=250, verbose_name='Punto de Referencia de busqueda')
    servicio = models.ForeignKey(Servicios, null=True, verbose_name='Servicio a Contratar')
    cancer = models.CharField(max_length=2, choices=Opciones, blank=True, verbose_name='Cancer')
    diabetes = models.CharField(max_length=2, choices=Opciones, blank=True, verbose_name='Diabetes')
    enfermedad_corazon = models.CharField(max_length=2, choices=Opciones, blank=True, verbose_name='Enfermedades del Corazon')
    presion_arterial = models.CharField(max_length=2, choices=Opciones, blank=True, verbose_name='Presion Arterial Alta')
    enfermedad_renal = models.CharField(max_length=2, choices=Opciones, blank=True, verbose_name='Enfermedades Renales')
    enfermendad_mental = models.CharField(max_length=2, choices=Opciones, blank=True, verbose_name='Enfermedades Mentales')
    enfermedades_importantes = models.CharField(max_length=250, blank=True, null=True, verbose_name='Otras Importantes')
    salud = models.CharField(max_length=7, choices=Salud, verbose_name='Estado de Salud', blank=True)
    peso = models.CharField(max_length=7, blank=True, verbose_name='Indique su peso')
    estatura = models.CharField(max_length=7, blank=True, verbose_name='Indique su Estatura')
    enfermedad_respiratoria = models.CharField(max_length=50, blank=True, choices=Respiratorio, verbose_name='Enfermedades Respiratorias', help_text='Indique si Padece')
    enfermedad_digestivo = models.CharField(max_length=50, blank=True, choices=Digestivo, verbose_name='Enfermedades Digestivas', help_text='Indique si Padece')
    enfermedad_circulatorio = models.CharField(max_length=50, blank=True, choices=Circulatorio, verbose_name='Enfermedades Circulatorias', help_text='Indique si Padece')
    otras_enfermedades = models.CharField(max_length=50, blank=True, choices=Otras, verbose_name='Otras Enfermedades', help_text='Indique si Padece')
    modalidad_cuotas = models.CharField(max_length=10, null=True, choices=ModoCuotas, verbose_name='Escoja la cantidad de cuotas en las que realizara sus pagos')
    fecha_contratacion = models.DateTimeField(auto_now_add=True)
    fecha_expiracion = models.DateTimeField(auto_now_add=True)
    precio_total = models.IntegerField(null=True, blank=True, verbose_name="Precio Total del Contrato")

    class Meta:
        verbose_name = 'Cliente a Contratar'
        verbose_name_plural = 'Contratos Generados'

    def __unicode__(self):
        return '%s - %s' % (self.numcontrato, self.cliente,)

class Beneficiario(models.Model):
    contratado = models.ForeignKey(Contratado, null = True)
    nombre = models.CharField(max_length = 255)
    apellido = models.CharField(max_length = 255)
    cedula = models.IntegerField(blank = True, null = True)
    email = models.EmailField(null=True, blank=True)
    edad = models.IntegerField(null=True, blank=True)
    fecha_n = models.DateField(verbose_name = 'Fecha de Nacimiento')
    telefono = models.IntegerField(blank = True, null = True)
    beneficiario_cancer = models.CharField(max_length=2, choices=Opciones, blank=True, verbose_name='Cancer')
    beneficiario_diabetes = models.CharField(max_length=2, choices=Opciones, blank=True, verbose_name='Diabetes')
    beneficiario_enfermedad_corazon = models.CharField(max_length=2, choices=Opciones, blank=True, verbose_name='Enfermedades del Corazon')
    beneficiario_presion_arterial = models.CharField(max_length=2, choices=Opciones, blank=True, verbose_name='Presion Arterial Alta')
    beneficiario_enfermedad_renal = models.CharField(max_length=2, choices=Opciones, blank=True, verbose_name='Enfermedades Renales')
    beneficiario_enfermendad_mental = models.CharField(max_length=2, choices=Opciones, blank=True, verbose_name='Enfermedades Mentales')
    beneficiario_enfermedades_importantes = models.CharField(max_length=250, blank=True, verbose_name='Otras Importantes')
    beneficiario_salud = models.CharField(max_length=7, choices=Salud, verbose_name='Estado de Salud', blank=True)
    beneficiario_peso = models.CharField(max_length=7, blank=True, verbose_name='Indique su peso')
    beneficiario_estatura = models.CharField(max_length=7, blank=True, verbose_name='Indique su Estatura')
    beneficiario_enfermedad_respiratoria = models.CharField(max_length=50, blank=True, choices=Respiratorio, verbose_name='Enfermedades Respiratorias', help_text='Indique si Padece')
    beneficiario_indique_respiratoria = models.CharField(max_length=150, blank=True, verbose_name='Indique', help_text='Especifique enfermedad Respirarotia')
    beneficiario_enfermedad_digestivo = models.CharField(max_length=50, blank=True, choices=Digestivo, verbose_name='Enfermedades Digestivas', help_text='Indique si Padece')
    beneficiario_indique_digestivo = models.CharField(max_length=150, blank=True, verbose_name='Indique', help_text='Especifique Enfermedad Digestiva')
    beneficiario_enfermedad_circulatorio = models.CharField(max_length=50, blank=True, choices=Circulatorio, verbose_name='Enfermedades Circulatorias', help_text='Indique si Padece')
    beneficiario_indique_circulatorio = models.CharField(max_length=150, blank=True, verbose_name='Indique', help_text='Especifique Enfermedad Circulatoria')
    beneficiario_otras_enfermedades = models.CharField(max_length=50, blank=True, choices=Otras, verbose_name='Otras Enfermedades', help_text='Indique si Padece')
    beneficiario_indique_otras = models.CharField(max_length=150, blank=True, verbose_name='Indique', help_text='Especifique la enfermedad')


    class Meta:
        verbose_name = 'Beneficiario'
        verbose_name_plural = 'Beneficiarios'

    def __unicode__(self):
        return '%s %s' % (self.nombre, self.apellido)
