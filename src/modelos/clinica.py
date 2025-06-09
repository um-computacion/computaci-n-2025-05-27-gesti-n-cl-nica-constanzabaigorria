from src.modelos.historia_clinica import HistoriaClinica
from src.modelos.excepciones import (
    PacienteNoEncontradoException,
    MedicoNoDisponibleException,
    TurnoOcupadoException,
    RecetaInvalidaException,
)
from src.modelos.receta import Receta
from src.modelos.turno import Turno

class Clinica:
    def __init__(self):
        self.__pacientes__ = {}  # dni: Paciente
        self.__medicos__ = {}    # matricula: Medico
        self.__turnos__ = []     # list of Turno
        self.__historias_clinicas__ = {}  # dni: HistoriaClinica

    def agregar_paciente(self, paciente):
        dni = paciente.obtener_dni()
        if dni in self.__pacientes__:
            raise ValueError("Paciente ya registrado.")
        self.__pacientes__[dni] = paciente
        self.__historias_clinicas__[dni] = HistoriaClinica(paciente)

    def agregar_medico(self, medico):
        matricula = medico.obtener_matricula()
        if matricula in self.__medicos__:
            raise ValueError("Médico ya registrado.")
        self.__medicos__[matricula] = medico

    def obtener_pacientes(self):
        return list(self.__pacientes__.values())

    def obtener_medicos(self):
        return list(self.__medicos__.values())

    def obtener_medico_por_matricula(self, matricula):
        if matricula not in self.__medicos__:
            raise MedicoNoDisponibleException("Médico no encontrado.")
        return self.__medicos__[matricula]

    def agendar_turno(self, dni, matricula, especialidad, fecha_hora):
        self.validar_existencia_paciente(dni)
        self.validar_existencia_medico(matricula)
        self.validar_turno_no_duplicado(matricula, fecha_hora)
        medico = self.__medicos__[matricula]
        paciente = self.__pacientes__[dni]
        dia_semana = self.obtener_dia_semana_en_espanol(fecha_hora)
        self.validar_especialidad_en_dia(medico, especialidad, dia_semana)
        turno = Turno(paciente, medico, fecha_hora, especialidad)
        self.__turnos__.append(turno)
        self.__historias_clinicas__[dni].agregar_turno(turno)

    def obtener_turnos(self):
        return list(self.__turnos__)

    def emitir_receta(self, dni, matricula, medicamentos):
        self.validar_existencia_paciente(dni)
        self.validar_existencia_medico(matricula)
        if not medicamentos or not isinstance(medicamentos, list) or len(medicamentos) == 0:
            raise RecetaInvalidaException("Debe indicar al menos un medicamento.")
        paciente = self.__pacientes__[dni]
        medico = self.__medicos__[matricula]
        receta = Receta(paciente, medico, medicamentos)
        self.__historias_clinicas__[dni].agregar_receta(receta)

    def obtener_historia_clinica(self, dni):
        self.validar_existencia_paciente(dni)
        return self.__historias_clinicas__[dni]

    # --- Validaciones y utilidades ---
    def validar_existencia_paciente(self, dni):
        if dni not in self.__pacientes__:
            raise PacienteNoEncontradoException("Paciente no encontrado.")

    def validar_existencia_medico(self, matricula):
        if matricula not in self.__medicos__:
            raise MedicoNoDisponibleException("Médico no encontrado.")

    def validar_turno_no_duplicado(self, matricula, fecha_hora):
        for turno in self.__turnos__:
            if (turno.obtener_medico().obtener_matricula() == matricula and
                turno.obtener_fecha_hora() == fecha_hora):
                raise TurnoOcupadoException("El médico ya tiene un turno en ese horario.")

    def obtener_dia_semana_en_espanol(self, fecha_hora):
        dias = [
            "lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"
        ]
        return dias[fecha_hora.weekday()]

    def obtener_especialidad_disponible(self, medico, dia_semana):
        return medico.obtener_especialidad_para_dia(dia_semana)

    def validar_especialidad_en_dia(self, medico, especialidad_solicitada, dia_semana):
        especialidad_disponible = self.obtener_especialidad_disponible(medico, dia_semana)
        if especialidad_disponible is None:
            raise MedicoNoDisponibleException("El médico no atiende ese día.")
        if especialidad_disponible.lower() != especialidad_solicitada.lower():
            raise MedicoNoDisponibleException("El médico no atiende esa especialidad ese día.")