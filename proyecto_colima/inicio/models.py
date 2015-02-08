#-*- coding:utf-8 -*-

from django.contrib.auth.models import User
from django.conf import settings
from django.db import models

from inicio.helpers import get_upload_path

import datetime

#esta clase se encarga de representar en el sistema los atributos de la clase EMPRESAS
class Empresas(models.Model):
	nombre=models.CharField(max_length=45)

#esta clase se encarga de representar en el sistema los atributos de la clase PERSONAL 
class Personal(models.Model):
	REPOSITORIO 	= settings.PERSONAL

	TIPO_PAGO 		= (('S', 'Semanal'), ('Q', 'Quincenal'), ('M', 'Mensual'),)
	TIPO_PLAZA 		= (('B', 'Becario'), ('H','Honorarios'), ('E', 'Efectivo'), ('O', 'Otro'))
	SEXO_OPCIONES 	= (('M', 'Masculino'), ('F', 'Femenino'), )

	rfc 						= models.CharField(max_length=45)
	credencial_elector 			= models.FileField(upload_to = get_upload_path, blank=True)
	nombre 						= models.CharField(max_length=45)
	apellido_paterno 			= models.CharField(max_length=45)
	apellido_materno 			= models.CharField(max_length=45)
	siglas_nombre 				= models.CharField(max_length=45, null=True)
	genero 						= models.CharField(max_length=2, choices=SEXO_OPCIONES)
	direccion 					= models.CharField(max_length=60)
	telefono 					= models.IntegerField(max_length=20)
	no_seguro 					= models.IntegerField(max_length=45)
	fecha_ingreso 				= models.DateField(default=datetime.datetime.now().date())
	puesto 						= models.CharField(max_length=45)
	turno 						= models.CharField(max_length=45)
	tipo_plaza 					= models.CharField(max_length=3, choices = TIPO_PLAZA)
	especificacion 				= models.CharField(max_length=45, null=True, blank=True)
	#En caso de que se seleccione Otro, abrir campo de especificacion
	tipo_pago 					= models.CharField(max_length=1, choices=TIPO_PAGO)
	monto 						= models.IntegerField()	
	#numero_oficio_contrato = models.CharField(max_length=45) # Dreprecated
	dias_trabajo_al_mes 		= models.IntegerField()
	
	fecha_vencimiento_contrato 	= models.DateField()
	fecha_baja 					= models.DateField()
	motivo_baja 				= models.CharField(max_length=45)
	responsable 				= models.CharField(max_length=45) #REsponsable de pagar... incluir en detalle pago....

	def __unicode__(self):
		return "%s-%s" % (self.rfc, self.nombre)


# Aqui se modelan los atributos multivaluados de la clase PAGOEMPLEADO (de uno a muchos)
class DetallePagoEmpleado(models.Model):
	REPOSITORIO 				= settings.DETALLES_PAGO_EMPLEADO

	personal 					= models.ForeignKey(Personal)
	responsable 				= models.CharField(max_length=45)
	archivo_documento_de_pago 	= models.FileField(upload_to = get_upload_path, blank=True)	

# Aqui se modelan los atributos multivaluados de la clase DOCUMENTORESPONSIVA (de uno a muchos)
class DetalleDocumentoResponsiva(models.Model):
	REPOSITORIO						= settings.DETALLES_DOCUMENTO_RESPONSIVA

	personal 						= models.ForeignKey(Personal)
	archivo_documento_responsiva 	= models.FileField(upload_to = get_upload_path, blank=True)

#esta clase se encarga de representar en el sistema los atributos de la clase PROYECTOS
class Proyectos(models.Model):

	STATUS = (('A', 'Activo'), ('H', 'Historico'))

	nombre 			= models.CharField(max_length=150)
	siglas 			= models.CharField(max_length=45)
	#responsable 	= models.ManyToManyField(Personal)
	#empresa 		= models.ManyToManyField(Empresas)
	fecha_inicio 	= models.DateField(default=datetime.datetime.now().date())
	#fecha_fin 		= models.DateField(default=datetime.datetime.now().date())
	status 			= models.CharField(max_length=3, choices = STATUS) #dreprecated
	avance 			= models.CharField(max_length=45)
	#comentario 		= models.CharField(max_length=500)
	#fecha_cambio 	= models.DateField()

	#
	# Relacion uno a muchas Empresas(49, 46) 
	#
	# fecha_fin
	# comentario
	# fecha_cambio #Una fecha de reprogramacion

	def __unicode__(self):
		return "%s-%s" % (self.nombre, self.siglas)

