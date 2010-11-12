from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from linguas.models import Keyword

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^trabalho/', include('trabalho.foo.urls')),
    (r'^keyword/$', ListView.as_view(
            model=Keyword, 
            context_object_name='keyword_list', 
            template_name='linguas/keyword_list.html')),
    (r'^keyword/(?P<pk>\w+)/$', DetailView.as_view(
            model=Keyword, 
            template_name='linguas/keyword_detail.html')),
       

    # (r'^keywords/$', linguas.views.keywords),
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
