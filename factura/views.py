from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView, UpdateView
from forms import FacturaForm
from clientes.models import Potenciales
from contratos.models import Contratado

# Create your views here.

class FacturasContrato(LoginRequiredMixin, generic.View):
    template_name = 'facturas.html'
    form_class = FacturaForm
    success_url = '/accounts/facturas/'

    def get(self, request, *args, **kwargs):
        user=request.user
        cliente_user= Potenciales.objects.filter(user_id=user)
        context = {
            'contratos': Contratado.objects.filter(cliente_id=cliente_user)
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = FacturaForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            form.save()
        return super(FacturasContrato, self).post(form)
