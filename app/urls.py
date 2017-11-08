"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from contratos.models import Contratado
from clientes.views import Dashboard, ClienteServiciosView, ContratoPDFView, ClienteContratosView, DatosClientesView, DatosClientesUpdate, IniciarSesion
from clientes import views
from factura.views import FacturasContrato
from contratos.views import ContratoClientesView
from django.views.generic import ListView, DetailView
from wkhtmltopdf.views import PDFTemplateView
from registration.backends.default import urls


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/dashboard/$', Dashboard.as_view(), name='dashboard'),
    url(r'^accounts/servicios/$', ClienteServiciosView.as_view(), name='clientes_servicios'),
    url(r'^accounts/profile/$', DatosClientesView.as_view(), name='datos'),
    url(r'^accounts/profile/update/$', DatosClientesUpdate.as_view(), name='perfil'),
    url(r'^accounts/contrato/$', ContratoClientesView.as_view(), name='contrato'),
    url(r'^accounts/contratos/$', ClienteContratosView.as_view(), name='contratos'),
    url(r'^accounts/contratos/pdf/$', ContratoPDFView.as_view(template_name='clientes/contrato_ambulancias.html',
                                             filename='Contrato OPA.pdf'), name='pdf'),
    #url(r'^accounts/contratos/pdf/(?P<pk>\d+)/$', ContratoPDFView.as_view(), name='pdf'),
    url(r'^accounts/facturas/$', FacturasContrato.as_view(), name='facturas'),
    url(r'^accounts/contacto/$', views.contacto, name='contacto'),
    url(r'^accounts/beneficiarios/$', views.beneficiarios, name='beneficiarios'),
    url (r'^accounts/contratos/(?P<pk>\d+)$', DetailView.as_view(model=Contratado,
    template_name='clientes/contrato_detalle'), name="contrato_detalle"),

    # ...

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
