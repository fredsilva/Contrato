from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^Contratos/', include('Contratos.foo.urls')), 
    url(r'^$', 'contrato.views.home', name='home'),    
    url(r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contratos/', 'contrato.views.contratos', name='contratos'),
    url(r'^usuarios/', 'contrato.views.usuarios', name='usuarios'),
    url(r'^pagamentos/', 'contrato.views.pagamentos', name='pagamentos'),
    url(r'^relatorios/', 'contrato.views.relatorios', name='relatorios'),
    url(r'^unidadesgestoras/', 'contrato.views.unidadesgestoras', name='unidadesgestoras'),
    url(r'^unidadessolicitante/', 'contrato.views.unidadessolicitante', name='unidadessolicitante'),
)
