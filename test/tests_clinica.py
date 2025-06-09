import sys
import os
import unittest
from datetime import datetime

# Add project root to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

import unittest
from datetime import datetime
from modelos.clase_paciente import Paciente
from modelos.médico import Medico
from modelos.especialidad import Especialidad
from modelos.clinica import Clinica
from modelos.excepciones import (
    PacienteNoEncontradoException,
    MedicoNoEncontradoException,
    MedicoNoDisponibleException,
    TurnoOcupadoException,
    RecetaInvalidaException
)

class TestClinica(unittest.TestCase):
    def setUp(self):
        self.clinica = Clinica()
        self.paciente = Paciente("Juan Perez", "12345678", "01/01/1990")
        self.medico = Medico("Dra. House", "M123")
        self.especialidad = Especialidad("Clínica", ["martes"])
        self.medico.agregar_especialidad(self.especialidad)
        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)

    def test_registro_paciente_exitoso(self):
        pacientes = self.clinica.obtener_pacientes()
        self.assertEqual(len(pacientes), 1)
        self.assertEqual(pacientes[0].obtener_dni(), "12345678")

    def test_registro_paciente_duplicado(self):
        with self.assertRaises(ValueError):
            self.clinica.agregar_paciente(Paciente("Juan Perez", "12345678", "01/01/1990"))

    def test_registro_medico_exitoso(self):
        medicos = self.clinica.obtener_medicos()
        self.assertEqual(len(medicos), 1)
        self.assertEqual(medicos[0].obtener_matricula(), "M123")

    def test_registro_medico_duplicado(self):
        with self.assertRaises(ValueError):
            self.clinica.agregar_medico(Medico("Dra. House", "M123"))

    def test_agendar_turno_exitoso(self):
        fecha_hora = datetime(2025, 6, 10, 10, 0)  # martes
        self.clinica.agendar_turno("12345678", "M123", "Clínica", fecha_hora)
        turnos = self.clinica.obtener_turnos()
        self.assertEqual(len(turnos), 1)
        self.assertEqual(turnos[0].obtener_medico().obtener_matricula(), "M123")

    def test_agendar_turno_paciente_no_existe(self):
        fecha_hora = datetime(2025, 6, 10, 10, 0)
        with self.assertRaises(PacienteNoEncontradoException):
            self.clinica.agendar_turno("99999999", "M123", "Clínica", fecha_hora)

    def test_agendar_turno_medico_no_existe(self):
        fecha_hora = datetime(2025, 6, 10, 10, 0)
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.agendar_turno("12345678", "M999", "Clínica", fecha_hora)

    def test_agendar_turno_especialidad_no_valida(self):
        fecha_hora = datetime(2025, 6, 10, 10, 0)
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.agendar_turno("12345678", "M123", "Pediatría", fecha_hora)

    def test_agendar_turno_dia_no_valido(self):
        fecha_hora = datetime(2025, 6, 11, 10, 0)  # miércoles, no atiende
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.agendar_turno("12345678", "M123", "Clínica", fecha_hora)

    def test_agendar_turno_duplicado(self):
        fecha_hora = datetime(2025, 6, 10, 10, 0)
        self.clinica.agendar_turno("12345678", "M123", "Clínica", fecha_hora)
        with self.assertRaises(TurnoOcupadoException):
            self.clinica.agendar_turno("12345678", "M123", "Clínica", fecha_hora)

    def test_emitir_receta_exitosa(self):
        self.clinica.emitir_receta("12345678", "M123", ["Paracetamol"])
        historia = self.clinica.obtener_historia_clinica("12345678")
        recetas = historia.obtener_recetas()
        self.assertEqual(len(recetas), 1)
        self.assertIn("Paracetamol", str(recetas[0]))

    def test_emitir_receta_paciente_no_existe(self):
        with self.assertRaises(PacienteNoEncontradoException):
            self.clinica.emitir_receta("99999999", "M123", ["Paracetamol"])

    def test_emitir_receta_medico_no_existe(self):
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.emitir_receta("12345678", "M999", ["Paracetamol"])

    def test_emitir_receta_sin_medicamentos(self):
        with self.assertRaises(RecetaInvalidaException):
            self.clinica.emitir_receta("12345678", "M123", [])

    def test_obtener_historia_clinica(self):
        historia = self.clinica.obtener_historia_clinica("12345678")
        self.assertIn("Juan Perez", str(historia))

if __name__ == "__main__":
    unittest.main()