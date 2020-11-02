from django.shortcuts import render
from .models import formulario
from .models import usuario
from .models import producto

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

def formulario_producto(request):
    print("Hola estoy en formulario producto...")
    context={}
    return render (request,'bicicletas/formulario_producto.html', context)

def guardado(request):
    print("Hola estoy en guardado...")
    context = {}
    return render(request, 'bicicletas/guardado', context)

def agregar_producto(request):
    print("hola  estoy en agregar producto...")
    if request.method == 'POST':
       mi_nombre = request.POST['nombre']
       mi_descripcion= request.POST['descripcion']
       mi_precio=request.POST['precio']
       mi_tipo=request.POST['tipo']
       mi_foto = request.FILES['foto']

       if mi_descripcion != "":
           try:
               prod = producto()

               prod.nombre       = mi_nombre
               prod.descripcion  = mi_descripcion
               prod.precio       = mi_precio
               prod.tipo         = mi_tipo
               prod.foto         = mi_foto

               prod.save()

               return render(request, 'bicicletas/guardado.html',{})

           except prod.DoesNotExist:
               return render(request, 'bicicletas/error/error_204.html', {})
       else:
           return render(request, 'bicicletas/error/error_201.html', {})
    else:
        return render(request, 'bicicletas/error/error_203.html', {})



