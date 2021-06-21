from django import forms
from django.db import models
from .models import Candidato, Contatos,  Habilidades, Objetivos, Formacao
# Create your models here.

class CandidatoForms(forms.ModelForm):
    class Meta:
        model = Candidato
        exclude = ['user']
        labels = {'name':'Nome', 'foto_candidato':'Foto', 'resumo': 'Resumo', 'perfil': 'Perfil'}

class ContatoForms(forms.ModelForm):
    class Meta:
        model = Contatos
        exclude = ['candidato']
        labels = {'site':'Site', 'email':'Email', 'celular': 'Celular', 'linkedin': 'Linkedin'}

class HabilidadeForms(forms.ModelForm):
    class Meta:
        model = Habilidades
        exclude = ['candidato']
        labels = {'descricaohab':'Habilidades'}

class ObjetivosForms(forms.ModelForm):
    class Meta:
        model = Objetivos
        exclude = ['candidato']
        labels = {'descricaoobj':'Objetivos'}

class FormacaoForms(forms.ModelForm):
    class Meta:
        model = Formacao
        exclude = ['candidato']
        labels = {'descricaofor':'Formações'}


    #name = forms.CharField(label='Nome', max_length=200)
    #foto_candidato = forms.ImageField(label='Foto',)
    #celular = forms.CharField(label='Celular',widget=forms.NumberInput)
    #email = forms.EmailField(label='Email', max_length=150)
    #linkedin = forms.CharField(label='Linkedin',max_length=200)
    #site = forms.CharField(label='Site',max_length=200)
    #perfil = forms.CharField(label='Perfil',widget=forms.Textarea)
    #habilidades = forms.CharField(label='Habilidades',max_length=200)
    #objetivos = forms.CharField(label='Objetivos',max_length=200)
    #resumo = forms.CharField(label='Resumo',widget=forms.Textarea)
    #formacao = forms.CharField(label='Formações',max_length=200)
