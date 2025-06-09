import sys
import os
import unittest
from datetime import datetime
# Add project root to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

import unittest
from datetime import date
from src.modelos.receta import Receta
from src.modelos.clase_paciente import Paciente
from src.modelos.médico import Medico

class TestReceta(unittest.TestCase):
    def setUp(self):
        self.paciente = Paciente("Juan Perez", "12345678", "01/01/1990")
        self.medico = Medico("Dra. House", "M123")

    def test_creacion_exitosa(self):
        receta = Receta(self.paciente, self.medico, ["Paracetamol", "Ibuprofeno"])
        self.assertIn("Paracetamol", str(receta))
        self.assertIn("Ibuprofeno", str(receta))
        self.assertIn("Juan Perez", str(receta))
        self.assertIn("Dra. House", str(receta))
        self.assertIsInstance(receta.obtener_fecha(), datetime)

    def test_str(self):
        receta = Receta(self.paciente, self.medico, ["Amoxicilina"])
        s = str(receta)
        self.assertIn("Amoxicilina", s)
        self.assertIn("Juan Perez", s)
        self.assertIn("Dra. House", s)

    def test_datos_invalidos(self):
        with self.assertRaises(TypeError):
            Receta()  # Sin argumentos
        with self.assertRaises(ValueError):
            Receta(None, self.medico, ["Paracetamol"])
        with self.assertRaises(ValueError):
            Receta(self.paciente, None, ["Paracetamol"])
        with self.assertRaises(ValueError):
            Receta(self.paciente, self.medico, [])
        with self.assertRaises(ValueError):
            Receta(self.paciente, self.medico, None)

if __name__ == "__main__":
    unittest.main()
