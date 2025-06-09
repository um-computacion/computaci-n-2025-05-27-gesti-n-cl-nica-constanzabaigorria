import sys
import os
import unittest
from datetime import datetime
# Add project root to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

import unittest
from src.modelos.clase_paciente import Paciente

class TestPaciente(unittest.TestCase):
    def test_creacion_exitosa(self):
        paciente = Paciente("Juan Perez", "12345678", "01/01/1990")
        self.assertEqual(paciente.obtener_dni(), "12345678")
        self.assertIn("Juan Perez", str(paciente))
        self.assertIn("12345678", str(paciente))

    def test_dni_unico(self):
        paciente1 = Paciente("Ana Gomez", "11111111", "02/02/1980")
        paciente2 = Paciente("Ana Gomez", "11111111", "02/02/1980")
        # Dos instancias pueden crearse, pero el sistema debe evitar duplicados al registrar (esto se testea en Clinica)
        self.assertEqual(paciente1.obtener_dni(), paciente2.obtener_dni())

    def test_datos_invalidos(self):
        with self.assertRaises(TypeError):
            Paciente()  # Sin argumentos
        with self.assertRaises(ValueError):
            Paciente("", "22222222", "03/03/1970")  # Nombre vacío
        with self.assertRaises(ValueError):
            Paciente("Pedro", "", "03/03/1970")  # DNI vacío
        with self.assertRaises(ValueError):
            Paciente("Pedro", "22222222", "")  # Fecha de nacimiento vacía

    def test_str(self):
        paciente = Paciente("Maria Lopez", "33333333", "04/04/2000")
        s = str(paciente)
        self.assertIn("Maria Lopez", s)
        self.assertIn("33333333", s)
        self.assertIn("04/04/2000", s)

if __name__ == "__main__":
    unittest.main()