from django.contrib import admin
from .models import Candidato, Contatos, Habilidades, Objetivos, Formacao
# Register your models here.

@admin.register(Candidato)
class candidatoAdmin(admin.ModelAdmin):
    list_display = ['id','name']

admin.site.register(Habilidades)

admin.site.register(Objetivos)

admin.site.register(Contatos)

admin.site.register(Formacao)