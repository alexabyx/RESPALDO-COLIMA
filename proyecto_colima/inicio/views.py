#! -*- coding:utf-8 -*-
# Create your views here.

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage
from django.shortcuts import render, render_to_response, get_object_or_404
from django.conf import settings
from django.http import HttpResponseRedirect, Http404
from django.template import RequestContext
from django.forms.models import model_to_dict

from inicio.forms import (	AuthForm, 
							RegistrarProyectoForm, 
							FacturasForm, 
							AnexosTecnicosForm, 
							ContratosForm, 
							ConveniosForm, 
							PropuestasForm, 
							EmpresasForm, 
							EntregablesForm, 
							PersonalForm,
							ConsultarAnexoTecnicoForm,
							ConsultarContratoForm,
							ConsultarFacturasForm,
							ConsultarConveniosForm,
							ConsultarEmpresasForm,
							ConsultarPropuestasForm
						  )

from inicio.models import ( AnexosTecnicos,
							Contratos,
							Facturas,
							Convenios,
							Propuestas,
							Empresas
						  )

def registrar_proyecto(request):
	if request.method=="POST":
		form = RegistrarProyectoForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			mensaje="Registro Guardado"
			return render(request, 'inicio/registrar_proyecto.html', {'mensaje': mensaje}, context_instance=RequestContext(request))
		else:
			print "No paso"
	else:
		form=RegistrarProyectoForm()	
	return render(request, 'inicio/registrar_proyecto.html', {'form': form}, context_instance=RequestContext(request))

def registrar_factura(request):
	form = FacturasForm()
	return render(request, 'inicio/registrar_factura.html', {'form': form}, context_instance=RequestContext(request))

#VIEWS PARA ANEXOS TECNICOS
def anexostecnicos(request):
	anexostecnicos_list = AnexosTecnicos.objects.all().order_by('-fecha_creacion')

	paginator = Paginator(anexostecnicos_list, 10)
	page = request.GET.get('page', 1)

	try:
		anexostecnicos = paginator.page(page)
	except PageNotAnInteger:
		anexostecnicos = paginator.page(1)
	except EmptyPage:
		anexostecnicos = paginator.page(paginator.num_pages)

	return render(request, 'inicio/anexostecnicos.html', {'anexostecnicos':anexostecnicos}, context_instance=RequestContext(request))

def consultar_anexotecnico(request, anexo_id):
	anexo= AnexosTecnicos.objects.get(id=anexo_id)
	form = ConsultarAnexoTecnicoForm(model_to_dict(anexo))
	return render(request, 'inicio/consultar_anexotecnico.html', {'form':form}, context_instance=RequestContext(request))

def agregar_anexotecnico(request):
	if request.method == "POST":
		form = AnexosTecnicosForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			mensaje = "Guardado"
			return render(request, 'inicio/agregar_anexotecnico.html', {'mensaje': mensaje}, context_instance=RequestContext(request))
	else:
		form = AnexosTecnicosForm()
	return render(request, 'inicio/agregar_anexotecnico.html', {'form':form}, context_instance=RequestContext(request))

def editar_anexotecnico(request, anexo_id):
	if request.method == "POST":
		form = AnexosTecnicosForm(request.POST)
		if form.is_valid():
			anexo = AnexosTecnicos.objects.get(id=anexo_id)
			anexo.numero_oficio = form.cleaned_data['numero_oficio']
			anexo.proyecto = form.cleaned_data['proyecto']
			anexo.tipo = form.cleaned_data['tipo']
			anexo.nombre = form.cleaned_data['nombre']
			anexo.siglas = form.cleaned_data['siglas']
			anexo.porcentaje = form.cleaned_data['porcentaje']
			anexo.fecha_creacion = form.cleaned_data['fecha_creacion']
			anexo.archivo = form.cleaned_data['archivo']
			anexo.save()
			mensaje = "Guardado"
			return render(request, 'inicio/editar_anexotecnico.html', {'mensaje': mensaje}, context_instance=RequestContext(request))
	else:					
		try:
			anexo = AnexosTecnicos.objects.get(id=anexo_id)
		except:
			anexo = None

		form = AnexosTecnicosForm(instance=anexo)	

	return render(request, 'inicio/editar_anexotecnico.html', {'form': form}, context_instance=RequestContext(request))

