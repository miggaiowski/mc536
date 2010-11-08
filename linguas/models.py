from django.db import models

class Programa(models.Model):
    nome = models.CharField(max_length=200)
    organizacao = models.ForeignKey(Usuario)

class Autor(models.Model):
    nome = models.CharField(max_length=200)
    nacionalidade = models.CharField(max_length=50)
    data_nasc = models.DateTimeField('Data de Nascimento')

class RedeTrabalho(models.Model):
    nome = models.CharField(max_length=200)

class Programa_do_Autor(models.Model):
    autor = models.ForeignKey(Autor)
    programa = models.ForeignKey(Programa)

class Idioma(models.Model):
    nome = models.CharField(max_length=200)
    pag_wiki = models.URLField(max_length=200)

