from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from linguas.models import *
import datetime

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

def documentos_idiomas(request, idioma):
    idioma = Idioma.objects.get(pk=idioma)
    docs = idioma.documento_set.all()
    return render_to_response('linguas/documento_list.html', 
                              {'documento_list': docs})    

def documento_detail(request, pk):
    try:
        doc = Documento.objects.get(pk=pk)
    except Documento.DoesNotExist:
        raise Http404
    doc.num_vizualizacoes += 1
    doc.save()
    form = ComentarioForm()
    return render_to_response('linguas/documento_detail.html', 
                              {'documento': doc,
                               'form': form, },
                              context_instance=RequestContext(request))    

def busca(request):
    res = {}
    if request.POST['s']:
        res['docs'] = Documento.objects.filter(titulo__icontains=request.POST['s'])
        res['users'] = Usuario.objects.filter(nome__icontains=request.POST['s'])
        res['progs'] = Programa.objects.filter(nome__icontains=request.POST['s'])
    return render_to_response('linguas/resultado_busca.html', 
                              {'results': res}, 
                              context_instance=RequestContext(request))    

def comenta(request, pk):
    if request.method == 'POST': 
        form = ComentarioForm(request.POST)
        if form.is_valid():
            try:
                usuario = Usuario.objects.get(pk=form.cleaned_data['usuario'])
                documento = Documento.objects.get(pk=pk)
                idioma = Idioma.objects.all()[0]
                data = datetime.datetime.now()
                texto = form.cleaned_data['texto']
                c = Comentario(usuario=usuario, 
                               documento=documento, 
                               idioma=idioma, 
                               data=data, 
                               texto=texto)
                c.save()
                return HttpResponseRedirect('/documento/'+str(pk))
            except:
                pass
    return HttpResponseRedirect('/documento/'+str(pk))

