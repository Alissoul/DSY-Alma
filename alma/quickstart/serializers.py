from django.contrib.auth.models import User, Group
from bicicletas.models import producto
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class ProductosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = producto
        fields = ['id_producto', 'codigo', 'nombre', 'descripcion', 'precio',
                 'tipo', 'foto', 'activo']

