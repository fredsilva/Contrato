# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from contrato.forms import FormCargo
from contrato.models import Cargo

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
    if request.method == "POST":
        form = FormCargo(request.POST, request.FILES)
        if form.is_valid():
            dados = form.cleaned_data
            cargo = Cargo(nome = dados['nome'])
            cargo.save()            
            return render_to_response("sucesso.html",{}, context_instance = RequestContext(request))
    else:   
        form = FormCargo()
        cargos = Cargo.objects.all()
    return render_to_response("cargos.html",{'titulo': titulo, 'nomePagina': nomePagina, 'form': form, 'cargos': cargos}, context_instance = RequestContext(request))
