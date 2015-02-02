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
							ConsultarContratoForm
						  )

from inicio.models import ( AnexosTecnicos,
							Contratos,
							Facturas
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
		form = facturasForm(request.POST)
		if form.is_valid():
			factura = facturas.objects.get(id=factura_id)
			factura.numero_oficio = form.cleaned_data['numero_oficio']
			factura.proyecto = form.cleaned_data['proyecto']
			factura.encargado=form.cleaned_data['encargado']
			factura.cliente=form.cleaned_data['cliente']		
			factura.fecha_creacion = form.cleaned_data['fecha_creacion']
			factura.archivo = form.cleaned_data['archivo']
			factura.save()
			mensaje = "Guardado"
			return render(request, 'inicio/editar_facturas.html', {'mensaje': mensaje}, context_instance=RequestContext(request))
	else:					
		try:
			factura = facturas.objects.get(id=factura_id)
		except:
			factura = None

		form = FacturasForm(instance=factura)	

	return render(request, 'inicio/editar_anexotecnico.html', {'form': form}, context_instance=RequestContext(request))

def eliminar_factura(request, factura_id):
	try:
		factura = facturas.objects.get(id=factura_id)
		try:
			factura.delete()
			mensaje = "Eliminado"
		except:
			mensaje = "Falló al eliminar"
	except:
		factura = None
		mensaje = "Error inesperado"

	return render(request, 'inicio/eliminar_factura.html',{'mensaje': mensaje}, context_instance=RequestContext(request))


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

