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
    
    #PROYECTOS
    url(r'^proyectos/$', proyectos, name="proyectos"),
    url(r'^detalle_proyecto/(?P<pk>\d+)/$', ProyectoDetailView.as_view(), name="detalle-proyecto"),
    url(r'^editar_proyecto/(?P<pk>\d+)/$', editar_proyecto, name="editar-proyecto"),
    url(r'^eliminar_proyecto/$', eliminar_proyecto, name='eliminar-proyecto'),
    url(r'^crear_proyecto/$', crear_proyecto, name="crear-proyecto"),

    #FACTURAS
    url(r'^facturas/$', facturas, name="facturas"),
    url(r'^detalle_factura/(?P<pk>\d+)/$', FacturaDetailView.as_view(), name="detalle-factura"),
    url(r'^editar_factura/(?P<pk>\d+)/$', editar_factura, name="editar-factura"),
    url(r'^crear_factura/$', crear_factura, name="crear-factura"),



    # url(r'^registrar_factura/$', registrar_factura, name="registrar-factura"),
     url(r'^anexostecnicos/$', anexostecnicos, name = "anexostecnicos"),
    # url(r'^agregar_anexotecnico/$', agregar_anexotecnico, name = "agregar-anexotecnico"),
    # url(r'^editar_anexotecnico/(?P<anexo_id>\d+)/$', editar_anexotecnico, name="editar-anexotecnico"),
    # url(r'^eliminar_anexotecnico/(?P<anexo_id>\d+)/$', eliminar_anexotecnico, name="eliminar-anexotecnico"),
    # url(r'^consultar_anexotecnico/(?P<anexo_id>\d+)/$', consultar_anexotecnico, name="consultar-anexotecnico"),

     url(r'^contratos/$', contratos, name="contratos"),
    # url(r'^agregar_contrato/$', agregar_contrato, name = "agregar-contrato"),
    # url(r'^editar_contrato/(?P<contrato_id>\d+)/$', editar_contrato, name="editar-contrato"),
    # url(r'^eliminar_contrato/(?P<contrato_id>\d+)/$', eliminar_contrato, name="eliminar-contrato"),
    # url(r'^consultar_contrato/(?P<contrato_id>\d+)/$', consultar_contrato, name="consultar-contrato"),

    # url(r'^facturas/$', facturas, name="facturas"),
    # url(r'^agregar_factura/$', agregar_factura, name = "agregar-factura"),
    # url(r'^editar_factura/(?P<factura_id>\d+)/$', editar_factura, name="editar-factura"),
    # url(r'^eliminar_factura/(?P<factura_id>\d+)/$', eliminar_factura, name="eliminar-factura"),
    # url(r'^consultar_factura/(?P<factura_id>\d+)/$', consultar_factura, name="consultar-factura"),

     url(r'^convenios/$', convenios, name="convenios"),
    # url(r'^agregar_convenio/$', agregar_convenio, name = "agregar-convenio"),
    # url(r'^editar_convenio/(?P<convenio_id>\d+)/$', editar_convenio, name="editar-convenio"),
    # url(r'^eliminar_convenio/(?P<convenio_id>\d+)/$', eliminar_convenio, name="eliminar-convenio"),
    # url(r'^consultar_convenio/(?P<convenio_id>\d+)/$', consultar_convenio, name="consultar-convenio"),

     url(r'^empresas/$', empresas, name = "empresas"),
    # url(r'^agregar_empresa/$', agregar_empresa, name = "agregar-empresa"),
    # url(r'^editar_empresa/(?P<empresa_id>\d+)/$', editar_empresa, name="editar-empresa"),
    # url(r'^eliminar_empresa/(?P<empresa_id>\d+)/$', eliminar_empresa, name="eliminar-empresa"),
    # url(r'^consultar_empresa/(?P<empresa_id>\d+)/$', consultar_empresa, name="consultar-empresa"),

     url(r'^propuestas/$', propuestas, name = "propuestas"),
    # url(r'^agregar_propuesta/$', agregar_propuesta, name = "agregar-propuesta"),
    # url(r'^editar_propuesta/(?P<propuesta_id>\d+)/$', editar_propuesta, name="editar-propuesta"),
    # url(r'^eliminar_propuesta/(?P<propuesta_id>\d+)/$', eliminar_propuesta, name="eliminar-propuesta"),
    # url(r'^consultar_propuesta/(?P<propuesta_id>\d+)/$', consultar_propuesta, name="consultar-propuesta"),



    url(r'^registrar_contratos/$', registrar_contratos, name="registrar-contratos"),
    url(r'^registrar_convenios/$', registrar_convenios, name="registrar-convenios"),
    url(r'^registrar_propuestas/$', registrar_propuestas, name="registrar-propuestas"),
    url(r'^registrar_empresa/$', registrar_empresa, name="registrar-empresa"),
    url(r'^registrar_entregable/$', registrar_entregable, name="registrar-entregable"),
    url(r'^registrar_personal/$', registrar_personal, name="registrar-personal")
    )