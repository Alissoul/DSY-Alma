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

]