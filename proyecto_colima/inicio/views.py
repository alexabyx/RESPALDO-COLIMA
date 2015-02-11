#! -*- coding:utf-8 -*-
# Create your views here.

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage
from django.contrib.auth import authenticate, login, logout
from django.forms.models import model_to_dict
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404

from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView

from inicio.models import ( Proyectos,
							Personal,
							Clientes,
							AnexosTecnicos,
							Contratos,
							Facturas,
							Convenios,
							Propuestas,
							Entidades,
							Entregables,
						  )

from inicio.forms import (	RegistrarProyectoForm,
							RegistrarFacturaForm, 
							RegistrarAnexotecnicoForm,
							RegistrarContratoForm,
							RegistrarConvenioForm,
							RegistrarPropuestaForm,
							RegistrarPersonalForm,
							RegistrarClienteForm,
							RegistrarEntidadForm,
							RegistrarEntregableForm,
						  )
#
#==================OPERACIONES DE PROYECTOS========================
#

@login_required(login_url='/')
def proyectos(request):
	proyectos_list = Proyectos.objects.filter(habilitado=True)

	paginator = Paginator(proyectos_list, 9)
	page = request.GET.get('page', 1)

	try:
		proyectos = paginator.page(page)
	except PageNotAnInteger:
		proyectos = paginator.page(1)
	except EmptyPage:
		proyectos = paginator.page(paginator.num_pages)

	return render(request, 'inicio/proyectos.html', {'proyectos': proyectos}, context_instance=RequestContext(request))

class ProyectoDetailView(DetailView):
	
	template_name = "inicio/proyecto_detail.html"
	model = Proyectos

	def get_object(self):
		object = super(ProyectoDetailView, self).get_object()
		return object

def editar_proyecto(request, pk):
	if request.method=="POST":
		form = RegistrarProyectoForm(request.POST)
		if form.is_valid():
			try:
				Proyectos.objects.filter(id=int(pk)).update( 
															nombre = form.cleaned_data['nombre'],
															siglas = form.cleaned_data['siglas'],
															fecha_inicio = form.cleaned_data['fecha_inicio'],
															fecha_fin = form.cleaned_data['fecha_fin'],
															avance = form.cleaned_data['avance'],
															comentario = form.cleaned_data['comentario'],
															cliente = form.cleaned_data['cliente'],								
															)

				proyecto = Proyectos.objects.get(id = int(pk))

				proyecto.responsable.clear()			

				for responsable in form.cleaned_data['responsable']:
					personal = Personal.objects.get(id = int(responsable))
					proyecto.responsable.add(personal)
				proyecto.save()

				return HttpResponseRedirect('/administracion/proyectos/')
			except Exception, e:				
				print "Error: ", e
				mensaje = "El proyecto no pudo ser actualizado"
		else:
			print "No paso"
	else:
		proyecto = Proyectos.objects.get(id=int(pk))
		form=RegistrarProyectoForm(model_to_dict(proyecto))
	return render(request, 'inicio/proyecto_edit.html', {'form': form})

def crear_proyecto(request):
	if request.method=="POST":
		form = RegistrarProyectoForm(request.POST)
		if form.is_valid():
			proyecto = Proyectos.objects.create(
												nombre = form.cleaned_data['nombre'],
												siglas = form.cleaned_data['siglas'],
												fecha_inicio = form.cleaned_data['fecha_inicio'],
												fecha_fin = form.cleaned_data['fecha_fin'],
												avance = form.cleaned_data['avance'],
												comentario = form.cleaned_data['comentario'],
												cliente = form.cleaned_data['cliente'],
												)
			for responsable in form.cleaned_data['responsable']:
				personal = Personal.objects.get(id = int(responsable))
				proyecto.responsable.add(personal)
			proyecto.save()

			mensaje = "El proyecto ha sido creado exitosamente"
			return HttpResponseRedirect('/administracion/proyectos/')
		else:
			print "No paso"
	else:
		form=RegistrarProyectoForm()
	return render(request, 'inicio/proyecto_create.html', {'form': form})

