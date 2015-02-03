#-*- coding:utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
import datetime
import os
# Create your models here.

def get_upload_path(instance, filename):
    return os.path.join(filename)

#PERSONAL DE DESARROLLO

#esta clase se encarga de representar en el sistema los atributos de la clase PERSONAL 
class Personal(models.Model):
	SEXO_OPCIONES = (('H', 'Hombre'), ('M', 'Mujer'), )
	TIPO_PAGO = (('S', 'Semanal'), ('Q', 'Quincenal'), ('M', 'Mensual'),)
	TIPO_PLAZA = (('B', 'Becario'), ('H','Honorarios'), ('E', 'Efectivo'), ('O', 'Otro'))

	rfc = models.CharField(max_length=45)
	credencial_elector = models.FileField(upload_to = get_upload_path, blank=True)
	nombre = models.CharField(max_length=45)
	apellido_paterno = models.CharField(max_length=45)
	apellido_materno = models.CharField(max_length=45)
	siglas_nombre = models.CharField(max_length=45, null=True)
	genero = models.CharField(max_length=1, choices=SEXO_OPCIONES)
	direccion = models.CharField(max_length=45)
	telefono = models.CharField(max_length=45)
	no_seguro = models.CharField(max_length=45)
	fecha_ingreso = models.DateField(default=datetime.datetime.now())
	puesto = models.CharField(max_length=45)
	turno = models.CharField(max_length=45)
	tipo_plaza = models.CharField(max_length=45, choices = TIPO_PLAZA)
	#En caso de que se seleccione Otro, abrir campo de especificacion
	tipo_pago = models.CharField(max_length=1, choices=TIPO_PAGO)
	monto = models.IntegerField()	
	numero_oficio_contrato = models.CharField(max_length=45) # Dreprecated
	dias_trabajo_al_mes = models.IntegerField()
	
	fecha_vencimiento_contrato = models.DateField()
	fecha_baja = models.DateField()
	motivo_baja = models.CharField(max_length=45)

	responsable = models.CharField(max_length=45) #REsponsable de pagar... incluir en detalle pago....

	def __unicode__(self):
		return "%s-%s" % (self.rfc, self.nombre)


# Aqui se modelan los atributos multivaluados de la clase PAGOEMPLEADO (de uno a muchos)
class DetallePagoEmpleado(models.Model):
	personal = models.ForeignKey(Personal)
	archivo_documento_de_pago = models.FileField(upload_to = get_upload_path, blank=True)	

# Aqui se modelan los atributos multivaluados de la clase DOCUMENTORESPONSIVA (de uno a muchos)

class DetalleDocumentoResponsiva(models.Model):
	personal = models.ForeignKey(Personal)
	archivo_documento_responsiva = models.FileField(upload_to = get_upload_path, blank=True)

#esta clase se encarga de representar en el sistema los atributos de la clase PROYECTOS

class Proyectos(models.Model):
	#
	#Relacion uno a muchas Empresas(49, 46) 
	#
	CHOICE = (('A', 'Activo'), ('H', 'Historico'))
	nombre = models.CharField(max_length=150, null=False)
	siglas = models.CharField(max_length=45)
	responsable = models.ManyToManyField(Personal)
	fecha_inicio = models.DateField(default=datetime.datetime.now())
	status = models.CharField(max_length=45, choices = CHOICE) #dreprecated
	avance = models.CharField(max_length=45)
	# fecha_fin
	# comentario
	# fecha_cambio #Una fecha de reprogramacion

	def __unicode__(self):
		return "%s-%s" % (self.nombre, self.siglas)
#esta clase se encarga de representar en el sistema los atributos de la clase Anexostecnicos


class AnexosTecnicos(models.Model):
	#Responsable distinto del proyeto
	#
	#
	TIPOS = (('D', 'Dependencia'), ('E', 'Empresa'), ('U', 'Universidad'))

	numero_oficio = models.IntegerField(blank=False)	
	proyecto = models.ForeignKey(Proyectos)

	tipo = models.CharField(max_length=1, choices=TIPOS) # Dreprecated
	nombre = models.CharField(max_length=45)
	siglas = models.CharField(max_length=45)
	porcentaje = models.IntegerField() # Deprecated
	fecha_creacion=models.DateField(default=datetime.datetime.now())
	archivo=models.FileField(upload_to = get_upload_path, blank=True)
	
	#status = En proceso/en revision/aceptado
	def __unicode__(self):
		return "%s-%s" % (self.numero_oficio, self.nombre)

#esta clase se encarga de representar en el sistema los atributos de la clase CONVENIOS

class Convenios (models.Model):
	# lo mismo que Contratos,  
	numero=models.CharField(max_length=45)
	proyecto=models.ForeignKey(Proyectos)

	numero_universidad=models.CharField(max_length=45)
	siglas_universidad=models.CharField(max_length=45)

	archivo=models.FileField(upload_to=get_upload_path, blank=True)
	fecha_creacion=models.DateField(default=datetime.datetime.now())

	encargado = models.ForeignKey(Personal)

	def __unicode__(self):
		return "%s-%s" % (self.rfc, self.nombre)


#esta clase se encarga de representar en el sistema los atributos de la clase CONTRATOS

