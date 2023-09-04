from django.shortcuts import render

def inicio(request):
    return render(request, 'inicio.html')
    
def contato(request):
    return render(request, 'contato.html')

# Create your views here.
