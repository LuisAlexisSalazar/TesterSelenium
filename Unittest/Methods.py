import unittest

# !3 posibles respuestas
# ?	OK: Exitosa
# ?	FAIL: Indica que la prueba no ha ocurrido de manera correcta
# ?	ERROR: Cuando no ha ocurrido correctamente pero tampoco ha sido una aserción


class metodos_unittest(unittest.TestCase):
    # !indica que el metodo se ejecutara a nivel de clase
    # *se ejecuta una sola vez en la clase de unit case mas no por cada metodo
    @classmethod
    def setUpClass(cls):
        print("Este metodo inicia cuando empieza la clase")

    # ?Metodo para definir ciertas condiciones antes de iniciar cada test
    # *Por cada test o metodo que se ejecuta se ejecuta el setUp antes
    def setUp(self):
        print("Yo me inicio en cada test case")

    def test_mensaje(self):
        print("Test del Metodo Mensaje")

    def test_llamada(self):
        print("Test del Metodo llamada")

    # *Por cada test o metodo al final se ejecuta tearDown
    def tearDown(self):
        print("Yo me ejecuto al final de cada Test")

    @classmethod
    def tearDown(cls):
        print("Este metodo ejecuta al final de la clase")

if __name__ == '__main__':
    unittest.main()
