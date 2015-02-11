from django.conf.urls import patterns, include, url
from inicio.views import *
from inicio.views_login import *
from inicio.views_modal import *

urlpatterns = patterns('proyecto_colima.inicio',

    #URL LOGOUT Y ADMINISTRACION
    url(r'^$', administracion, name="index"),
    url(r'^logout/$', logout_web, name="logout-web"),

    #MODALES
    url(r'^modal_ok/$', modal_ok, name="modal-ok"),
    url(r'^modal_aviso/$', modal_aviso, name="modal-aviso"),
    url(r'^modal_error/$', modal_error, name="modal-error"),
    
    #PERSONAL
    url(r'^personal/$', personal, name="personal"),
    url(r'^detalle_personal/(?P<pk>\d+)/$', PersonalDetailView.as_view(), name="detalle-personal"),
    url(r'^editar_personal/(?P<pk>\d+)/$', editar_personal, name="editar-personal"),
    url(r'^eliminar_personal/$', eliminar_personal, name='eliminar-personal'),
    url(r'^crear_personal/$', crear_personal, name="crear-personal"),

    #PROYECTOS
    url(r'^proyectos/$', proyectos, name="proyectos"),
    url(r'^detalle_proyecto/(?P<pk>\d+)/$', ProyectoDetailView.as_view(), name="detalle-proyecto"),
    url(r'^editar_proyecto/(?P<pk>\d+)/$', editar_proyecto, name="editar-proyecto"),
    url(r'^eliminar_proyecto/$', eliminar_proyecto, name='eliminar-proyecto'),
    url(r'^crear_proyecto/$', crear_proyecto, name="crear-proyecto"),

    #ENTREGABLES
    url(r'^entregables/$', entregables, name="entregables"),
    url(r'^detalle_entregable/(?P<pk>\d+)/$', EntregableDetailView.as_view(), name="detalle-proyecto"),
    url(r'^editar_entregable/(?P<pk>\d+)/$', editar_entregable, name="editar-entregable"),
    url(r'^eliminar_entregable/$', eliminar_entregable, name='eliminar-entregable'),
    url(r'^crear_entregable/$', crear_entregable, name="crear-entregable"),

    #FACTURAS
    url(r'^facturas/$', facturas, name="facturas"),
    url(r'^detalle_factura/(?P<pk>\d+)/$', FacturaDetailView.as_view(), name="detalle-factura"),
    url(r'^editar_factura/(?P<pk>\d+)/$', editar_factura, name="editar-factura"),
    url(r'^crear_factura/$', crear_factura, name="crear-factura"),

    #ANEXOS TECNICOS
    url(r'^anexostecnicos/$', anexostecnicos, name = "anexostecnicos"),
    url(r'^detalle_anexotecnico/(?P<pk>\d+)/$', AnexotecnicoDetailView.as_view(), name="detalle-anexotecnico"),
    url(r'^editar_anexotecnico/(?P<pk>\d+)/$', editar_anexotecnico, name="editar-anexotecnico"),
    url(r'^eliminar_anexotecnico/$', eliminar_anexotecnico, name='eliminar-anexotecnico'),
    url(r'^crear_anexotecnico/$', crear_anexotecnico, name="crear-anexotecnico"),

    #CONTRATOS
    url(r'^contratos/$', contratos, name="contratos"),
    url(r'^detalle_contrato/(?P<pk>\d+)/$', ContratoDetailView.as_view(), name="detalle-contrato"),
    url(r'^editar_contrato/(?P<pk>\d+)/$', editar_contrato, name="editar-contrato"),
    url(r'^eliminar_contrato/$', eliminar_contrato, name='eliminar-contrato'),
    url(r'^crear_contrato/$', crear_contrato, name="crear-contrato"),

    #CONVENIOS
    url(r'^convenios/$', convenios, name="convenios"),
    url(r'^detalle_convenio/(?P<pk>\d+)/$', ConvenioDetailView.as_view(), name="detalle-convenio"),
    url(r'^editar_convenio/(?P<pk>\d+)/$', editar_convenio, name="editar-convenio"),
    url(r'^eliminar_convenio/$', eliminar_convenio, name='eliminar-convenio'),
    url(r'^crear_convenio/$', crear_convenio, name="crear-convenio"),

    #PROPUESTAS
    url(r'^propuestas/$', propuestas, name = "propuestas"),
    url(r'^detalle_propuesta/(?P<pk>\d+)/$', PropuestaDetailView.as_view(), name="detalle-propuesta"),
    url(r'^editar_propuesta/(?P<pk>\d+)/$', editar_propuesta, name="editar-propuesta"),
    url(r'^eliminar_propuesta/$', eliminar_propuesta, name='eliminar-propuesta'),
    url(r'^crear_propuesta/$', crear_propuesta, name="crear-propuesta"),

    url(r'^clientes/$', clientes, name="clientes"),
    url(r'^detalle_cliente/(?P<pk>\d+)/$', ClienteDetailView.as_view(), name="detalle-cliente"),
    url(r'^editar_cliente/(?P<pk>\d+)/$', editar_cliente, name="editar-cliente"),
    url(r'^eliminar_cliente/$', eliminar_cliente, name='eliminar-cliente'),
    url(r'^crear_cliente/$', crear_cliente, name="crear-cliente"),

    #ENTIDADES
    url(r'^entidades/$', entidades, name="entidades"),
    url(r'^detalle_entidad/(?P<pk>\d+)/$', EntidadDetailView.as_view(), name="detalle-entidad"),
    url(r'^editar_entidad/(?P<pk>\d+)/$', editar_entidad, name="editar-entidad"),
    url(r'^eliminar_entidad/$', eliminar_entidad, name='eliminar-entidad'),
    url(r'^crear_entidad/$', crear_entidad, name="crear-entidad"),
    )