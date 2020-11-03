import unittest
from bicicletas.models import producto

class testproducto(unittest.TestCase):
    def test_crear_objeto(self):
        prod = producto.objects.create(codigo='24',
                                       nombre= 'Bicicleta ALMA',
                                       descripcion='Aro 26',
                                       precio='199000',
                                       tipo= 'Bicicleta',
                                       foto='',
                                       activo = 1)
        prod.save()
        self.assertTrue(prod, True)

    #class testproducto(unittest.TestCase):
        #def test_eliminar_objeto(self):
           # prod = producto.objects.get(codigo='19')
            #if prod is not None:
             #   print("producto= ", prod)
              #  prod.delete()
            #self.assertTrue(prod, True)


    def test_val_codigo(self):
        prod = producto.objects.get(codigo='1')
        self.assertEquals(prod.codigo, '1')

    def test_crear_demo(self):
        a = 1
        self.assertEqual(a, 1)