from django.shortcuts import render

# Create your views here.

def index(request):
    print("Hola estoy en index...")
    context={}
    return render (request,'bicicletas/index.html', context)