def eliminar_anexotecnico(request, anexo_id):
	try:
		anexo = AnexosTecnicos.objects.get(id=anexo_id)
		try:
			anexo.delete()
			mensaje = "Eliminado"
		except:
			mensaje = "Falló al eliminar"
	except:
		anexo = None
		mensaje = "Error inesperado"

	return render(request, 'inicio/eliminar_anexotecnico.html',{'mensaje': mensaje}, context_instance=RequestContext(request))

def contratos(request):
	contratos = Contratos.objects.all()

	paginator = Paginator(contratos, 10)
	page = request.GET.get('page', 1)

	try:
		contratos = paginator.page(page)
	except PageNotAnInteger:
		contratos = paginator.page(1)
	except EmptyPage:
		contratos = paginator.page(paginator.num_pages)

	return render(request, 'inicio/contratos.html', {'contratos':contratos}, context_instance=RequestContext(request))

def agregar_contrato(request):
	if request.method == "POST":
		form = ContratosForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			mensaje = "Guardado"
			return render(request, 'inicio/agregar_contrato.html', {'mensaje': mensaje}, context_instance=RequestContext(request))
	else:
		form = ContratosForm()
	return render(request, 'inicio/agregar_contrato.html', {'form':form}, context_instance=RequestContext(request))


def consultar_contrato(request, contrato_id):
	contrato= Contratos.objects.get(id=contrato_id)
	form = ConsultarContratoForm(model_to_dict(contrato))
	return render(request, 'inicio/consultar_contrato.html', {'form':form}, context_instance=RequestContext(request))


def editar_contrato(request, contrato_id):
	if request.method == "POST":
		form = ContratosForm(request.POST)
		if form.is_valid():
			contrato = Contratos.objects.get(id=contrato_id)
			contrato.numero_oficio = form.cleaned_data['numero_oficio']
			contrato.proyecto = form.cleaned_data['proyecto']
			contrato.encargado=form.cleaned_data['encargado']
			contrato.cliente=form.cleaned_data['cliente']		
			contrato.fecha_creacion = form.cleaned_data['fecha_creacion']
			contrato.archivo = form.cleaned_data['archivo']
			contrato.save()
			mensaje = "Guardado"
			return render(request, 'inicio/editar_contratos.html', {'mensaje': mensaje}, context_instance=RequestContext(request))
	else:					
		try:
			contrato = Contratos.objects.get(id=contrato_id)
		except:
			contrato = None

		form = ContratosForm(instance=contrato)	

	return render(request, 'inicio/editar_contrato.html', {'form': form}, context_instance=RequestContext(request))

def eliminar_contrato(request, contrato_id):
	try:
		contrato = Contratos.objects.get(id=contrato_id)
		try:
			contrato.delete()
			mensaje = "Eliminado"
		except:
			mensaje = "Falló al eliminar"
	except:
		contrato = None
		mensaje = "Error inesperado"

	return render(request, 'inicio/eliminar_contrato.html',{'mensaje': mensaje}, context_instance=RequestContext(request))

def facturas(request):
	facturas = Facturas.objects.all()

	paginator = Paginator(facturas, 10)
	page = request.GET.get('page', 1)

	try:
		facturas = paginator.page(page)
	except PageNotAnInteger:
		facturas = paginator.page(1)
	except EmptyPage:
		facturas = paginator.page(paginator.num_pages)

	return render(request, 'inicio/facturas.html', {'facturas':facturas}, context_instance=RequestContext(request))



def agregar_factura(request):
	if request.method == "POST":
		form = FacturasForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			mensaje = "Guardado"
			return render(request, 'inicio/agregar_factura.html', {'mensaje': mensaje}, context_instance=RequestContext(request))
	else:
		form = FacturasForm()
	return render(request, 'inicio/agregar_factura.html', {'form':form}, context_instance=RequestContext(request))

