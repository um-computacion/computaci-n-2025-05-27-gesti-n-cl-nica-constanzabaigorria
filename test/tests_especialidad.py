import sys
import os
import unittest
from datetime import datetime

# Add project root to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

import unittest
from modelos.especialidad import Especialidad

class TestEspecialidad(unittest.TestCase):
    def test_creacion_exitosa(self):
        esp = Especialidad("Pediatría", ["lunes", "miércoles", "viernes"])
        self.assertEqual(esp.obtener_especialidad(), "Pediatría")
        self.assertIn("lunes", str(esp))
        self.assertIn("miércoles", str(esp))
        self.assertIn("viernes", str(esp))

    def test_dias_invalidos(self):
        with self.assertRaises(ValueError):
            Especialidad("Cardiología", ["luness"])  # Día inválido

    def test_verificar_dia(self):
        esp = Especialidad("Clínica", ["martes", "jueves"])
        self.assertTrue(esp.verificar_dia("martes"))
        self.assertTrue(esp.verificar_dia("MARTES"))  # No sensible a mayúsculas
        self.assertFalse(esp.verificar_dia("domingo"))

    def test_str(self):
        esp = Especialidad("Dermatología", ["lunes", "viernes"])
        s = str(esp)
        self.assertIn("Dermatología", s)
        self.assertIn("lunes", s)
        self.assertIn("viernes", s)

if __name__ == "__main__":
    unittest.main()