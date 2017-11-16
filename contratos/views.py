from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from administracion.models import Servicios
from forms import ContratosForm
from django.views.generic.edit import FormView
from clientes.models import Potenciales
from clientes.views import ClienteContratosView
from factura.models import Facturas
from wkhtmltopdf.views import PDFTemplateView
from django.shortcuts import redirect
from django.http import HttpResponse

class ContratoClientesView(LoginRequiredMixin, FormView):
	template_name = 'clientes/contrato.html'
	form_class = ContratosForm
	fields =[
		'cedula', 'edad', 'fecha_n',
		'rif', 'telefono_o','estado',
		'municipio', 'parroquia', 'sector',
		'nombre_sector', 'ubicacion', 'nombre_ubicacion',
		'vivienda', 'nombre_vivienda', 'piso',
		'numero',
		'punto_referencia', 'servicio', 'cancer',
		'diabetes', 'enfermedad_corazon', 'presion_arterial',
		'enfermedad_renal', 'enfermendad_mental', 'enfermedades_importantes',
		'salud', 'peso', 'estatura', 'enfermedad_respiratoria',
		'enfermedad_digestivo',
		'enfermedad_circulatorio', 'otras_enfermedades',]

	def save(self, *args, **kwargs):
		Facturas.objects.create(
			something=kwargs['something'])
		#YetAnotherModel.objects.create(
			#something_else=kwargs['something_else']
		#)
		super(self).save(*args, **kwargs)

	def post(self, request, *args, **kwargs):
		form = ContratosForm(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			cliente = get_object_or_404(Potenciales, user=request.user.id)
			instance.cliente = cliente
			instance.save()
			#form.save()
			#return redirect('/accounts/contratos/')
                return render(request, ClienteContratosView.template_name)
		#return super(ContratoClientesView, self).post(form)