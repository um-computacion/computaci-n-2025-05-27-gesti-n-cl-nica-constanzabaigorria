import sys
import os
import unittest
from datetime import datetime
# Add project root to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

import unittest
from datetime import datetime
from src.modelos.clase_paciente import Paciente
from src.modelos.médico import Medico  
from src.modelos.turno import Turno

class TestTurno(unittest.TestCase):
    def setUp(self):
        self.paciente = Paciente("Juan Perez", "12345678", "01/01/1990")
        self.medico = Medico("Dra. House", "M123")
        self.fecha_hora = datetime(2025, 6, 10, 10, 0)

    def test_creacion_exitosa(self):
        turno = Turno(self.paciente, self.medico, self.fecha_hora, "Clínica")
        self.assertEqual(turno.obtener_medico(), self.medico)
        self.assertEqual(turno.obtener_fecha_hora(), self.fecha_hora)
        self.assertIn("Clínica", str(turno))
        self.assertIn("Juan Perez", str(turno))
        self.assertIn("Dra. House", str(turno))

    def test_str(self):
        turno = Turno(self.paciente, self.medico, self.fecha_hora, "Pediatría")
        s = str(turno)
        self.assertIn("Pediatría", s)
        self.assertIn("Juan Perez", s)
        self.assertIn("Dra. House", s)
        self.assertIn("2025", s)

    def test_datos_invalidos(self):
        with self.assertRaises(TypeError):
            Turno()  # Sin argumentos
        with self.assertRaises(ValueError):
            Turno(None, self.medico, self.fecha_hora, "Clínica")
        with self.assertRaises(ValueError):
            Turno(self.paciente, None, self.fecha_hora, "Clínica")
        with self.assertRaises(ValueError):
            Turno(self.paciente, self.medico, None, "Clínica")
        with self.assertRaises(ValueError):
            Turno(self.paciente, self.medico, self.fecha_hora, "")

if __name__ == "__main__":
    unittest.main()