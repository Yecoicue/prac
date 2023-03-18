from django.shortcuts import render

# Create your views here.
def inicio(request):
    context={}
    return render(request, 'inicio.html',context)




# Create your views here.
def list_clientes(request):
    clientes=['cliente 1','cliente 2','cliente 3','cliente 4']
    context={'clave':clientes}
    return render(request, 'list_clientes.html',context)
