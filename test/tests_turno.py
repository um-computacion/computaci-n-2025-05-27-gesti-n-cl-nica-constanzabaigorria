import unittest
from datetime import datetime
from modelos.clase_paciente import Paciente
from modelos.médico import Medico
from modelos.especialidad import Especialidad   
from modelos.turno import Turno

class TestTurno(unittest.TestCase):
    def setUp(self):
        self.paciente = Paciente("Ana García", "23456789")
        self.medico = Medico("Dr. Pedro Martínez", "MP789")
        self.fecha = datetime(2025, 6, 15, 14, 30)  # 15/06/2025 14:30
        self.turno = Turno(
            paciente=self.paciente,
            medico=self.medico,
            fecha=self.fecha
        )

    def test_creacion_turno(self):
        self.assertEqual(self.turno.paciente, self.paciente)
        self.assertEqual(self.turno.medico, self.medico)
        self.assertEqual(self.turno.fecha, self.fecha)
        self.assertEqual(self.turno.duracion, 30)
        self.assertEqual(self.turno.estado, "Programado")

    def test_cancelar_turno(self):
        self.turno.cancelar()
        self.assertEqual(self.turno.estado, "Cancelado")

    def test_completar_turno(self):
        self.turno.completar()
        self.assertEqual(self.turno.estado, "Completado")

    def test_reprogramar_turno(self):
        nueva_fecha = datetime(2025, 6, 16, 15, 0)
        self.turno.reprogramar(nueva_fecha)
        self.assertEqual(self.turno.fecha, nueva_fecha)
        self.assertEqual(self.turno.estado, "Programado")

    def test_str_representacion(self):
        resultado = str(self.turno)
        self.assertIn("Ana García", resultado)
        self.assertIn("Dr. Pedro Martínez", resultado)
        self.assertIn("15/06/2025 14:30", resultado)
        self.assertIn("Estado: Programado", resultado)

    def test_validacion_tipos(self):
        with self.assertRaises(TypeError):
            Turno("no es paciente", self.medico, self.fecha)
        with self.assertRaises(TypeError):
            Turno(self.paciente, "no es medico", self.fecha)
        with self.assertRaises(TypeError):
            Turno(self.paciente, self.medico, "no es datetime")
        with self.assertRaises(TypeError):
            self.turno.reprogramar("no es datetime")

if __name__ == '__main__':
    unittest.main()