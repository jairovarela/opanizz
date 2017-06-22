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
from clientes.views import ClienteServiciosView, DatosClientesView, DatosClientesUpdate
from clientes import views
from contratos.views import ContratoClientesView

urlpatterns = [
    url(r'^$', views.inicio, name = 'inicio'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^accounts/servicios/$', ClienteServiciosView.as_view(), name='clientes_servicios'),
    url(r'^accounts/profile/$', views.perfil, name='perfil'),
    url(r'^accounts/(?P<pk>\d+)/user/$', DatosClientesUpdate.as_view(), name='usuario'),
    url(r'^accounts/datos/$', DatosClientesView.as_view(), name='datos'),
    url(r'^accounts/contratos/$', ContratoClientesView.as_view(), name='contrato'),
    url(r'^accounts/contratados/$', views.contratados, name='contratados'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)