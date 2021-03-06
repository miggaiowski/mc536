from django.db import models
from django import forms

class Programa(models.Model):
    nome = models.CharField(max_length=200)
    organizacao = models.ForeignKey('Usuario')

    def __unicode__(self):
        return self.nome

class Autor(models.Model):
    nome = models.CharField(max_length=200)
    nacionalidade = models.CharField(max_length=50)
    data_nasc = models.DateTimeField('Data de Nascimento')

    def __unicode__(self):
        return self.nome

class RedeTrabalho(models.Model):
    nome = models.CharField(max_length=200, primary_key=True)

    def __unicode__(self):
        return self.nome

class Programa_do_Autor(models.Model):
    autor = models.ForeignKey(Autor)
    programa = models.ForeignKey(Programa)

class Idioma(models.Model):
    nome = models.CharField(max_length=200)
    pag_wiki = models.URLField(max_length=200)

    def __unicode__(self):
        return self.nome

class Local_do_Idioma(models.Model):
    idioma = models.ForeignKey(Idioma)
    pais = models.CharField(max_length=200)
    regiao = models.CharField(max_length=200)

class Keyword(models.Model):
    texto = models.CharField(max_length=50, primary_key=True)
    idioma = models.ForeignKey(Idioma)

    def __unicode__(self):
        return self.texto

class Natureza(models.Model):
    tipo = models.CharField(max_length=200, primary_key=True)

    def __unicode__(self):
        return self.tipo


class Usuario(models.Model):
    login = models.CharField(max_length=30, primary_key=True)
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    senha = models.CharField(max_length=20)
    tipo = models.CharField(max_length=30)
    pais_sede = models.CharField(max_length=200)

    def __unicode__(self):
        return self.login

class RedeUsuario(models.Model):
    login = models.ForeignKey(Usuario)
    nome = models.ForeignKey('RedeTrabalho')


class Documento(models.Model):
    arquivo = models.FileField(upload_to='/Users/miguelgaiowski/src/mc536/trabalho/static')
    formato = models.CharField(max_length=5)
    titulo = models.CharField(max_length=200)
    data_criacao = models.DateTimeField()
    data_submissao = models.DateTimeField()
    num_vizualizacoes = models.IntegerField()
    autor = models.ForeignKey(Autor)
    idioma = models.ForeignKey(Idioma)
    submetido_por = models.ForeignKey(Usuario)
    maquina_submissao = models.IPAddressField()
    programa = models.ForeignKey(Programa)
    natureza = models.ForeignKey(Natureza)
    resposta = models.ManyToManyField('Documento', through='Responde', related_name='res')
    ligado = models.ManyToManyField('Documento', through='Liga', related_name='ligacao')
    keywords = models.ManyToManyField('Keyword', through='DocumentoKeyword')

    def __unicode__(self):
        return self.titulo

class Descricao(models.Model):
    idioma = models.ForeignKey(Idioma)
    texto = models.CharField(max_length=1000)

class DocumentoKeyword(models.Model):
    documento = models.ForeignKey(Documento)
    texto = models.ForeignKey(Keyword)

class Favorito(models.Model):
    documento = models.ForeignKey(Documento)
    login = models.ForeignKey(Usuario)

class Responde(models.Model):
    sobre = models.ForeignKey(Documento, related_name='+')
    resposta = models.ForeignKey(Documento, related_name='+')

class Liga(models.Model):
    login = models.ForeignKey(Usuario)
    did_a = models.ForeignKey(Documento, related_name='+')
    did_liga = models.ForeignKey(Documento, related_name='+')

class Debate(models.Model):
    comentario_1 = models.ForeignKey('Comentario', related_name='+')
    comentario_2 = models.ForeignKey('Comentario', related_name='+')

class Comentario(models.Model):
    usuario = models.ForeignKey(Usuario)
    documento = models.ForeignKey('Documento')
    idioma = models.ForeignKey(Idioma)
    data = models.DateTimeField()
    texto = models.CharField(max_length=1000)
    resposta = models.ManyToManyField('Comentario', through='Debate', related_name='res')

    def __unicode__(self):
        return self.texto

class ComentarioForm(forms.Form):
    usuario = forms.CharField(max_length=30)
    texto = forms.CharField(max_length=1000)
    
