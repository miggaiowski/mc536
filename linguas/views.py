from django.shortcuts import render_to_response
from linguas.models import *

def ultimos_documentos(request):
    ult_doc = Documento.objects.all().order_by('-data_submissao')[:5]
    return render_to_response('linguas/home_doc_list.html', 
                              {'documento_list': ult_doc})

def documentos_keywords(request, key):
    keyword = Keyword.objects.filter(texto=key)[0]
    docs = keyword.documento_set.all()
    return render_to_response('linguas/documento_list.html', 
                              {'documento_list': docs})    
