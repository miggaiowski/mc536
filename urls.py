from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from linguas.models import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Example:
    # (r'^trabalho/', include('trabalho.foo.urls')),
    
    (r'^keywords?/$', ListView.as_view(
            model=Keyword,
            context_object_name='keyword_list')),
    (r'^keywords?/(?P<pk>\w+)/$', DetailView.as_view(
            model=Keyword)),
    (r'^usuarios?/$', ListView.as_view(
            model=Usuario, 
            context_object_name='usuario_list')),
    (r'^usuarios?/(?P<pk>\w+)/$', DetailView.as_view(
            model=Usuario)),
    (r'^programas?/$', ListView.as_view(
            model=Programa, 
            context_object_name='programa_list')),
    (r'^programas?/(?P<pk>\w+)/$', DetailView.as_view(
            model=Programa)),
    (r'^documentos?/$', ListView.as_view(
            model=Documento, 
            context_object_name='documento_list')),
    (r'^documentos?/(?P<pk>\w+)/$', DetailView.as_view(
            model=Documento)),

    # (r'^keywords/$', linguas.views.keywords),
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)