def eliminar_proyecto(request):
	import json

	if not request.is_ajax():
		raise Http404

	pk = request.POST.get('pk')

	try:
		proyecto = Proyectos.objects.filter(id=pk).update(habilitado=False)
	except Exception, e:
		print "Error: ", e
		mensaje = {'mensaje': "Fallo la operación", 'error': True}
	else:
		mensaje = {'mensaje': "Operación exitosa", 'error': False}

	content = json.dumps(mensaje)
	http_response = HttpResponse(content, content_type="application/json")

	return http_response	

#
#==================OPERACIONES DE FACTURAS========================
#
def facturas(request):
	facturas_list = Facturas.objects.all()

	paginator = Paginator(facturas_list, 9)
	page = request.GET.get('page', 1)

	try:
		facturas = paginator.page(page)
	except PageNotAnInteger:
		facturas = paginator.page(1)
	except EmptyPage:
		facturas = paginator.page(paginator.num_pages)

	return render(request, 'inicio/facturas.html', {'facturas': facturas}, context_instance=RequestContext(request))

class FacturaDetailView(DetailView):
	
	template_name = "inicio/factura_detail.html"
	model = Facturas

	def get_object(self):
		object = super(FacturaDetailView, self).get_object()
		return object

def editar_factura(request, pk):
	if request.method=="POST":
		form = RegistrarFacturaForm(request.POST, request.FILES)
		if form.is_valid():
			try:
				Facturas.objects.filter(id=int(pk)).update(
															contrato 			= form.cleaned_data['contrato'],
															responsable 		= form.cleaned_data['responsable'],
															tipo 				= form.cleaned_data['tipo'],
															nombre 				= form.cleaned_data['nombre'],
															siglas 				= form.cleaned_data['siglas'],
															numero_factura 		= form.cleaned_data['numero_factura'],
															fecha_factura 		= form.cleaned_data['fecha_factura'],
															folio_venta 		= form.cleaned_data['folio_venta'],
															rfc 				= form.cleaned_data['rfc'],
															direccion 			= form.cleaned_data['direccion'],
															subtotal 			= form.cleaned_data['subtotal'],
															iva 				= form.cleaned_data['iva'],
															total_con_numero 	= form.cleaned_data['total_con_numero'],
															total_con_letra 	= form.cleaned_data['total_con_letra'],
															pagada 				= form.cleaned_data['pagada'],
															archivo_xml 		= form.cleaned_data['archivo_xml'],
															archivo_fisico 		= form.cleaned_data['archivo_fisico'],
															)

				return HttpResponseRedirect('/administracion/facturas/')
			except Exception, e:				
				print "Error: ", e
				mensaje = "La factura no pudo ser actualizada"
		else:
			print "No paso"
	else:
		factura = Facturas.objects.get(id=int(pk))
		form=RegistrarFacturaForm(model_to_dict(factura))
	return render(request, 'inicio/factura_edit.html', {'form': form})

def crear_factura(request):
	if request.method=="POST":
		form = RegistrarFacturaForm(request.POST, request.FILES)
		if form.is_valid():
			factura = Facturas.objects.create(
												contrato 			= form.cleaned_data['contrato'],
												responsable 		= form.cleaned_data['responsable'],
												tipo 				= form.cleaned_data['tipo'],
												nombre 				= form.cleaned_data['nombre'],
												siglas 				= form.cleaned_data['siglas'],
												numero_factura 		= form.cleaned_data['numero_factura'],
												fecha_factura 		= form.cleaned_data['fecha_factura'],
												folio_venta 		= form.cleaned_data['folio_venta'],
												rfc 				= form.cleaned_data['rfc'],
												direccion 			= form.cleaned_data['direccion'],
												subtotal 			= form.cleaned_data['subtotal'],
												iva 				= form.cleaned_data['iva'],
												total_con_numero 	= form.cleaned_data['total_con_numero'],
												total_con_letra 	= form.cleaned_data['total_con_letra'],
												pagada 				= form.cleaned_data['pagada'],
												archivo_xml 		= form.cleaned_data['archivo_xml'],
												archivo_fisico 		= form.cleaned_data['archivo_fisico'],
												)

			mensaje = "La factura ha sido creada exitosamente"
			return HttpResponseRedirect('/administracion/facturas/')

		else:
			print "No paso"
	else:
		form=RegistrarFacturaForm()
	return render(request, 'inicio/factura_create.html', {'form': form})

