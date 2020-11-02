from django.contrib import admin
from .models import formulario
from .models import usuario
from .models import producto

# Register your models here.
admin.site.register(formulario)
admin.site.register(usuario)
admin.site.register(producto)