# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):    
    nomePagina = "Home"
    titulo  = "Sefaz - Sistema de Gerenciamento de Contratos"    
    return render_to_response("home.html",{'titulo': titulo, 'nomePagina': nomePagina}, context_instance = RequestContext(request))

def contratos(request):
    nomePagina = "Contratos"
    titulo  = "Contratos"    
    return render_to_response("home.html",{'titulo': titulo, 'nomePagina': nomePagina}, context_instance = RequestContext(request))

def usuarios(request):
    nomePagina = "Usuários"
    titulo  = "Usuários"    
    return render_to_response("usuarios.html",{'titulo': titulo, 'nomePagina': nomePagina}, context_instance = RequestContext(request))

def pagamentos(request):
    nomePagina = "Pagamentos"
    titulo  = "Pagamentos"    
    return render_to_response("home.html",{'titulo': titulo, 'nomePagina': nomePagina}, context_instance = RequestContext(request))

def relatorios(request):
    nomePagina = "Relatórios"
    titulo  = "Relatórios"    
    return render_to_response("home.html",{'titulo': titulo, 'nomePagina': nomePagina}, context_instance = RequestContext(request))

def unidadesgestoras(request):
    nomePagina = "Unidades Gestoras"
    titulo  = "Unidades Gestoras"    
    return render_to_response("home.html",{'titulo': titulo, 'nomePagina': nomePagina}, context_instance = RequestContext(request))

def unidadessolicitante(request):
    nomePagina = "Unidades Solicitante"
    titulo  = "Unidades Solicitante"    
    return render_to_response("home.html",{'titulo': titulo, 'nomePagina': nomePagina}, context_instance = RequestContext(request))

def cargos(request):
    nomePagina = "Cargos"
    titulo  = "Cargos"    
    
    return render_to_response("cargos.html",{'titulo': titulo, 'nomePagina': nomePagina}, context_instance = RequestContext(request))