#
#==================OPERACIONES DE ANEXOSTECNICOS========================
#
def anexostecnicos(request):
	anexostecnicos_list = AnexosTecnicos.objects.filter(habilitado=True).order_by('-fecha_creacion')

	paginator = Paginator(anexostecnicos_list, 9)
	page = request.GET.get('page', 1)

	try:
		anexostecnicos = paginator.page(page)
	except PageNotAnInteger:
		anexostecnicos = paginator.page(1)
	except EmptyPage:
		anexostecnicos = paginator.page(paginator.num_pages)

	return render(request, 'inicio/anexostecnicos.html', {'anexostecnicos':anexostecnicos}, context_instance=RequestContext(request))

def crear_anexotecnico(request):
	if request.method=="POST":
		form = RegistrarAnexotecnicoForm(request.POST, request.FILES)
		if form.is_valid():
			anexotecnico = AnexosTecnicos.objects.create(
														numero_oficio 	= form.cleaned_data['numero_oficio'],	
														proyecto 		= form.cleaned_data['proyecto'],
														nombre 			= form.cleaned_data['nombre'],
														siglas 			= form.cleaned_data['siglas'],
														status 			= form.cleaned_data['status'],
														archivo         = form.cleaned_data['archivo'],
														)

			mensaje = "El anexotecnico ha sido creado exitosamente"
			return HttpResponseRedirect('/administracion/anexostecnicos/')
		else:
			print "No paso"
	else:
		form=RegistrarAnexotecnicoForm()
	return render(request, 'inicio/anexotecnico_create.html', {'form': form})

def editar_anexotecnico(request, pk):
	if request.method=="POST":
		form = RegistrarAnexotecnicoForm(request.POST, request.FILES)
		if form.is_valid():
			try:
				AnexosTecnicos.objects.filter(id=int(pk)).update(
																numero_oficio 	= form.cleaned_data['numero_oficio'],	
																proyecto 		= form.cleaned_data['proyecto'],
																nombre 			= form.cleaned_data['nombre'],
																siglas 			= form.cleaned_data['siglas'],
																status 			= form.cleaned_data['status'],
																archivo         = form.cleaned_data['archivo'],
																)

				return HttpResponseRedirect('/administracion/anexostecnicos/')
			except Exception, e:				
				print "Error: ", e
				mensaje = "El anexotecnico no pudo ser actualizado"
		else:
			print "No paso"
	else:
		anexotecnico = AnexosTecnicos.objects.get(id=int(pk))
		form=RegistrarAnexotecnicoForm(model_to_dict(anexotecnico))
	return render(request, 'inicio/anexotecnico_edit.html', {'form': form})

class AnexotecnicoDetailView(DetailView):
	
	template_name = "inicio/anexotecnico_detail.html"
	model = AnexosTecnicos

	def get_object(self):
		object = super(AnexotecnicoDetailView, self).get_object()
		return object

def eliminar_anexotecnico(request):
	import json

	if not request.is_ajax():
		raise Http404

	pk = request.POST.get('pk')

	try:
		proyecto = AnexosTecnicos.objects.filter(id=pk).update(habilitado=False)
	except Exception, e:
		print "Error: ", e
		mensaje = {'mensaje': "Fallo la operación", 'error': True}
	else:
		mensaje = {'mensaje': "Operación exitosa", 'error': False}

	content = json.dumps(mensaje)
	http_response = HttpResponse(content, content_type="application/json")

	return http_response

#
#==================OPERACIONES DE CONTATOS========================
#

def contratos(request):
	contratos_list = Contratos.objects.filter(habilitado=True).order_by('-fecha_creacion')

	paginator = Paginator(contratos_list, 9)
	page = request.GET.get('page', 1)

	try:
		contratos = paginator.page(page)
	except PageNotAnInteger:
		contratos = paginator.page(1)
	except EmptyPage:
		contratos = paginator.page(paginator.num_pages)

	return render(request, 'inicio/contratos.html', {'contratos':contratos}, context_instance=RequestContext(request))

class ContratoDetailView(DetailView):
	
	template_name = "inicio/contrato_detail.html"
	model = Contratos

	def get_object(self):
		object = super(ContratoDetailView, self).get_object()
		return object

