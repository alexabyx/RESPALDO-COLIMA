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