#esta clase se encarga de representar en el sistema los atributos de la clase Anexostecnicos
class AnexosTecnicos(models.Model):
	REPOSITORIO 	= settings.ANEXOS_TECNICOS

	TIPOS 			= (('D1', 'Dependencia'), ('E', 'Empresa'), ('U1', 'Universidad'))
	STATUS 			= (('EP','En proceso'),('ER', 'En revision'), ('A', 'Aceptado'))

	numero_oficio 	= models.IntegerField(blank=False)	
	proyecto 		= models.ForeignKey(Proyectos)
	tipo 			= models.CharField(max_length=1, choices=TIPOS) # Dreprecated
	nombre 			= models.CharField(max_length=45)
	siglas 			= models.CharField(max_length=45)
	porcentaje 		= models.IntegerField() # Deprecated
	status 			= models.CharField(max_length=3, choices=STATUS)
	fecha_creacion  = models.DateField(default=datetime.datetime.now().date())
	archivo         = models.FileField(upload_to=get_upload_path, blank=True)
	
	#Responsable distinto del proyeto
	#
	#		
	#status = En proceso/en revision/aceptado
	
	def __unicode__(self):
		return "%s-%s" % (self.numero_oficio, self.nombre)

#esta clase se encarga de representar en el sistema los atributos de la clase CONVENIOS
class Convenios (models.Model):
	REPOSITORIO 		= settings.CONVENIOS
	# lo mismo que Contratos,  
	numero 				= models.CharField(max_length=45)
	proyecto 			= models.ForeignKey(Proyectos)

	numero_universidad 	= models.CharField(max_length=45)
	siglas_universidad	= models.CharField(max_length=45)

	archivo 			= models.FileField(upload_to=get_upload_path, blank=True)
	fecha_creacion 		= models.DateField(default=datetime.datetime.now().date())

	encargado = models.ForeignKey(Personal)

	def __unicode__(self):
		return "%s-%s" % (self.rfc, self.nombre)


#esta clase se encarga de representar en el sistema los atributos de la clase CONTRATOS
class Contratos(models.Model):
	REPOSITORIO 	= settings.CONTRATOS

	numero_oficio 	= models.CharField(max_length=45)
	proyecto        = models.ForeignKey(Proyectos)
	fecha_creacion  = models.DateField(default=datetime.datetime.now().date())
	encargado 		= models.ForeignKey(Personal) #Responsable
	cliente 		= models.CharField(max_length=45, help_text = "Nombre de la dependencia") # Deprecated
	archivo 		= models.FileField(upload_to=get_upload_path, blank=True) # Deprecated

	#Contrato Dependencia universidad
	#Convenio Universidad Empresa 46/49

	def __unicode__(self):
		return "%s-%s" % (self.numero_oficio, self.proyecto)

#esta clase se encarga de representar en el sistema los atributos de la clase ENTREGABLES

class Entregables(models.Model):
	REPOSITORIO 	= settings.ENTREGABLES

	contrato 		= models.ForeignKey(Contratos)
	proyecto 		= models.ForeignKey(Proyectos)
	responsable 	= models.ForeignKey(Personal)
	archivo 		= models.FileField(upload_to=get_upload_path, blank=True)

	# nombre = models.CharField(max_length=45)
	# fecha_creacion=models.DateField(default=datetime.datetime.now())
	# Total de entregables ---UNO/N----

# Aqui se modelan los atributos multivaluados de la clase ENTREGABLES (de uno a muchos)
class DetallesEntregables(models.Model):
	REPOSITORIO 	= settings.DETALLES_ENTREGABLES

	entregable 		= models.ForeignKey(Entregables)
	responsable 	= models.ForeignKey(Personal)
	numero 			= models.IntegerField()
	nombre 			= models.CharField(max_length=45)
	siglas 			= models.CharField(max_length=45)
	fecha_creacion 	= models.DateField(default=datetime.datetime.now())
	archivo 		= models.FileField(upload_to=get_upload_path, blank=True)