def crear_contrato(request):
	if request.method=="POST":
		form = RegistrarContratoForm(request.POST, request.FILES)
		if form.is_valid():
			contrato = Contratos.objects.create(
												numero_oficio 	= form.cleaned_data['numero_oficio'],	
												proyecto 		= form.cleaned_data['proyecto'],
												encargado 		= form.cleaned_data['encargado'],
												archivo         = form.cleaned_data['archivo'],
												)

			mensaje = "El contrato ha sido creado exitosamente"
			return HttpResponseRedirect('/administracion/contratos/')
		else:
			print "No paso"
	else:
		form=RegistrarContratoForm()
	return render(request, 'inicio/contrato_create.html', {'form': form})

def editar_contrato(request, pk):
	if request.method=="POST":
		form = RegistrarContratoForm(request.POST, request.FILES)
		if form.is_valid():
			try:
				Contratos.objects.filter(id=int(pk)).update(
															numero_oficio 	= form.cleaned_data['numero_oficio'],	
															proyecto 		= form.cleaned_data['proyecto'],
															encargado 			= form.cleaned_data['encargado'],
															archivo         = form.cleaned_data['archivo'],
															)

				return HttpResponseRedirect('/administracion/contratos/')
			except Exception, e:				
				print "Error: ", e
				mensaje = "El contrato no pudo ser actualizado"
		else:
			print "No paso"
	else:
		contrato = Contratos.objects.get(id=int(pk))
		form=RegistrarContratoForm(model_to_dict(contrato))
	return render(request, 'inicio/contrato_edit.html', {'form': form})	

def eliminar_contrato(request):
	import json

	if not request.is_ajax():
		raise Http404

	pk = request.POST.get('pk')

	try:
		contrato = Contratos.objects.filter(id=pk).update(habilitado=False)
	except Exception, e:
		print "Error: ", e
		mensaje = {'mensaje': "Fallo la operación", 'error': True}
	else:
		mensaje = {'mensaje': "Operación exitosa", 'error': False}

	content = json.dumps(mensaje)
	http_response = HttpResponse(content, content_type="application/json")

	return http_response

#
#==================OPERACIONES DE CONVENIOS========================
#
def convenios(request):
	convenios_list = Convenios.objects.filter(habilitado=True).order_by('-fecha_creacion')

	paginator = Paginator(convenios_list, 9)
	page = request.GET.get('page', 1)

	try:
		convenios = paginator.page(page)
	except PageNotAnInteger:
		convenios = paginator.page(1)
	except EmptyPage:
		convenios = paginator.page(paginator.num_pages)

	return render(request, 'inicio/convenios.html', {'convenios':convenios}, context_instance=RequestContext(request))

class ConvenioDetailView(DetailView):
	
	template_name = "inicio/convenio_detail.html"
	model = Convenios

	def get_object(self):
		object = super(ConvenioDetailView, self).get_object()
		return object

def crear_convenio(request):
	if request.method=="POST":
		form = RegistrarConvenioForm(request.POST, request.FILES)
		if form.is_valid():
			convenio = Convenios.objects.create(
												numero 		= form.cleaned_data['numero'],
												proyecto 	= form.cleaned_data['proyecto'],
												encargado 	= form.cleaned_data['encargado'],
												archivo 	= form.cleaned_data['archivo'],
												)

			mensaje = "El convenio ha sido creado exitosamente"
			return HttpResponseRedirect('/administracion/convenios/')
		else:
			print "No paso"
	else:
		form=RegistrarConvenioForm()
	return render(request, 'inicio/convenio_create.html', {'form': form})

def editar_convenio(request, pk):
	if request.method=="POST":
		form = RegistrarConvenioForm(request.POST, request.FILES)
		if form.is_valid():
			try:
				Convenios.objects.filter(id=int(pk)).update(
															numero 		= form.cleaned_data['numero'],
															proyecto 	= form.cleaned_data['proyecto'],
															encargado 	= form.cleaned_data['encargado'],
															archivo 	= form.cleaned_data['archivo'],					
															)

				return HttpResponseRedirect('/administracion/convenios/')
			except Exception, e:				
				print "Error: ", e
				mensaje = "El convenio no pudo ser actualizado"
		else:
			print "No paso"
	else:
		convenio = Convenios.objects.get(id=int(pk))
		form=RegistrarConvenioForm(model_to_dict(convenio))
	return render(request, 'inicio/convenio_edit.html', {'form': form})	

