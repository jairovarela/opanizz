from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from administracion.models import Servicios
from forms import PotencialesForm


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












def handler404(request):
    response = render_to_response('404.html', {},context_instance=RequestContext(request))
    response.status_code = 404
    return response

def inicio(request):
	return render(request, "inicio.html", {})


def perfil(request):
	return render(request, "clientes/perfil.html", {})

def datos(request):
    form = PotencialesForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    return render(request, "clientes/datos.html", {"form":form})
