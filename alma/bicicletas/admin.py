from django.contrib import admin
from .models import formulario
from .models import usuario

# Register your models here.
admin.site.register(formulario)
admin.site.register(usuario)