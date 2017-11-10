from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext
from administracion.models import Servicios
from contratos.models import Contratado, Beneficiario
from forms import PotencialesForm, PotencialesUpdateForm
from contratos.forms import ContratosForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView, UpdateView, CreateView
from django.views.generic import TemplateView
from models import Potenciales
from django.shortcuts import redirect
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from wkhtmltopdf.views import PDFTemplateView

def index(request):
    return render(request, "inicio.html", {})

def handler404(request):
    response = render_to_response('404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response

def is_profile_updated(user):
    if hasattr(user, 'potenciales'):
        return all((getattr(user.potenciales, field.name) for field in user.potenciales._meta.fields))
    return False

def cliente_user_contrato(user):
    cliente_user = Potenciales.objects.filter(user_id=user)
    return cliente_user

def beneficiarios(request):
    return render(request, "clientes/beneficiarios.html", {})

def contacto(request):
    return render(request, "clientes/contacto.html", {})


class ClienteContratosView(LoginRequiredMixin, ListView):

    template_name = 'clientes/contratos.html'
    paginate_by = 5

    def get_queryset(self):
        queryset = Contratado.objects.all().order_by("numcontrato")
        return queryset

    def get(self, request, *args, **kwargs):
        user=request.user
        cliente_user= Potenciales.objects.filter(user_id=user)
        context = {
            'contratos': Contratado.objects.filter(cliente_id=cliente_user)
        }
        return render(request, self.template_name, context)

class ContratoPDFView(LoginRequiredMixin, PDFTemplateView):

    #contrato = get_object_or_404(Contratado, id=pk)
    #contrato_cliente = Potenciales.objects.filter(contratado=contrato)
    def get_context_data(self, **kwargs):
        context = super(ContratoPDFView, self).get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        cliente_user = cliente_user_contrato(request.user)
        cliente_contratado = Contratado.objects.filter(cliente_id=cliente_user).order_by("id")[:1].get()
        context = {
            'numcontrato': cliente_contratado.numcontrato,
            'nombre': cliente_contratado.cliente,
            'cedula': cliente_contratado.cedula,
            'estado': cliente_contratado.estado,
            'municipio': cliente_contratado.municipio,
            'parroquia': cliente_contratado.parroquia,
            'sector': cliente_contratado.sector,
            'nombre_sector': cliente_contratado.nombre_sector,
            'ubicacion': cliente_contratado.ubicacion,
            'nombre_ubicacion': cliente_contratado.nombre_ubicacion,
            'vivienda': cliente_contratado.vivienda,
            'nombre_vivienda': cliente_contratado.nombre_vivienda,
            'piso': cliente_contratado.piso,
            'numero': cliente_contratado.numero,
            'fecha_contratacion': cliente_contratado.fecha_contratacion,
            'fecha_expiracion': cliente_contratado.fecha_expiracion
        }
        return render(request, self.template_name, context)


class Dashboard(LoginRequiredMixin, generic.View):

    template_name = 'clientes/dashboard.html'

    def get(self, request, *args, **kwargs):
        user=request.user
        cliente_user= Potenciales.objects.filter(user_id=user)
        context = {
            'contratos': Contratado.objects.filter(cliente_id=cliente_user),
            'ncontratos': Contratado.objects.filter(cliente_id=cliente_user).count()
        }
        return render(request, self.template_name, context)

class IniciarSesion(LoginRequiredMixin, generic.View):
    template_name = 'clientes/datos.html'
    def get(self, request, *args, **kwargs):
        if not is_profile_updated(request.user):
            return redirect('/accounts/datos/')
        return render(request, self.template_name)

class ClienteServiciosView(LoginRequiredMixin, generic.View):
    template_name = 'clientes/servicios.html'
    def get(self, request, *args, **kwargs):
        context = {
            'servicios': Servicios.objects.all()
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        data = request.POST
        context = {
            'servicios': Servicios.objects.all()
        }
        return render(request, self.template_name, context)

class DatosClientesView(LoginRequiredMixin, FormView):
    template_name = 'clientes/user.html'
    model = Potenciales
    form_class = PotencialesForm
    success_url = '/accounts/profile/'
    fields =[
        'nombre',
        'apellido',
        'celular',
        'telefono_h',
        'personas',
        'cantidad_p',
        'adultos',
        'valencia',
        'estado',
        'municipio',
        'parroquia',
    ]

    def post(self, request, *args, **kwargs):
        form = PotencialesForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            form.save()
        return super(DatosClientesView, self).post(form)

class DatosClientesUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'clientes/user.html'
    model = Potenciales
    form_class = PotencialesUpdateForm
    success_url = '/accounts/profile/update/'

    def get_object(self, queryset=None):
        return Potenciales.objects.get(user=self.request.user)

    def post(self, request, *args, **kwargs):
        form = PotencialesForm(request.POST or None)
        if form.is_valid():
            instance = form.save
            instance.user = request.user
            instance.save()
            form.save()
        return super(DatosClientesUpdate, self).post(form)