#esta clase se encarga de representar en el sistema los atributos de la clase FACTURAS
class Facturas(models.Model):
	REPOSITORIO 		= settings.FACTURAS

	TIPOS 				= (('E1', 'Empresa 46%'), ('E2', 'Empresa 49%'), ('U1', 'Universidad'))
	
	contrato 			= models.ForeignKey(Contratos)
	responsable 		= models.ForeignKey(Personal)

	tipo 				= models.CharField(max_length=1, choices=TIPOS)
	nombre 				= models.CharField(max_length=45)
	siglas 				= models.CharField(max_length=45)

	numero_factura 		= models.IntegerField(unique=True)
	fecha_factura 		= models.DateField(default=datetime.datetime.now())
	folio_venta 		= models.CharField(max_length=45, blank=True, help_text="Folio de la factura")

	rfc 				= models.CharField(max_length=45, help_text="RFC persona fisica/moral")
	direccion 			= models.CharField(max_length=45, help_text=u"dirección persona fisica/moral")

	subtotal 			= models.IntegerField()
	iva 				= models.IntegerField()
	total_con_numero 	= models.IntegerField()
	total_con_letra 	= models.CharField(max_length=45)
	pagada 				= models.BooleanField(default=False)
	archivo_xml 		= models.FileField(upload_to=get_upload_path, blank=True) #Archivo en XML
	archivo_fisico 		= models.FileField(upload_to=get_upload_path, blank=True) #Archivo fisico de la factura

	def __unicode__(self):
		return "%s-%s" % (self.nombre, self.folio_venta)

#Aqui se modelan los atributos multivaluados de la clase FACTURA (de uno a muchos)
class DetallesFacturas(models.Model):
	factura 		= models.ForeignKey(Facturas) 
	descripcion 	= models.CharField(max_length=200)
	cantidad 		= models.IntegerField()

#esta clase se encarga de representar en el sistema los atributos de la clase PROPUESTAS
class Propuestas(models.Model):
	TIPOS 			= (('E1', 'Empresa 46%'), ('E2', 'Empresa 49%'), ('U1', 'Universidad'))

	numero_oficio 	= models.CharField(max_length=45)
	proyecto 		= models.ForeignKey(Proyectos)
	responsable 	= models.ForeignKey(Personal)

	# Deprecated. viene directamente del proyecto
	# nombre_dependencia=models.CharField(max_length=45)
	# siglas_dependencia=models.CharField(max_length=45)

	tipo 			= models.CharField(max_length=3, choices=TIPOS)
	nombre 			= models.CharField(max_length=45)
	siglas 			= models.CharField(max_length=45)

	fecha_creacion 	= models.DateField(default=datetime.datetime.now().date())

#esta clase se encarga de representar en el sistema los atributos de la claseDOCUMENTOS GENERALES
class DocumentosGenerales(models.Model):
	TIPOS 			= (('D1', 'Dependencia'), ('E', 'Empresa'), ('U1', 'Universidad'))

	proyecto 		= models.ForeignKey(Proyectos)
	responsable 	= models.ForeignKey(Personal)
	clave 			= models.CharField(max_length=45)
	tipo 			= models.CharField(max_length=3, choices=TIPOS)
	nombre 			= models.CharField(max_length=45)
	siglas 			= models.CharField(max_length=45)
	fecha_creacion 	= models.DateField(default=datetime.datetime.now().date())

#Aqui se modelan los atributos multivaluados de la clase Documentos Generales (de uno a muchos)
class DetallesDocumentosGenerales(models.Model):
	REPOSITORIO 	= settings.DETALLE_DOCUMENTOS_GENERALES

	documentos_generales 	= models.ForeignKey(DocumentosGenerales)
	responsable 			= models.ForeignKey(Personal)
	numero 					= models.IntegerField()
	nombre 					= models.CharField(max_length=45)
	siglas 					= models.CharField(max_length=45)
	archivo 				= models.FileField(upload_to=get_upload_path, blank=True)
	fecha_creacion 			= models.DateField(default=datetime.datetime.now().date())