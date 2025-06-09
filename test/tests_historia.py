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
from src.modelos.receta import Receta
from src.modelos.historia_clinica import HistoriaClinica
from src.modelos.turno import Turno

class TestHistoriaClinica(unittest.TestCase):
    def setUp(self):
        self.paciente = Paciente("Juan Perez", "12345678", "01/01/1990")
        self.medico = Medico("Dra. House", "M123")
        self.historia = HistoriaClinica(self.paciente)
        self.fecha_hora = datetime(2025, 6, 10, 10, 0)

    def test_agregar_turno(self):
        turno = Turno(self.paciente, self.medico, self.fecha_hora, "Clínica")
        self.historia.agregar_turno(turno)
        turnos = self.historia.obtener_turnos()
        self.assertEqual(len(turnos), 1)
        self.assertIs(turnos[0], turno)

    def test_agregar_receta(self):
        receta = Receta(self.paciente, self.medico, ["Paracetamol"])
        self.historia.agregar_receta(receta)
        recetas = self.historia.obtener_recetas()
        self.assertEqual(len(recetas), 1)
        self.assertIs(recetas[0], receta)

    def test_obtener_turnos_y_recetas_copias(self):
        turno = Turno(self.paciente, self.medico, self.fecha_hora, "Clínica")
        receta = Receta(self.paciente, self.medico, ["Ibuprofeno"])
        self.historia.agregar_turno(turno)
        self.historia.agregar_receta(receta)
        turnos = self.historia.obtener_turnos()
        recetas = self.historia.obtener_recetas()
        turnos.append("otro")
        recetas.append("otro")
        self.assertEqual(len(self.historia.obtener_turnos()), 1)
        self.assertEqual(len(self.historia.obtener_recetas()), 1)

    def test_str(self):
        turno = Turno(self.paciente, self.medico, self.fecha_hora, "Clínica")
        receta = Receta(self.paciente, self.medico, ["Ibuprofeno"])
        self.historia.agregar_turno(turno)
        self.historia.agregar_receta(receta)
        s = str(self.historia)
        self.assertIn("Juan Perez", s)
        self.assertIn("Clínica", s)
        self.assertIn("Ibuprofeno", s)

if __name__ == "__main__":
    unittest.main()