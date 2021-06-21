from django.contrib.auth.models import User
from django.db import models
# Create your models here.

class Candidato(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    foto_candidato = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=True)
    perfil = models.TextField()
    resumo = models.TextField()

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'candidato'


class Habilidades(models.Model):
    descricaohab = models.CharField(max_length=200)
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)

class Objetivos(models.Model):
    descricaoobj = models.CharField(max_length=200)
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)

class Formacao(models.Model):
    descricaofor = models.CharField(max_length=200)
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)

class Contatos(models.Model):
    celular = models.BigIntegerField()
    email = models.EmailField()
    linkedin = models.CharField(max_length=80)
    site = models.CharField(max_length=80)
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)
