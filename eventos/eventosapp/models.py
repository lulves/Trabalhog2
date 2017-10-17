from django.db import models
from django.contrib.auth.models import User


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    idade = models.IntegerField(max_length=100)
    usuario = models.ForeignKey(User, null=True, blank=False)

    def __str__(self):
        return self.nome


class Evento (models.Model):

    nome = models.CharField(max_length=150)
    dataEHoraDeInicio = models.DateField(blank=True, null=True)
    dataEHoraFim = models.DateField(blank=True, null=True)
    cidade=models.CharField(null= True, blank=False)
    uf = models.CharField(null= True, blank=False)
    endereco =models.CharField(null= True, blank=False)
    def __str__(self):
        return self.nome

class Ticket (models.Model):

    nome = models.CharField(max_length=150)
    descricao = models.CharField(max_length=450)
    valor = models.IntegerField()
    evento = models.ForeignKey(Evento, null=True, blank=False)

    def __str__(self):
        return self.nome

class Inscricao (models.Model):
    evento = models.ForeignKey(Evento, null=True, blank=False)
    pessoa = models.ForeignKey(Pessoa, null=True, blank=False)
    ticket = models.ForeignKey(Ticket, null=True, blank=False)
    validacao = models.BooleanField("Validação")
    def __str__(self):
        return self.evento

# Create your models here.
