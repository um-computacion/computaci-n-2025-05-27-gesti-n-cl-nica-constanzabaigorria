import unittest
from modelos.especialidad import Especialidad

class TestEspecialidad(unittest.TestCase):

    def test_crear_especialidad(self):
        especialidad = Especialidad("Pediatria", ["lunes", "miercoles", "viernes"])

        self.assertEqual(especialidad.obtener_especialidad(), "Pediatria")
        self.assertTrue(especialidad.verificar_dia("lunes"))
        self.assertTrue(especialidad.verificar_dia("MIERCOLES"))
        self.assertFalse(especialidad.verificar_dia("martes"))

    def test_dias_invalidos(self):
        with self.assertRaises(ValueError):
            Especialidad("Cardiologia", ["lunez", "martes"]) # lunes escrito con error 

    def test_dia_vacio(self):
        with self.assertRaises(ValueError):
            Especialidad("Cardiologia", [])
    
    def test_especialidad_vacia(self):
        with self.assertRaises(ValueError):
            Especialidad("", ["lunes", "martes"]) 

    def test_dia_case_insensitive(self):
        especialidad = Especialidad("Neurologia", ["martes", "jueves"])

        self.assertTrue(especialidad.verificar_dia("martes"))
        self.assertTrue(especialidad.verificar_dia("MARTES"))
        self.assertTrue(especialidad.verificar_dia("Martes"))
        self.assertTrue(especialidad.verificar_dia("mArTeS"))

    def test_especialidad_acentos(self):
        especialidad = Especialidad("Pediatría", ["lunes", "miércoles", "viernes"])
        
        self.assertEqual(especialidad.obtener_especialidad(), "Pediatría")
        self.assertTrue(especialidad.verificar_dia("miércoles"))
        self.assertIn("Pediatría", str(especialidad))

    def test_normalizacion_dias_entrada(self):
        especialidad1 = Especialidad("Neurología", ["miércoles", "sábado"])
        especialidad2 = Especialidad("Oftalmología", ["miercoles", "sabado"])  # Sin tildes
        
        self.assertTrue(especialidad1.verificar_dia("miércoles"))
        self.assertTrue(especialidad2.verificar_dia("miércoles"))
        self.assertTrue(especialidad1.verificar_dia("miercoles"))
        self.assertTrue(especialidad2.verificar_dia("miercoles"))

    def test_str(self):
        especialidad = Especialidad("Traumatologia", ["lunes", "miercoles"])
        resultado = str(especialidad)

        self.assertIn("Traumatologia", resultado)
        self.assertIn("lunes", resultado)
        self.assertIn("miercoles", resultado)

if __name__ == "__main__":
    unittest.main()