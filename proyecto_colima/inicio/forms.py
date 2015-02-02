#! -*- coding:utf-8 -*-

from django import forms
from inicio.models import ( Proyectos,
							Facturas,
							AnexosTecnicos,
							Contratos,
							Convenios,
							Propuestas,
							Empresas,
							Entregables,
							Personal
							)


class AuthForm(forms.Form):
    username = forms.CharField(required=True, max_length = 10, label=u'Usuario', widget = forms.TextInput(attrs = {'id':'usernames'}))  
    password = forms.CharField(required=True,label=u'Contraseña',widget=forms.PasswordInput(attrs = {'id':'elpassword'}))

class RegistrarProyectoForm(forms.ModelForm):
	class Meta:
		model = Proyectos

class FacturasForm(forms.ModelForm):
	class Meta:
		model = Facturas

class AnexosTecnicosForm(forms.ModelForm):
	class Meta:
		model = AnexosTecnicos

class ContratosForm(forms.ModelForm):
	class Meta:
		model = Contratos

class ConveniosForm(forms.ModelForm):
	class Meta:
		model = Convenios
		
class PropuestasForm(forms.ModelForm):
	class Meta:
		model = Propuestas

class EmpresasForm(forms.ModelForm):
	class Meta:
		model = Empresas

class EntregablesForm(forms.ModelForm):
	class Meta:
		model = Entregables

class PersonalForm(forms.ModelForm):
	class Meta:
		model= Personal

class ConsultarAnexoTecnicoForm(forms.Form):
	numero_oficio = forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))	
	#proyecto = forms.ModelChoiceField(required=False, label='Proyecto', widget=forms.Select(attrs={'readonly':True}), queryset=AnexosTecnicos.objects.all())
	proyecto = forms.CharField(required=False, label='Proyecto', widget=forms.TextInput(attrs={'readonly':True}) )
#plan                 = forms.ModelChoiceField(required=True, label='Plan de Estudios', widget=forms.Select(), queryset=PlanEstudios.objects.all())
	tipo = forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))
	nombre = forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))
	siglas = forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))
	porcentaje = forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))
	fecha_creacion=forms.DateField(required=False, widget=forms.TextInput(attrs={'readonly':True}))
	archivo=forms.FileField(required=False, widget=forms.TextInput(attrs={'readonly':True}))

class ConsultarContratoForm(forms.Form):
	numero_oficio = forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))	
	proyecto = forms.CharField(required=False, label='Proyecto', widget=forms.TextInput(attrs={'readonly':True}) )
	fecha_creacion=forms.DateField(required=False, widget=forms.TextInput(attrs={'readonly':True}))
	encargado=forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}) )	
	cliente=forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))	
	archivo=forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))

class ConsultarEntregables(forms.Form):
	contratrato = forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))	
	proyecto = forms.CharField(required=False, label='Proyecto', widget=forms.TextInput(attrs={'readonly':True}) )
	responsable = forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))


class ConsultarPersonalForm(forms.Form):
	rfc = forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))	
	nombre = forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}) )
	tipo = forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))
	nombre = forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))
	apellido_paterno = forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))
	apellido_materno = forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))
	siglas_nombre = forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))
	genero = forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))
	direccion = forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))
	telefono = forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))
	no_seguro = forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))
	fecha_ingreso = forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))
	puesto = forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))
	turno = forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))
	tipo_plaza = forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))
	tipo_pago = forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))
	monto = forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))
	numero_oficio_contrato = forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))
	fecha_vencimiento_contrato = forms.DateField(required=False, widget=forms.TextInput(attrs={'readonly':True}))
	fecha_baja=forms.DateField(required=False, widget=forms.TextInput(attrs={'readonly':True}))
	motivo_baja=forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))
	responsable=forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))


class ConsultarProyectosForm(forms.Form):
	nombre = forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))	
	siglas = forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}) )
	responsable = forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))
	fecha_inicio = forms.DateField(required=False, widget=forms.TextInput(attrs={'readonly':True}))
	status=forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))
	avance=forms.FileField(required=False, widget=forms.TextInput(attrs={'readonly':True}))	

class ConsultarConveniosForm(forms.Form):
	numero = forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))	
	proyecto = forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}) )
	numero_universidad = forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))
	siglas_universidad = forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))
	fecha_creacion = forms.DateField(required=False, widget=forms.TextInput(attrs={'readonly':True}))
	archivo=forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))	
	#encargado = models.ForeignKey(Personal) = forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))


class ConsultarFacturasForm(forms.Form):
	contrato = forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}) )
	responsable = forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))
	tipo = forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))
	nombre = forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))
	siglas = forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))
	numero_factura = forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))
	fecha_factura = forms.DateField(required=False, widget=forms.TextInput(attrs={'readonly':True}))
	folio_venta = forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))
	rfc = forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))
	direccion = forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))
	subtotal = forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))
	iva = forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))
	total_con_numero = forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))
	total_con_letra = forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))
	pagada = forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))
	archivo = forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))

class ConsultarPropuestasForm(forms.Form):
	numero_oficio = forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))	
	proyecto = forms.CharField(required=False, label='Proyecto', widget=forms.TextInput(attrs={'readonly':True}) )
	responsable = forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))
	nombre_dependencia=models = forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))
	siglas_dependencia=forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))
	tipo=forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))	
	nombre=forms.DateField(required=False, widget=forms.TextInput(attrs={'readonly':True}))	
	siglas=forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))	
	fecha_creacion=forms.DateField(required=False, widget=forms.TextInput(attrs={'readonly':True}))	

class ConsultarDocumentosGeneralesForm(forms.Form):
	proyecto = forms.CharField(required=False, label='Proyecto', widget=forms.TextInput(attrs={'readonly':True}) )
	responsable = forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))
	clave=models = forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))
	tipo=forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))
	nombre=forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))	
	siglas=forms.CharField(required=False, widget=forms.TextInput(attrs={'readonly':True}))	
	fecha_creacion=forms.DateField(required=False, widget=forms.TextInput(attrs={'readonly':True}))	