def eliminar_convenio(request):
	import json

	if not request.is_ajax():
		raise Http404

	pk = request.POST.get('pk')

	try:
		contrato = Convenios.objects.filter(id=pk).update(habilitado=False)
	except Exception, e:
		print "Error: ", e
		mensaje = {'mensaje': "Fallo la operación", 'error': True}
	else:
		mensaje = {'mensaje': "Operación exitosa", 'error': False}

	content = json.dumps(mensaje)
	http_response = HttpResponse(content, content_type="application/json")

	return http_response

#
#==================OPERACIONES DE PROPUESTAS========================
#
def propuestas(request):
	propuestas_list = Propuestas.objects.filter(habilitado=True).order_by('-fecha_creacion')

	paginator = Paginator(propuestas_list, 9)
	page = request.GET.get('page', 1)

	try:
		propuestas = paginator.page(page)
	except PageNotAnInteger:
		propuestas = paginator.page(1)
	except EmptyPage:
		propuestas = paginator.page(paginator.num_pages)

	return render(request, 'inicio/propuestas.html', {'propuestas':propuestas}, context_instance=RequestContext(request))

class PropuestaDetailView(DetailView):
	
	template_name = "inicio/propuesta_detail.html"
	model = Propuestas

	def get_object(self):
		object = super(PropuestaDetailView, self).get_object()
		return object

def crear_propuesta(request):
	if request.method=="POST":
		form = RegistrarPropuestaForm(request.POST)
		if form.is_valid():
			propuestas = Propuestas.objects.create(
												numero_oficio 	= form.cleaned_data['numero_oficio'],
												proyecto 		= form.cleaned_data['proyecto'],
												responsable 	= form.cleaned_data['responsable'],
												)

			mensaje = "La propuesta ha sido creada exitosamente"
			return HttpResponseRedirect('/administracion/propuestas/')
		else:
			print "No paso"
	else:
		form=RegistrarPropuestaForm()
	return render(request, 'inicio/propuesta_create.html', {'form': form})

def editar_propuesta(request, pk):
	if request.method=="POST":
		form = RegistrarPropuestaForm(request.POST)
		if form.is_valid():
			try:
				Propuestas.objects.filter(id=int(pk)).update(
															numero_oficio 	= form.cleaned_data['numero_oficio'],
															proyecto 		= form.cleaned_data['proyecto'],
															responsable 	= form.cleaned_data['responsable'],
															)

				return HttpResponseRedirect('/administracion/propuestas/')
			except Exception, e:				
				print "Error: ", e
				mensaje = "El convenio no pudo ser actualizado"
		else:
			print "No paso"
	else:
		propuesta = Propuestas.objects.get(id=int(pk))
		form=RegistrarPropuestaForm(model_to_dict(propuesta))
	return render(request, 'inicio/propuesta_edit.html', {'form': form})	

def eliminar_propuesta(request):
	import json

	if not request.is_ajax():
		raise Http404

	pk = request.POST.get('pk')

	try:
		propuesta = Propuestas.objects.filter(id=pk).update(habilitado=False)
	except Exception, e:
		print "Error: ", e
		mensaje = {'mensaje': "Fallo la operación", 'error': True}
	else:
		mensaje = {'mensaje': "Operación exitosa", 'error': False}

	content = json.dumps(mensaje)
	http_response = HttpResponse(content, content_type="application/json")

	return http_response

#
#==================OPERACIONES DE PERSONAL========================
#
def personal(request):
	personal_list = Personal.objects.filter(habilitado=True).order_by('-fecha_ingreso')

	paginator = Paginator(personal_list, 9)
	page = request.GET.get('page', 1)

	try:
		personal = paginator.page(page)
	except PageNotAnInteger:
		personal = paginator.page(1)
	except EmptyPage:
		personal = paginator.page(paginator.num_pages)

	return render(request, 'inicio/personal.html', {'personal':personal}, context_instance=RequestContext(request))

