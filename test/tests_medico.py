import sys
import os
import unittest
from datetime import datetime

# Add project root to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

import unittest
from modelos.médico import Medico
from modelos.especialidad import Especialidad

class TestMedico(unittest.TestCase):
    def test_creacion_exitosa(self):
        medico = Medico("Dr. House", "M123")
        self.assertEqual(medico.obtener_matricula(), "M123")
        self.assertIn("Dr. House", str(medico))

    def test_agregar_especialidad(self):
        medico = Medico("Dra. Grey", "M456")
        esp = Especialidad("Cardiología", ["lunes", "miércoles"])
        medico.agregar_especialidad(esp)
        self.assertIn("Cardiología", str(medico))
        self.assertEqual(medico.obtener_especialidad_para_dia("lunes"), "Cardiología")
        self.assertIsNone(medico.obtener_especialidad_para_dia("viernes"))

    def test_prevenir_especialidad_duplicada(self):
        medico = Medico("Dr. Strange", "M789")
        esp1 = Especialidad("Neurología", ["martes"])
        esp2 = Especialidad("Neurología", ["jueves"])
        medico.agregar_especialidad(esp1)
        with self.assertRaises(ValueError):
            medico.agregar_especialidad(esp2)  # No debe permitir duplicados

    def test_dias_invalidos(self):
        with self.assertRaises(ValueError):
            Especialidad("Pediatría", ["funday"])  # Día inválido

    def test_str(self):
        medico = Medico("Dra. Who", "M999")
        esp = Especialidad("Clínica", ["lunes", "viernes"])
        medico.agregar_especialidad(esp)
        s = str(medico)
        self.assertIn("Dra. Who", s)
        self.assertIn("Clínica", s)
        self.assertIn("lunes", s)
        self.assertIn("viernes", s)

if __name__ == "__main__":
    unittest.main()