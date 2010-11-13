from django.shortcuts import render_to_response
from linguas.models import *

def ultimos_documentos(request):
    ult_doc = Documento.objects.all().order_by('-data_submissao')[:5]
    return render_to_response('linguas/documento_list.html', {'documento_list': ult_doc})

