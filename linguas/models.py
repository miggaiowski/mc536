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

class Local_do_Idioma(models.Model):
    idioma = models.ForeignKey(Idioma)
    pais = models.CharField(max_length=200)
    regiao = models.CharField(max_length=200)

class Keyword(models.Model):
    texto = models.CharField(max_length=50, unique=True)
    idioma = models.ForeignKey(Idioma)

class Natureza(models.Model):
    tipo = models.CharField(max_length=200)

class Usuario(models.Model):
    login = models.CharField(max_length=30)
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    senha = models.CharField(max_length=20)
    tipo = models.CharField(max_length=30)
    pais_sede = models.CharField(max_length=200)


    
