import unittest
from datetime import date
from modelos.receta import Receta
from modelos.clase_paciente import Paciente
from modelos.médico import Medico

class TestReceta(unittest.TestCase):

    def setUp(self):
        self.paciente = Paciente("Maria López", "12345678")
        self.medico = Medico("Dr. Juan Pérez", "MP1234")
        self.receta = Receta(
            paciente=self.paciente,
            medico=self.medico,
            medicamentos=["Paracetamol"]
        )

    def test_datos_iniciales(self):
        self.assertEqual(str(self.receta.paciente), "Maria López")
        self.assertEqual(str(self.receta.medico), "Dr. Juan Pérez")
        self.assertIn("Paracetamol", self.receta.medicamentos)
        self.assertEqual(self.receta.fecha, date.today())

    def test_agregar_medicamento(self):
        self.receta.agregar_medicamento("Ibuprofeno")
        self.assertIn("Ibuprofeno", self.receta.medicamentos)

    def test_str(self):
        resultado = str(self.receta)
        self.assertIn("Maria López", resultado)
        self.assertIn("Dr. Juan Pérez", resultado)
        self.assertIn("Paracetamol", resultado)

if __name__ == '__main__':
    unittest.main()