class Contratos(models.Model):
	numero_oficio =models.CharField(max_length=45)
	proyecto=models.ForeignKey(Proyectos)
	fecha_creacion=models.DateField(default=datetime.datetime.now())
	encargado=models.ForeignKey(Personal) #Responsable
	cliente=models.CharField(max_length=45, help_text = "Nombre de la dependencia") # Deprecated
	archivo=models.FileField(upload_to=get_upload_path, blank=True) # Deprecated

	#Contrato Dependencia universidad
	#Convenio Universidad Empresa 46/49
	def __unicode__(self):
		return "%s-%s" % (self.numero_oficio, self.proyecto)

#esta clase se encarga de representar en el sistema los atributos de la clase ENTREGABLES

class Entregables(models.Model):
	contrato = models.ForeignKey(Contratos)
	proyecto = models.ForeignKey(Proyectos)
	responsable = models.ForeignKey(Personal)

	#nombre = models.CharField(max_length=45)
	#fecha_creacion=models.DateField(default=datetime.datetime.now())
	nombre = models.CharField(max_length=45)
	fecha_creacion=models.DateField(default=datetime.datetime.now())
	archivo = models.FileField(upload_to=get_upload_path, blank=True)
	
	# Total de entregables ---UNO/N----

	# @property
	# def total(self):
	# 	return len(Detalle_entregable.objects.filter(entregable=self))

# Aqui se modelan los atributos multivaluados de la clase ENTREGABLES (de uno a muchos)

class DetallesEntregables(models.Model):
	entregable = models.ForeignKey(Entregables)
	responsable = models.ForeignKey(Personal)
	numero = models.IntegerField()
	nombre =models.CharField(max_length=45)
	siglas = models.CharField(max_length=45)
	fecha_creacion=models.DateField(default=datetime.datetime.now())
	archivo=models.FileField(upload_to=get_upload_path, blank=True)

#esta clase se encarga de representar en el sistema los atributos de la clase EMPRESAS

class Empresas(models.Model):
	nombre=models.CharField(max_length=45)

#esta clase se encarga de representar en el sistema los atributos de la clase FACTURAS

class Facturas(models.Model):
	#TIPOS = (('D', 'Dependencia'), ('E', 'Empresa'), ('U', 'Universidad'))
	TIPOS = (('E2', 'Empresa 46%'), ('E1', 'Empresa 49%'), ('U', 'Universidad'))
	
	contrato = models.ForeignKey(Contratos)
	responsable = models.ForeignKey(Personal)

	tipo = models.CharField(max_length=1, choices=TIPOS)
	nombre=models.CharField(max_length=45)
	siglas=models.CharField(max_length=45)

	numero_factura=models.IntegerField(unique=True)
	fecha_factura = models.DateField(default=datetime.datetime.now())
	folio_venta=models.CharField(max_length=45, blank=True, help_text="Folio de la factura")

	rfc=models.CharField(max_length=45, help_text="RFC persona fisica/moral")
	direccion=models.CharField(max_length=45, help_text=u"dirección persona fisica/moral")

	subtotal=models.IntegerField()
	iva=models.IntegerField()
	total_con_numero = models.IntegerField()
	total_con_letra = models.CharField(max_length=45)
	pagada=models.BooleanField(default=False)
	archivo=models.FileField(upload_to=get_upload_path )
	# archivo_xml=models.FileField(upload_to=get_upload_path ) #Archivo en XML
	# archivo_fisico=models.FileField(upload_to=get_upload_path ) #Archivo fisico de la factura

	def __unicode__(self):
		return "%s-%s" % (self.nombre, self.folio_venta)

#Aqui se modelan los atributos multivaluados de la clase FACTURA (de uno a muchos)

class DetallesFacturas(models.Model):
	factura = models.ForeignKey(Facturas) 
	descripcion = models.CharField(max_length=45)
	cantidad = models.IntegerField()

#esta clase se encarga de representar en el sistema los atributos de la clase PROPUESTAS

class Propuestas(models.Model):
	TIPOS = (('E1', 'Empresa 46%'), ('E2', 'Empresa 49%'), ('U1', 'Universidad'))

	numero_oficio = models.CharField(max_length=45)
	proyecto = models.ForeignKey(Proyectos)

	responsable = models.ForeignKey(Personal)

	# Deprecated. viene directamente del proyecto
	nombre_dependencia=models.CharField(max_length=45)
	siglas_dependencia=models.CharField(max_length=45)

	tipo = models.CharField(max_length=2, choices=TIPOS)
	nombre =models.CharField(max_length=45)
	siglas=models.CharField(max_length=45)

	fecha_creacion=models.DateField(default=datetime.datetime.now())

#esta clase se encarga de representar en el sistema los atributos de la claseDOCUMENTOS GENERALES

class DocumentosGenerales(models.Model):
	TIPOS = (('D', 'Dependencia'), ('E', 'Empresa'), ('U', 'Universidad'))
	proyecto=models.ForeignKey(Proyectos)
	responsable=models.ForeignKey(Personal)
	clave =models.CharField(max_length=45)
	tipo = models.CharField(max_length=1, choices=TIPOS)
	nombre =models.CharField(max_length=45)
	siglas=models.CharField(max_length=45)
	fecha_creacion=models.DateField(default=datetime.datetime.now())

#Aqui se modelan los atributos multivaluados de la clase Documentos Generales (de uno a muchos)

class DetallesDocumentosGenerales(models.Model):
	documentos_generales =models.ForeignKey(DocumentosGenerales)
	responsable=models.ForeignKey(Personal)
	numero =models.IntegerField()
	nombre =models.CharField(max_length=45)
	siglas =models.CharField(max_length=45)
	archivo=models.CharField(max_length=45)
	fecha_creacion=models.DateField(default=datetime.datetime.now())
