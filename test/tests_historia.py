import unittest
from datetime import datetime
from modelos.clase_paciente import Paciente
from modelos.médico import Medico
from modelos.receta import Receta
from modelos.historia_clinica import HistoriaClinica

class TestHistoriaClinica(unittest.TestCase):
    def setUp(self):
        self.paciente = Paciente("Juan Pérez", "12345678")
        self.medico = Medico("Dra. Ana Silva", "MP456")
        self.historia = HistoriaClinica(self.paciente)
        self.fecha_consulta = datetime(2025, 6, 15, 14, 30)

    def test_crear_historia(self):
        self.assertEqual(self.historia.paciente, self.paciente)
        self.assertEqual(len(self.historia.consultas), 0)
        self.assertEqual(len(self.historia.recetas), 0)
        self.assertIsInstance(self.historia.fecha_creacion, datetime)

    def test_agregar_consulta(self):
        self.historia.agregar_consulta(
            fecha=self.fecha_consulta,
            motivo="Dolor de cabeza",
            diagnostico="Migraña",
            medico=self.medico
        )
        self.assertEqual(len(self.historia.consultas), 1)
        consulta = self.historia.consultas[0]
        self.assertEqual(consulta['fecha'], self.fecha_consulta)
        self.assertEqual(consulta['motivo'], "Dolor de cabeza")
        self.assertEqual(consulta['diagnostico'], "Migraña")
        self.assertEqual(consulta['medico'], self.medico)

    def test_agregar_receta(self):
        receta = Receta(self.paciente, self.medico, ["Paracetamol"])
        self.historia.agregar_receta(receta)
        self.assertEqual(len(self.historia.recetas), 1)
        self.assertEqual(self.historia.recetas[0], receta)

    def test_validaciones_consulta(self):
        with self.assertRaises(TypeError):
            self.historia.agregar_consulta("no fecha", "motivo", "diagnostico", self.medico)
        with self.assertRaises(TypeError):
            self.historia.agregar_consulta(self.fecha_consulta, "motivo", "diagnostico", "no medico")
        with self.assertRaises(ValueError):
            self.historia.agregar_consulta(self.fecha_consulta, "", "diagnostico", self.medico)
        with self.assertRaises(ValueError):
            self.historia.agregar_consulta(self.fecha_consulta, "motivo", "", self.medico)

    def test_validaciones_receta(self):
        otra_paciente = Paciente("María López", "87654321")
        receta_invalida = Receta(otra_paciente, self.medico, ["Paracetamol"])
        with self.assertRaises(ValueError):
            self.historia.agregar_receta(receta_invalida)
        with self.assertRaises(TypeError):
            self.historia.agregar_receta("no es receta")

    def test_buscar_consultas_por_fecha(self):
        self.historia.agregar_consulta(self.fecha_consulta, "Dolor", "Migraña", self.medico)
        consultas = self.historia.buscar_consultas_por_fecha(self.fecha_consulta)
        self.assertEqual(len(consultas), 1)
        self.assertEqual(consultas[0]['motivo'], "Dolor")

    def test_obtener_consultas_ordenadas(self):
        fecha1 = datetime(2025, 6, 15, 14, 30)
        fecha2 = datetime(2025, 6, 16, 15, 30)
        self.historia.agregar_consulta(fecha1, "Dolor", "Migraña", self.medico)
        self.historia.agregar_consulta(fecha2, "Control", "Normal", self.medico)
        consultas = self.historia.obtener_consultas()
        self.assertEqual(consultas[0]['fecha'], fecha2)  # La más reciente primero

if __name__ == '__main__':
    unittest.main()