class PersonalDetailView(DetailView):
	
	template_name = "inicio/personal_detail.html"
	model = Personal

	def get_object(self):
		object = super(PersonalDetailView, self).get_object()
		return object

def crear_personal(request):
	if request.method=="POST":
		form = RegistrarPersonalForm(request.POST, request.FILES)
		if form.is_valid():
			personal = Personal.objects.create(	
												rfc 						= form.cleaned_data['rfc'],
												credencial_elector 			= form.cleaned_data['credencial_elector'],
												nombre 						= form.cleaned_data['nombre'],
												apellido_paterno 			= form.cleaned_data['apellido_paterno'],
												apellido_materno 			= form.cleaned_data['apellido_materno'],
												siglas_nombre 				= form.cleaned_data['siglas_nombre'],
												genero 						= form.cleaned_data['genero'],
												direccion 					= form.cleaned_data['direccion'],
												telefono 					= form.cleaned_data['telefono'],
												no_seguro 					= form.cleaned_data['no_seguro'],
												fecha_ingreso 				= form.cleaned_data['fecha_ingreso'],
												puesto 						= form.cleaned_data['puesto'],
												turno 						= form.cleaned_data['turno'],
												tipo_plaza 					= form.cleaned_data['tipo_plaza'],
												especificacion 				= form.cleaned_data['especificacion'],
												tipo_pago 					= form.cleaned_data['tipo_pago'],
												monto 						= form.cleaned_data['monto'],
												dias_trabajo_al_mes 		= form.cleaned_data['dias_trabajo_al_mes'],
												fecha_vencimiento_contrato 	= form.cleaned_data['fecha_vencimiento_contrato'],
												fecha_baja 					= form.cleaned_data['fecha_baja'],
												motivo_baja 				= form.cleaned_data['motivo_baja'],
												)

			mensaje = "El empleado ha sido creada exitosamente"
			return HttpResponseRedirect('/administracion/personal/')
		else:
			print "No paso"
	else:
		form=RegistrarPersonalForm()
	return render(request, 'inicio/personal_create.html', {'form': form})

def editar_personal(request, pk):
	if request.method=="POST":
		form = RegistrarPersonalForm(request.POST, request.FILES)
		if form.is_valid():
			try:
				Personal.objects.filter(id=int(pk)).update(
															rfc 						= form.cleaned_data['rfc'],
															credencial_elector 			= form.cleaned_data['credencial_elector'],
															nombre 						= form.cleaned_data['nombre'],
															apellido_paterno 			= form.cleaned_data['apellido_paterno'],
															apellido_materno 			= form.cleaned_data['apellido_materno'],
															siglas_nombre 				= form.cleaned_data['siglas_nombre'],
															genero 						= form.cleaned_data['genero'],
															direccion 					= form.cleaned_data['direccion'],
															telefono 					= form.cleaned_data['telefono'],
															no_seguro 					= form.cleaned_data['no_seguro'],
															fecha_ingreso 				= form.cleaned_data['fecha_ingreso'],
															puesto 						= form.cleaned_data['puesto'],
															turno 						= form.cleaned_data['turno'],
															tipo_plaza 					= form.cleaned_data['tipo_plaza'],
															especificacion 				= form.cleaned_data['especificacion'],
															tipo_pago 					= form.cleaned_data['tipo_pago'],
															monto 						= form.cleaned_data['monto'],
															dias_trabajo_al_mes 		= form.cleaned_data['dias_trabajo_al_mes'],
															fecha_vencimiento_contrato 	= form.cleaned_data['fecha_vencimiento_contrato'],
															fecha_baja 					= form.cleaned_data['fecha_baja'],
															motivo_baja 				= form.cleaned_data['motivo_baja'],
															)

				return HttpResponseRedirect('/administracion/personal/')
			except Exception, e:				
				print "Error: ", e
				mensaje = "El convenio no pudo ser actualizado"
		else:
			print "No paso"
	else:
		personal = Personal.objects.get(id=int(pk))
		form=RegistrarPersonalForm(model_to_dict(personal))
	return render(request, 'inicio/personal_edit.html', {'form': form})	