def consultar_factura(request, factura_id):
	factura= Facturas.objects.get(id=factura_id)
	form = ConsultarFacturasForm(model_to_dict(factura))
	return render(request, 'inicio/consultar_factura.html', {'form':form}, context_instance=RequestContext(request))

def editar_factura(request, factura_id):
	if request.method == "POST":
		form = FacturasForm(request.POST)
		if form.is_valid():
			factura = Facturas.objects.get(id=factura_id)
			factura.contrato = form.cleaned_data['contrato']
			factura.responsable = form.cleaned_data['responsable']
			factura.tipo=form.cleaned_data['tipo']
			factura.nombre=form.cleaned_data['nombre']		
			factura.siglas=form.cleaned_data['siglas']		
			factura.numero_factura=form.cleaned_data['numero_factura']		
			factura.fecha_factura = form.cleaned_data['fecha_factura']
			factura.folio_venta = form.cleaned_data['folio_venta']
			factura.rfc = form.cleaned_data['folio_venta']
			factura.direccion = form.cleaned_data['direccion']
			factura.subtotal = form.cleaned_data['subtotal']
			factura.iva = form.cleaned_data['iva']
			factura.total_con_numero = form.cleaned_data['total_con_numero']
			factura.total_con_letra = form.cleaned_data['total_con_letra']
			factura.pagada = form.cleaned_data['pagada']
			factura.archivo = form.cleaned_data['archivo']
			factura.save()
			mensaje = "Guardado"
			return render(request, 'inicio/editar_facturas.html', {'mensaje': mensaje}, context_instance=RequestContext(request))
	else:					
		try:
			factura = Facturas.objects.get(id=factura_id)
		except:
			factura = None

		form = FacturasForm(instance=factura)	

	return render(request, 'inicio/editar_anexotecnico.html', {'form': form}, context_instance=RequestContext(request))	

def eliminar_factura(request, factura_id):
	try:
		factura = Facturas.objects.get(id=factura_id)
		try:
			factura.delete()
			mensaje = "Eliminado"
		except:
			mensaje = "Falló al eliminar"
	except:
		factura = None
		mensaje = "Error inesperado"

	return render(request, 'inicio/eliminar_factura.html',{'mensaje': mensaje}, context_instance=RequestContext(request))

#apartir de aqui copio convenios
def convenios(request):
	convenios = Convenios.objects.all()

	paginator = Paginator(convenios, 10)
	page = request.GET.get('page', 1)

	try:
		convenios = paginator.page(page)
	except PageNotAnInteger:
		convenios = paginator.page(1)
	except EmptyPage:
		convenios = paginator.page(paginator.num_pages)

	return render(request, 'inicio/convenios.html', {'convenios':convenios}, context_instance=RequestContext(request))



def agregar_convenio(request):
	if request.method == "POST":
		form = ConveniosForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			mensaje = "Guardado"
			return render(request, 'inicio/agregar_convenio.html', {'mensaje': mensaje}, context_instance=RequestContext(request))
	else:
		form = ConveniosForm()
	return render(request, 'inicio/agregar_convenio.html', {'form':form}, context_instance=RequestContext(request))

def consultar_convenio(request, convenio_id):
	convenio= Convenios.objects.get(id=convenio_id)
	form = ConsultarConveniosForm(model_to_dict(convenio))
	return render(request, 'inicio/consultar_convenio.html', {'form':form}, context_instance=RequestContext(request))

def editar_convenio(request, convenio_id):
	if request.method == "POST":
		form = ConveniosForm(request.POST)
		if form.is_valid():
			convenio = Convenios.objects.get(id=convenio_id)
			convenio.numero_universidad = form.cleaned_data['numero_universidad']
			convenio.siglas_universidad = form.cleaned_data['siglas_universidad']
			convenio.archivo=form.cleaned_data['archivo']
			convenio.fecha_creacion=form.cleaned_data['fecha_creacion']		
			convenio.encargado=form.cleaned_data['encargado']					
			convenio.save()
			mensaje = "Guardado"
			return render(request, 'inicio/editar_convenios.html', {'mensaje': mensaje}, context_instance=RequestContext(request))
	else:					
		try:
			convenio = Convenios.objects.get(id=convenio_id)
		except:
			convenio = None

		form = ConveniosForm(instance=convenio)	

	return render(request, 'inicio/editar_anexotecnico.html', {'form': form}, context_instance=RequestContext(request))	

