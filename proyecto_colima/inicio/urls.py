from django.conf.urls import patterns, include, url
from inicio.views import *


urlpatterns = patterns('proyecto_colima.inicio',
    # Examples:
    # url(r'^$', 'proyecto_colima.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', inicio, name="login"),
    url(r'^administrar_usuarios/$', administrar_usuarios, name="administrar-usuarios"),

    url(r'^registrar_proyecto/$', registrar_proyecto, name="registrar-proyecto"),
    url(r'^registrar_factura/$', registrar_factura, name="registrar-factura"),


    url(r'^anexostecnicos/$', anexostecnicos, name = "anexostecnicos"),
    url(r'^agregar_anexotecnico/$', agregar_anexotecnico, name = "agregar-anexotecnico"),
    url(r'^editar_anexotecnico/(?P<anexo_id>\d+)/$', editar_anexotecnico, name="editar-anexotecnico"),
    url(r'^eliminar_anexotecnico/(?P<anexo_id>\d+)/$', eliminar_anexotecnico, name="eliminar-anexotecnico"),
    url(r'^consultar_anexotecnico/(?P<anexo_id>\d+)/$', consultar_anexotecnico, name="consultar-anexotecnico"),

    url(r'^contratos/$', contratos, name="contratos"),
    url(r'^agregar_contrato/$', agregar_contrato, name = "agregar-contrato"),
    url(r'^editar_contrato/(?P<contrato_id>\d+)/$', editar_contrato, name="editar-contrato"),
    url(r'^eliminar_contrato/(?P<contrato_id>\d+)/$', eliminar_contrato, name="eliminar-contrato"),
    url(r'^consultar_contrato/(?P<contrato_id>\d+)/$', consultar_contrato, name="consultar-contrato"),

    url(r'^facturas/$', facturas, name="facturas"),
    url(r'^agregar_factura/$', agregar_factura, name = "agregar-factura"),
    url(r'^editar_factura/(?P<factura_id>\d+)/$', editar_factura, name="editar-factura"),
    url(r'^eliminar_factura/(?P<factura_id>\d+)/$', eliminar_factura, name="eliminar-factura"),
    url(r'^consultar_factura/(?P<factura_id>\d+)/$', consultar_factura, name="consultar-factura"),

    url(r'^convenios/$', convenios, name="convenios"),
    url(r'^agregar_convenios/$', agregar_convenios, name = "agregar-convenio"),
    url(r'^editar_convenio/(?P<convenio_id>\d+)/$', editar_convenio, name="editar-convenio"),
    url(r'^eliminar_convenio/(?P<convenio_id>\d+)/$', eliminar_convenio, name="eliminar-convenio"),
    url(r'^consultar_convenio/(?P<convenio_id>\d+)/$', consultar_convenio, name="consultar-convenio"),


   


    url(r'^registrar_contratos/$', registrar_contratos, name="registrar-contratos"),
    url(r'^registrar_convenios/$', registrar_convenios, name="registrar-convenios"),
    url(r'^registrar_propuestas/$', registrar_propuestas, name="registrar-propuestas"),
    url(r'^registrar_empresa/$', registrar_empresa, name="registrar-empresa"),
    url(r'^registrar_entregable/$', registrar_entregable, name="registrar-entregable"),
    url(r'^registrar_personal/$', registrar_personal, name="registrar-personal")
    )