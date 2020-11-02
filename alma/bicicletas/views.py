from django.shortcuts import render
from .models import formulario

# Create your views here.

def index(request):
    print("Hola estoy en index...")
    context={}
    return render (request,'bicicletas/index.html', context)

def bicicletas(request):
    print("Hola estoy en bicicletas...")
    context={}
    return render (request,'bicicletas/bicicletas.html', context)

def accesorios(request):
    print("Hola estoy en accesorios...")
    context={}
    return render (request,'bicicletas/accesorios.html', context)


def piezas(request):
    print("Hola estoy en piezas...")
    context={}
    return render (request,'bicicletas/piezas.html', context)

def datos_enviados(request):
    print("Hola estoy en datos_enviados...")
    context = {}
    return render(request, 'bicicletas/datos_enviados.html', context)

def contacto(request):
    print("Hola estoy en contacto...")
    context={}
    return render (request,'bicicletas/contacto.html', context)

def formulario_agregar(request):
    print("hola  estoy en agregar formulario...")
    if request.method == 'POST':
       mi_nombres = request.POST['nombres']
       mi_apellidos= request.POST['apellidos']
       mi_email=request.POST['email']
       mi_telefono=request.POST['telefono']
       mi_direccion =request.POST['direccion']
       mi_comentario=request.POST['comentario']

       if mi_comentario != "":
           try:
               form = formulario()

               form.nombres     = mi_nombres
               form.apellidos   = mi_apellidos
               form.email       = mi_email
               form.telefono    = mi_telefono
               form.direccion   = mi_direccion
               form.comentario  = mi_comentario

               form.save()

               return render(request, 'bicicletas/datos_enviados.html',{})

           except form.DoesNotExist:
               return render(request, 'bicicletas/error/error_204.html', {})
       else:
           return render(request, 'bicicletas/error/error_201.html', {})
    else:
        return render(request, 'bicicletas/error/error_203.html', {})