def eliminar_convenio(request, convenio_id):
	try:
		convenio = Convenios.objects.get(id=convenio_id)
		try:
			convenio.delete()
			mensaje = "Eliminado"
		except:
			mensaje = "Falló al eliminar"
	except:
		convenio = None
		mensaje = "Error inesperado"

	return render(request, 'inicio/eliminar_convenio.html',{'mensaje': mensaje}, context_instance=RequestContext(request))

#y hasta aqui es el fin de propuestas

def propuestas(request):
	propuestas = Propuestas.objects.all()

	paginator = Paginator(propuestas, 10)
	page = request.GET.get('page', 1)

	try:
		propuestas = paginator.page(page)
	except PageNotAnInteger:
		propuestas = paginator.page(1)
	except EmptyPage:
		propuestas = paginator.page(paginator.num_pages)

	return render(request, 'inicio/propuestas.html', {'propuestas':propuestas}, context_instance=RequestContext(request))



def agregar_propuesta(request):
	if request.method == "POST":
		form = PropuestasForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			mensaje = "Guardado"
			return render(request, 'inicio/agregar_propuesta.html', {'mensaje': mensaje}, context_instance=RequestContext(request))
	else:
		form = PropuestasForm()
	return render(request, 'inicio/agregar_propuesta.html', {'form':form}, context_instance=RequestContext(request))

def consultar_propuesta(request, propuesta_id):
	propuesta= Propuestas.objects.get(id=propuesta_id)
	form = ConsultarPropuestasForm(model_to_dict(propuesta))
	return render(request, 'inicio/consultar_propuesta.html', {'form':form}, context_instance=RequestContext(request))

def editar_propuesta(request, propuesta_id):
	if request.method == "POST":
		form = PropuestasForm(request.POST)
		if form.is_valid():
			propuesta = Propuestas.objects.get(id=propuesta_id)
			propuesta.numero_oficio = form.cleaned_data['numero_oficio']
			propuesta.proyecto = form.cleaned_data['proyecto']
			propuesta.responsable =form.cleaned_data['responsable']
			propuesta.nombre_dependencia=form.cleaned_data['nombre_dependencia']		
			propuesta.siglas_dependencia=form.cleaned_data['siglas_dependencia']
			propuesta.tipo = form.cleaned_data['tipo']
			propuesta.nombre = form.cleaned_data['nombre']
			propuesta.siglas = form.cleaned_data['siglas']
			propuesta.save()
			mensaje = "Guardado"
			return render(request, 'inicio/editar_convenios.html', {'mensaje': mensaje}, context_instance=RequestContext(request))
	else:					
		try:
			propuesta = Propuestas.objects.get(id=propuesta_id)
		except:
			propuesta = None

		form = PropuestasForm(instance=propuesta)	

	return render(request, 'inicio/editar_anexotecnico.html', {'form': form}, context_instance=RequestContext(request))	

def eliminar_propuesta(request, propuesta_id):
	try:
		propuesta = Propuestas.objects.get(id=propuesta_id)
		try:
			propuesta.delete()
			mensaje = "Eliminado"
		except:
			mensaje = "Falló al eliminar"
	except:
		propuesta = None
		mensaje = "Error inesperado"

	return render(request, 'inicio/eliminar_propuesta.html',{'mensaje': mensaje}, context_instance=RequestContext(request))
#y hasta aqui es el fin de propuestas




#views de empresas
def empresas(request):
	empresas_list = Empresas.objects.all()

	paginator = Paginator(empresas_list, 10)
	page = request.GET.get('page', 1)

	try:
		empresas = paginator.page(page)
	except PageNotAnInteger:
		empresas = paginator.page(1)
	except EmptyPage:
		empresas = paginator.page(paginator.num_pages)

	return render(request, 'inicio/empresas.html', {'empresas':empresas}, context_instance=RequestContext(request))

