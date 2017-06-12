from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext


def handler404(request):
    response = render_to_response('404.html', {},context_instance=RequestContext(request))
    response.status_code = 404
    return response

def inicio(request):
	return render(request, "inicio.html", {})

def perfil(request):
	return render(request, "perfil.html",{})

def datos(request):
	return render(request, "datos.html",{})
