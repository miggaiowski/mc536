from django.shortcuts import render_to_response
from django.template import RequestContext
from linguas.models import *

def ultimos_documentos(request):
    ult_doc = Documento.objects.all().order_by('-data_submissao')[:5]
    return render_to_response('linguas/home_doc_list.html', 
                              {'documento_list': ult_doc},
                              context_instance=RequestContext(request))

def documentos_keywords(request, key):
    keyword = Keyword.objects.filter(texto=key)[0]
    docs = keyword.documento_set.all()
    return render_to_response('linguas/documento_list.html', 
                              {'documento_list': docs})    

def documentos_programas(request, pk):
    prog = Programa.objects.get(pk=pk)
    docs = prog.documento_set.all()
    return render_to_response('linguas/documento_list.html', 
                              {'documento_list': docs})    

def busca(request):
    res = {}
    if request.POST['s']:
        res['docs'] = Documento.objects.filter(titulo__icontains=request.POST['s'])
        res['users'] = Usuario.objects.filter(nome__icontains=request.POST['s'])
        res['progs'] = Programa.objects.filter(nome__icontains=request.POST['s'])
    return render_to_response('linguas/resultado_busca.html', 
                              {'results': res}, 
                              context_instance=RequestContext(request))    
        