def consultar_empresa(request, empresa_id):
	empresa= Empresas.objects.get(id=empresa_id)
	form = ConsultarEmpresasForm(model_to_dict(empresa))
	return render(request, 'inicio/consultar_empresa.html', {'form':form}, context_instance=RequestContext(request))

def agregar_empresa(request):
	if request.method == "POST":
		form = EmpresasForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			mensaje = "Guardado"
			return render(request, 'inicio/agregar_empresa.html', {'mensaje': mensaje}, context_instance=RequestContext(request))
	else:
		form = EmpresasForm()
	return render(request, 'inicio/agregar_empresa.html', {'form':form}, context_instance=RequestContext(request))

def editar_empresa(request, empresa_id):
	if request.method == "POST":
		form = EmpresasForm(request.POST)
		if form.is_valid():
			empresa = Empresas.objects.get(id=empresa_id)
			empresa.nombre = form.cleaned_data['nombre']
			empresa.save()
			mensaje = "Guardado"
			return render(request, 'inicio/editar_empresa.html', {'mensaje': mensaje}, context_instance=RequestContext(request))
	else:					
		try:
			empresa = Empresas.objects.get(id=empresa_id)
		except:
			empresa = None

		form = EmpresasForm(instance=empresa)	

	return render(request, 'inicio/editar_empresa.html', {'form': form}, context_instance=RequestContext(request))

def eliminar_empresa(request, empresa_id):
	try:
		empresa = Empresas.objects.get(id=empresa_id)
		try:
			empresa.delete()
			mensaje = "Eliminado"
		except:
			mensaje = "Falló al eliminar"
	except:
		empresa = None
		mensaje = "Error inesperado"

	return render(request, 'inicio/eliminar_empresa.html',{'mensaje': mensaje}, context_instance=RequestContext(request))
#teminan las view de empresas
def registrar_contratos(request):
	form = ContratosForm()
	return render(request, 'inicio/registrar_contratos.html', {'form': form}, context_instance=RequestContext(request))

def registrar_convenios(request):
	form = ConveniosForm()
	return render(request, 'inicio/registrar_convenios.html', {'form': form}, context_instance=RequestContext(request))

def registrar_propuestas(request):
	form = PropuestasForm()
	return render(request, 'inicio/registrar_propuestas.html', {'form': form}, context_instance=RequestContext(request))

def registrar_empresa(request):
	form = EmpresasForm
	return render(request, 'inicio/registrar_empresa.html', {'form': form}, context_instance=RequestContext(request))

def registrar_entregable(request):
	form = EntregablesForm()
	return render(request, 'inicio/registrar_entregable.html', {'form': form}, context_instance=RequestContext(request))

def registrar_personal(request):
	form = PersonalForm()
	return render(request, 'inicio/registrar_personal.html', {'form': form}, context_instance=RequestContext(request))

def inicio(request):
	if request.method == "POST":
		form = AuthForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			try:
				usuario = authenticate(username = username, password=password)
			except:
				usuario = None
			print usuario
			if usuario is not None:
				if usuario.is_active:                        
					login(request, usuario)
					request.session.set_expiry(settings.TIEMPO_EXPIRACION_SESION)
					return HttpResponseRedirect('administrar_usuarios')
				else:
					mensaje = "Usuario inactivo"
					return render(request, 'inicio/login.html', {'form': form, 'mensaje': mensaje}, context_instance=RequestContext(request))					
			else:
				mensaje = "Usuario o contraseña incorrectos"
				return render(request, 'inicio/login.html', {'form': form, 'mensaje': mensaje}, context_instance=RequestContext(request))
		else:
			return render(request, 'inicio/login.html', {'form': form }, context_instance=RequestContext(request))
	else:
		form = AuthForm()
	return render(request, 'inicio/login.html', {'form': form }, context_instance=RequestContext(request))

@login_required(login_url="/inicio")
def administrar_usuarios(request):
	return render(request, 'inicio/administrar_usuarios.html',{},context_instance=RequestContext(request))

