import unittest
from datetime import datetime
from modelos.clinica import Clinica
from modelos.médico import Medico
from modelos.clase_paciente import Paciente
from modelos.especialidad import Especialidad

class TestClinica(unittest.TestCase):
    def setUp(self):
        self.clinica = Clinica("Clínica San Martín")
        self.medico = Medico("Dr. Juan Pérez", "MP123")
        self.paciente = Paciente("Ana García", "12345678")
        self.fecha = datetime(2025, 6, 15, 14, 30)

    def test_crear_clinica(self):
        self.assertEqual(self.clinica.nombre, "Clínica San Martín")
        self.assertEqual(len(self.clinica.medicos), 0)
        self.assertEqual(len(self.clinica.pacientes), 0)
        self.assertEqual(len(self.clinica.turnos), 0)
        self.assertEqual(len(self.clinica.historias_clinicas), 0)

    def test_agregar_medico(self):
        self.clinica.agregar_medico(self.medico)
        self.assertIn(self.medico, self.clinica.medicos)
        with self.assertRaises(ValueError):
            self.clinica.agregar_medico(self.medico)  # Duplicado
        with self.assertRaises(TypeError):
            self.clinica.agregar_medico("no es médico")

    def test_agregar_paciente(self):
        self.clinica.agregar_paciente(self.paciente)
        self.assertIn(self.paciente, self.clinica.pacientes)
        self.assertIn(self.paciente.dni, self.clinica.historias_clinicas)
        with self.assertRaises(ValueError):
            self.clinica.agregar_paciente(self.paciente)  # Duplicado
        with self.assertRaises(TypeError):
            self.clinica.agregar_paciente("no es paciente")

    def test_programar_turno(self):
        # Primero registramos médico y paciente
        self.clinica.agregar_medico(self.medico)
        self.clinica.agregar_paciente(self.paciente)
        
        turno = self.clinica.programar_turno(self.paciente, self.medico, self.fecha)
        self.assertIn(turno, self.clinica.turnos)
        self.assertEqual(turno.paciente, self.paciente)
        self.assertEqual(turno.medico, self.medico)
        self.assertEqual(turno.fecha, self.fecha)
        
        # Verificar que no se puede programar otro turno en el mismo horario
        with self.assertRaises(ValueError):
            self.clinica.programar_turno(self.paciente, self.medico, self.fecha)

    def test_buscar_turnos_medico(self):
        self.clinica.agregar_medico(self.medico)
        self.clinica.agregar_paciente(self.paciente)
        turno = self.clinica.programar_turno(self.paciente, self.medico, self.fecha)
        
        turnos = self.clinica.buscar_turnos_medico(self.medico)
        self.assertEqual(len(turnos), 1)
        self.assertEqual(turnos[0], turno)
        
        # Buscar por fecha específica
        turnos_fecha = self.clinica.buscar_turnos_medico(self.medico, self.fecha)
        self.assertEqual(len(turnos_fecha), 1)
        
        # Buscar en fecha sin turnos
        otra_fecha = datetime(2025, 6, 16, 14, 30)
        turnos_vacios = self.clinica.buscar_turnos_medico(self.medico, otra_fecha)
        self.assertEqual(len(turnos_vacios), 0)

    def test_obtener_historia_clinica(self):
        self.clinica.agregar_paciente(self.paciente)
        historia = self.clinica.obtener_historia_clinica(self.paciente)
        self.assertIsNotNone(historia)
        self.assertEqual(historia.paciente, self.paciente)

if __name__ == '__main__':
    unittest.main()