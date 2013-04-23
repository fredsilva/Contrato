# -*- encoding: utf-8 -*-
from django.db import models

class Cargo(models.Model):
    nome = models.CharField(max_length = 50, unique = True)

class Gestor(models.Model):
    nome  = models.CharField(max_length = 80)
    cargo = models.ForeignKey("Cargo")

class TipoContrato(models.Model):
    decricao = models.CharField(max_length = 50)
    
class Origem(models.Model):
    decricao = models.CharField(max_length = 50)

class UnidadeGestora(models.Model):
    nome   = models.CharField(max_length = 50)    
    
class UnidadeSolicitante(models.Model):
    nome   = models.CharField(max_length = 50)
    gestor = models.ForeignKey("Gestor")

class Interessado(models.Model):
    cpfCnpj     = models.CharField(max_length = 14)
    razaoSocial = models.CharField(max_length = 80)
    
class Notificacoes(models.Model):
    descricao    = models.TextField()
    ativa        = models.BooleanField()
    dataAtivacao = models.DateField()
    contrato     = models.ForeignKey("Contrato")
    
class Contrato(models.Model):
    numero              = models.IntegerField()
    ano                 = models.IntegerField()
    processo            = models.CharField(max_length = 16)
    modalidadeLicitacao = models.ForeignKey("ModalidadeLicitacao")
    objeto              = models.TextField()
    dataInicial         = models.DateField()
    dataFinal           = models.DateField()
    situacao            = models.CharField(max_length = 50)
    valorTotal          = models.DecimalField(max_digits=15, decimal_places=2)
    valorParcela        = models.DecimalField(max_digits=15, decimal_places=2)
    valorReajuste       = models.DecimalField(max_digits=15, decimal_places=2)
    tipoPagamento       = models.ForeignKey("TipoPagamento")
    avisoVigencia       = models.IntegerField()
    unidadeSolicitante  = models.ForeignKey("UnidadeSolicitante")
    tipoContrato        = models.ForeignKey("TipoContrato")
    origem              = models.ForeignKey("Origem")
    fiscal              = models.ForeignKey("Fiscal")        
    #arquivo             = models.FileField(upload_to=None[, height_field=None, width_field=None, max_length=100, **options])
        
class TermoAditivo(models.Model):
    descricao = models.CharField(max_length = 50)
    valor     = models.DecimalField(max_digits=15, decimal_places=2)
    inicio    = models.DateField()
    fim       = models.DateField()
    contrato  = models.ForeignKey("Contrato")

class UnidadeGestorasContrato(models.Model):
    contrato       = models.ForeignKey("Contrato")
    unidadeGestora = models.ForeignKey("UnidadeGestora")
    valor          = models.DecimalField(max_digits=15, decimal_places=2)    
    
class InteressadosContrato(models.Model):
    contrato    = models.ForeignKey("Contrato")
    interessado = models.ForeignKey("Interessado")
    percentual  = models.DecimalField(max_digits=3, decimal_places=2)

class ModalidadeLicitacao(models.Model):
    modalidade = models.CharField(max_length = 50)
    
class TipoPagamento(models.Model):
    tipo = models.CharField(max_length = 50)

class Fiscal(models.Model):
    nome = models.CharField(max_length = 80)
    matricula = models.IntegerField()
    cargo     = models.ForeignKey("Cargo")
    suplente = models.ForeignKey("FiscalSuplente")

class FiscalSuplente(models.Model):
    nome = models.CharField(max_length = 80)
    matricula = models.IntegerField()
    cargo     = models.ForeignKey("Cargo")    