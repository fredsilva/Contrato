# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db import IntegrityError
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
    mensagem = None
    erro = False
    if request.method == "POST":
        form = FormCargo(request.POST, request.FILES)
        if form.is_valid():
            mensagem = "Cargo cadastrado com sucesso!"
            dados = form.cleaned_data
            cargo = Cargo(nome = dados['nome'])
            cargos = Cargo.objects.all()
            try:
                cargo.save()            
                form = FormCargo()
                return render_to_response("cargos.html",{'mensagem':mensagem, 'erro':erro, 'cargos': cargos, 'form':form}, context_instance = RequestContext(request))
            except IntegrityError, e:                
                erro = True
                e.message = "Registro já existe no banco de dados"
                mensagem = e.message
                form = FormCargo()
                return render_to_response("cargos.html",{'mensagem':mensagem, 'erro':erro, 'cargos': cargos, 'form':form}, context_instance = RequestContext(request))  
    else:   
        form = FormCargo()
        cargos = Cargo.objects.all()
    return render_to_response("cargos.html",{'titulo': titulo, 'nomePagina': nomePagina, 'form': form, 'cargos': cargos}, context_instance = RequestContext(request))
