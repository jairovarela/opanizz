from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from administracion.models import Servicios
from forms import PotencialesForm, PotencialesUpdateForm
from contratos.forms import ContratosForm
from django.views.generic.edit import FormView, UpdateView
from django.views.generic import TemplateView
from models import Potenciales
from django.shortcuts import redirect




def inicio(request):
    return render(request, "inicio.html", {})

def usuario(request):
    return render(request, "clientes/user.html", {})

def handler404(request):
    response = render_to_response('404.html', {},context_instance=RequestContext(request))
    response.status_code = 404
    return response

def contrato(request):
    form = ContratosForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    return render(request, "clientes/contrato.html", {"form":form})

def contratados(request):
    return render(request, "clientes/contrato_hecho.html", {})

def is_profile_updated(user):
    if hasattr(user, 'potenciales'):
        return all((getattr(user.potenciales, field.name) for field in user.potenciales._meta.fields))
    return False




class IniciarSesion(LoginRequiredMixin, generic.View):
    template_name = 'clientes/perfil.html'
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
    	import ipdb; ipdb.set_trace()
    	data = request.POST
        context = {
            'servicios': Servicios.objects.all()
        }
        return render(request, self.template_name, context)
 

class DatosClientesView(LoginRequiredMixin, FormView):
    template_name = 'clientes/datos.html'
    form_class = PotencialesForm
    success_url = '/accounts/profile/'
    fields =[
            'nombre',
            'apellido',
            'medio_contactado',
            'celular',
            'telefono_h',
            'personas',
            'cantidad_p',
            'adultos',
            'valencia',
            'zona',
            'estado',
            'municipio',
            'parroquia',
        ]
        
    def post(self, request, *args, **kwargs):
        form = PotencialesForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.usuario = request.user
            instance.save()
            form.save()

        return super(DatosClientesView, self).post(form)


class DatosClientesUpdate(UpdateView):
    template_name = 'clientes/user.html'
    model = Potenciales
    form_class = PotencialesUpdateForm
    success_url = '/accounts/profile/'

        
    def post(self, request, *args, **kwargs):
        form = PotencialesForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.usuario = request.user
            instance.save()
            form.save()

        return super(DatosClientesUpdate, self).post(form)




