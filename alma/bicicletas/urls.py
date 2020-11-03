from django.conf.urls import url
from django.urls import path, include

from . import views
urlpatterns = [
    path('index', views.index, name='index'),
    path('bicicletas', views.bicicletas, name='bicicletas'),
    path('accesorios', views.accesorios, name='accesorios'),
    path('piezas', views.piezas, name='piezas'),
    path('contacto', views.contacto, name='contacto'),
    path('formulario_agregar', views.formulario_agregar, name='formulario_agregar'),
    path('datos_enviados', views.datos_enviados, name='datos_enviados'),
    path('formulario_producto', views.formulario_producto, name='formulario_producto'),
    path('guardado', views.guardado, name='guardado'),
    path('agregar_producto', views.agregar_producto, name='agregar_producto'),
    path('buscar_para_editar', views.buscar_para_editar, name='buscar_para_editar'),
    path('actualizar_producto', views.actualizar_producto, name='actualizar_producto'),
    path('editar_producto', views.editar_producto, name='editar_producto'),
    path('listar', views.listar, name='listar'),
    path('mostrar_producto', views.mostrar_producto, name='mostrar_producto'),

]