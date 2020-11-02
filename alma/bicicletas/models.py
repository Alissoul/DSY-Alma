from django.db import models

# Create your models here.
class formulario (models.Model):
    id_form     = models.AutoField(db_column='id_form', primary_key=True)
    nombres     = models.CharField(max_length=50, blank=True, null=True)
    apellidos   = models.CharField(max_length=50, blank=True, null=True)
    email       = models.CharField(max_length=50, blank=True, null=True)
    telefono    = models.CharField(max_length=9, unique=True)
    direccion   = models.CharField(max_length=100, blank=True, null=True)
    comentario  = models.CharField(max_length=200, blank=True, null=True)

class usuario (models.Model):
    id_usuario          = models.AutoField(db_column='id_usuario', primary_key=True)
    fecha_nacimiento    = models.DateField(blank=True, null = True)
    rut                 = models.CharField(max_length=19, unique=True)
    nombre              = models.CharField(max_length=20, blank=True, null=True)
    apellidos           = models.CharField(max_length=20, blank=True, null=True)
    genero              = models.CharField(max_length=10, blank=True, null=True)
    activo              = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.rut+"," + self.nombre +"," + self.apellidos + ","\
               +str(self.fecha_nacimiento) + ","\
               +self.genero

    class Meta:
        ordering = ["rut"]