def eliminar_personal(request):
	import json

	if not request.is_ajax():
		raise Http404

	pk = request.POST.get('pk')

	try:
		personal = Personal.objects.filter(id=pk).update(habilitado=False)
	except Exception, e:
		print "Error: ", e
		mensaje = {'mensaje': "Fallo la operación", 'error': True}
	else:
		mensaje = {'mensaje': "Operación exitosa", 'error': False}

	content = json.dumps(mensaje)
	http_response = HttpResponse(content, content_type="application/json")

	return http_response

#
#==================OPERACIONES DE CLIENTES========================
#

def clientes(request):
	clientes_list = Clientes.objects.filter(habilitado=True).order_by('-fecha_creacion')

	paginator = Paginator(clientes_list, 9)
	page = request.GET.get('page', 1)

	try:
		clientes = paginator.page(page)
	except PageNotAnInteger:
		clientes = paginator.page(1)
	except EmptyPage:
		clientes = paginator.page(paginator.num_pages)

	return render(request, 'inicio/clientes.html', {'clientes':clientes}, context_instance=RequestContext(request))

class ClienteDetailView(DetailView):
	
	template_name = "inicio/cliente_detail.html"
	model = Clientes

	def get_object(self):
		object = super(ClienteDetailView, self).get_object()
		return object

def crear_cliente(request):
	if request.method=="POST":
		form = RegistrarClienteForm(request.POST)
		if form.is_valid():
			cliente = Clientes.objects.create(
												nombre 	= form.cleaned_data['nombre'],
												siglas	= form.cleaned_data['siglas'],
												)

			mensaje = "El cliente ha sido creada exitosamente"
			return HttpResponseRedirect('/administracion/clientes/')
		else:
			print "No paso"
	else:
		form=RegistrarClienteForm()
	return render(request, 'inicio/cliente_create.html', {'form': form})

def editar_cliente(request, pk):
	if request.method=="POST":
		form = RegistrarClienteForm(request.POST)
		if form.is_valid():
			try:
				Clientes.objects.filter(id=int(pk)).update(
															nombre 	= form.cleaned_data['nombre'],
															siglas	= form.cleaned_data['siglas'],
															)

				return HttpResponseRedirect('/administracion/clientes/')
			except Exception, e:				
				print "Error: ", e
				mensaje = "El cliente no pudo ser actualizado"
		else:
			print "No paso"
	else:
		cliente = Clientes.objects.get(id=int(pk))
		form=RegistrarClienteForm(model_to_dict(cliente))
	return render(request, 'inicio/cliente_edit.html', {'form': form})	

def eliminar_cliente(request):
	import json

	if not request.is_ajax():
		raise Http404

	pk = request.POST.get('pk')

	try:
		cliente = Clientes.objects.filter(id=pk).update(habilitado=False)
	except Exception, e:
		print "Error: ", e
		mensaje = {'mensaje': "Fallo la operación", 'error': True}
	else:
		mensaje = {'mensaje': "Operación exitosa", 'error': False}

	content = json.dumps(mensaje)
	http_response = HttpResponse(content, content_type="application/json")

	return http_response
#
#==================OPERACIONES DE ENTIDADES========================
#

def entidades(request):
	entidades_list = Entidades.objects.filter(habilitado=True).order_by('-fecha_creacion')

	paginator = Paginator(entidades_list, 9)
	page = request.GET.get('page', 1)

	try:
		entidades = paginator.page(page)
	except PageNotAnInteger:
		entidades = paginator.page(1)
	except EmptyPage:
		entidades = paginator.page(paginator.num_pages)

	return render(request, 'inicio/entidades.html', {'entidades':entidades}, context_instance=RequestContext(request))

class EntidadDetailView(DetailView):
	
	template_name = "inicio/entidad_detail.html"
	model = Entidades

	def get_object(self):
		object = super(EntidadDetailView, self).get_object()
		return object

def crear_entidad(request):
	if request.method=="POST":
		form = RegistrarEntidadForm(request.POST)
		if form.is_valid():
			entidad = Entidades.objects.create(
												nombre 	= form.cleaned_data['nombre'],
												siglas 	= form.cleaned_data['siglas'], 
												tipo 	= form.cleaned_data['tipo'],
												)

			mensaje = "La entidad ha sido creada exitosamente"
			return HttpResponseRedirect('/administracion/entidades/')
		else:
			print "No paso"
	else:
		form=RegistrarEntidadForm()
	return render(request, 'inicio/entidad_create.html', {'form': form})

