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

#Productos

def agregar_producto(request):
    print("Estoy en agregar producto...")
    if request.method == 'POST':

       mi_codigo = request.POST['codigo']
       mi_nombre = request.POST['nombre']
       mi_descripcion= request.POST['descripcion']
       mi_precio=request.POST['precio']
       mi_tipo=request.POST['tipo']
       mi_foto = request.FILES['foto']

       if mi_codigo != "":
           try:
               prod = producto()

               prod.codigo       = mi_codigo
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

def editar_producto(request):
    print("Hola estoy en actualizar producto...")
    context={}
    return render (request,'bicicletas/editar_producto.html', context)

def buscar_para_editar(request):
    print("Estamos en la vista buscar para editar")
    if request.method =='POST':
        mi_codigo= request.POST['codigo']

        if mi_codigo !="":
            try:
                prod = producto()
                prod = producto.objects.get(codigo=mi_codigo)
                if prod is not None:
                    print ("producto = ", prod)
                    context={'prod':prod}
                    return render(request,'bicicletas/formulario_editar.html',context)
                else:
                    return render(request,'bicicletas/error_202.html',{})
            except prod.DoesNotExist:
                return render(request,'bicicletas/error/error_202.html',{})
        else:
            return render(request,'bicicletas/error/error_201.html', {})
    else:
        return render(request, 'personas/error/error_203.html',{})


def actualizar_producto(request):
    print("Estoy en actualizar productos...")
    if request.method == 'POST':
        mi_id     = request.POST['id_producto']
        mi_codigo = request.POST['codigo']
        mi_nombre = request.POST['nombre']
        mi_descripcion= request.POST['descripcion']
        mi_precio=request.POST['precio']
        mi_tipo=request.POST['tipo']
        mi_foto = request.FILES['foto']

        if mi_codigo != "":
            try:
                prod = producto()

                prod.id_producto = mi_id
                prod.codigo = mi_codigo
                prod.nombre = mi_nombre
                prod.descripcion = mi_descripcion
                prod.precio = mi_precio
                prod.tipo = mi_tipo
                prod.foto = mi_foto
                prod.activo = 1

                prod.save()

                return render(request, 'bicicletas/guardado.html', {})

            except prod.DoesNotExist:
                return render(request, 'bicicletas/error/error_204.html', {})
        else:
            return render(request, 'bicicletas/error/error_201.html', {})
    else:
        return render(request, 'bicicletas/error/error_203.html', {})

def listar(request):
    print("ok, estamos en la vista listar")
    context={}
    return render(request, 'bicicletas/listar.html', context)

def mostrar_producto(request):
    print("ok, estamos en la vista mostrar producto")
    lista = producto.objects.all()
    context = {'listado':lista}
    return render (request, 'bicicletas/listar_producto.html', context)
    return render (request, 'bicicletas/listar_producto.html', context)

def eliminar(request):
    print("ok, estamos en la vista eliminar")
    context={}
    return render(request, 'bicicletas/eliminar.html', context)

def eliminar_por_codigo(request):

    print("ok, estamos en la vista eliminar por codigo")
    if request.method =='POST':
        mi_codigo=request.POST['codigo']

        if mi_codigo!="":
            try:
                prod = producto()
                prod = producto.objects.get(codigo=mi_codigo)
                if prod is not None:
                    print("producto= ", prod)
                    prod.delete()
                    context={}

                    return render (request,'bicicletas/index.html',context)
                else:
                    return render(request,'bicicletas/error/error_202.html',{})
            except prod.DoesNotExist:
                return render(request,'bicicletas/error/error_202.html',{})
        else:
            return render (request,'bicicletas/error/error_201.html',{})
    else:
        return render(request, 'bicicletas/error/error_203.html',{})

