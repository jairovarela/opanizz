"""
This file was generated with the custommenu management command, it contains
the classes for the admin menu, you can customize this class as you want.

To activate your custom menu add the following to your settings.py::
    ADMIN_TOOLS_MENU = 'app.menu.CustomMenu'
"""

from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from admin_tools.menu import items, Menu


class CustomMenu(Menu):
    """
    Custom Menu for app admin site.
    """
    def __init__(self, **kwargs):
        Menu.__init__(self, **kwargs)
        self.children += [
            items.MenuItem(_('Inicio'), reverse('admin:index')),
            #            items.AppList(
            #                _('Applications'),
            #                exclude=('django.contrib.*',)
            #            ),
            items.MenuItem('Administracion', '/admin/administracion/',
                           children=[
                               items.MenuItem('Servicios', '/admin/administracion/servicios/'),
                           ]
                           ),
            items.MenuItem('Clientes', '/admin/clientes/',
                           children=[
                               items.MenuItem('Clientes Potenciales', '/admin/clientes/potenciales/'),
                               items.MenuItem('Actividades de Clientes', '/admin/clientes/actividad/'),
                           ]
                           ),
            items.MenuItem('Facturas', '/admin/factura/',
                           children=[
                               items.MenuItem('Crear Factura', '/admin/factura/facturas/add/'),
                           ]
                           ),
            items.MenuItem('Contratos', '/admin/contratos/',
                           children=[
                               items.MenuItem('Agregar Contrato a Cliente', '/admin/contratos/contratado/add/'),
                           ]
                           ),
            items.MenuItem('Generalidades', '/admin/generalidades/',
                           children=[
                               items.MenuItem('Estados', '/admin/generalidades/estado/',),
                               items.MenuItem('Municipios', '/admin/generalidades/municipio/',),
                               items.MenuItem('Parroquias', '/admin/generalidades/parroquia/',),
                               items.MenuItem('Sectores', '/admin/generalidades/sector/',
                                              children=[
                                                  items.MenuItem('Agregar Sector', '/admin/generalidades/sector/add/'),
                                                  items.MenuItem('Ubicaciones', '/admin/generalidades/ubicacion/'),
                                                  items.MenuItem('Viviendas', '/admin/generalidades/vivienda/',
                                                                 children=[
                                                                     items.MenuItem('Agregar Vivienda', '/admin/generalidades/vivienda/add/'),
                                                                 ]

                                                                 )
                                              ]
                                              ),
                               items.MenuItem('Zonas de Valencia', '/admin/generalidades/zonasvalencia/',),
                               items.MenuItem('Medios de Contacto', '/admin/generalidades/mediocontacto/'),
                               items.MenuItem('Medios de Contacto para Actividades', '/admin/generalidades/mediosactividad/'),
                               items.MenuItem('Usuarios Activos', '/admin/registration/',),
                           ]
                           ),
            items.AppList(
                _('Accesos y Permisos'),
                models=('django.contrib.*',)
            ),
        ]

    def init_with_context(self, context):
        """
        Use this method if you need to access the request context.
        """
        return super(CustomMenu, self).init_with_context(context)