def editar_entidad(request, pk):
	if request.method=="POST":
		form = RegistrarEntidadForm(request.POST)
		if form.is_valid():
			try:
				Entidades.objects.filter(id=int(pk)).update(
															nombre 	= form.cleaned_data['nombre'],
															siglas 	= form.cleaned_data['siglas'], 
															tipo 	= form.cleaned_data['tipo'],
															)

				return HttpResponseRedirect('/administracion/entidades/')
			except Exception, e:				
				print "Error: ", e
				mensaje = "La entidad no pudo ser actualizada"
		else:
			print "No paso"
	else:
		entidad = Entidades.objects.get(id=int(pk))
		form=RegistrarEntidadForm(model_to_dict(entidad))
	return render(request, 'inicio/entidad_edit.html', {'form': form})	

def eliminar_entidad(request):
	import json

	if not request.is_ajax():
		raise Http404

	pk = request.POST.get('pk')

	try:
		entidad = Entidades.objects.filter(id=pk).update(habilitado=False)
	except Exception, e:
		print "Error: ", e
		mensaje = {'mensaje': "Fallo la operación", 'error': True}
	else:
		mensaje = {'mensaje': "Operación exitosa", 'error': False}

	content = json.dumps(mensaje)
	http_response = HttpResponse(content, content_type="application/json")

	return http_response

#
#==================OPERACIONES DE ENTREGABLES========================
#

def entregables(request):
	entregables_list = Entregables.objects.filter(habilitado=True).order_by('-proyecto__fecha_inicio')

	paginator = Paginator(entregables_list, 9)
	page = request.GET.get('page', 1)

	try:
		entregables = paginator.page(page)
	except PageNotAnInteger:
		entregables = paginator.page(1)
	except EmptyPage:
		entregables = paginator.page(paginator.num_pages)

	return render(request, 'inicio/entregables.html', {'entregables':entregables}, context_instance=RequestContext(request))

class EntregableDetailView(DetailView):
	
	template_name = "inicio/entregable_detail.html"
	model = Entregables

	def get_object(self):
		object = super(EntregableDetailView, self).get_object()
		return object

def crear_entregable(request):
	if request.method=="POST":
		form = RegistrarEntregableForm(request.POST)
		if form.is_valid():
			entregable = Entregables.objects.create(
													proyecto 	= form.cleaned_data['proyecto'],
													responsable = form.cleaned_data['responsable'],
													total 		= form.cleaned_data['total'],
													)

			mensaje = "El entregable ha sido creado exitosamente"
			return HttpResponseRedirect('/administracion/entregables/')
		else:
			print "No paso"
	else:
		form=RegistrarEntregableForm()
	return render(request, 'inicio/entregable_create.html', {'form': form})

def editar_entregable(request, pk):
	if request.method=="POST":
		form = RegistrarEntregableForm(request.POST)
		if form.is_valid():
			try:
				Entregables.objects.filter(id=int(pk)).update(
															proyecto 	= form.cleaned_data['proyecto'],
															responsable = form.cleaned_data['responsable'],
															total 		= form.cleaned_data['total'],
															)

				return HttpResponseRedirect('/administracion/entregables/')
			except Exception, e:				
				print "Error: ", e
				mensaje = "El entregable no pudo ser actualizado"
		else:
			print "No paso"
	else:
		entregable = Entregables.objects.get(id=int(pk))
		form=RegistrarEntregableForm(model_to_dict(entregable))
	return render(request, 'inicio/entregable_edit.html', {'form': form})	

def eliminar_entregable(request):
	import json

	if not request.is_ajax():
		raise Http404

	pk = request.POST.get('pk')

	try:
		entregable = Entregables.objects.filter(id=pk).update(habilitado=False)
	except Exception, e:
		print "Error: ", e
		mensaje = {'mensaje': "Fallo la operación", 'error': True}
	else:
		mensaje = {'mensaje': "Operación exitosa", 'error': False}

	content = json.dumps(mensaje)
	http_response = HttpResponse(content, content_type="application/json")

	return http_response