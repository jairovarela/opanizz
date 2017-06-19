from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from administracion.models import Servicios
from forms import ContratosForm


def datos(request):
    form = ContratosForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.usuario = request.user    
        instance.save()
    return render(request, "contratos/contrato.html", {"form":form})