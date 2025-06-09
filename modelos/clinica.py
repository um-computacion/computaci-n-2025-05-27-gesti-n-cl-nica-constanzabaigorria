from datetime import datetime
from .médico import Medico
from .clase_paciente import Paciente
from .turno import Turno
from .historia_clinica import HistoriaClinica
from .especialidad import Especialidad
from .receta import Receta

class Clinica:
    def __init__(self, nombre):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre de la clínica no puede estar vacío")
        
        self.nombre = nombre.strip()
        self.medicos = []
        self.pacientes = []
        self.turnos = []
        self.historias_clinicas = {}  # dni_paciente: historia_clinica
        
    def agregar_medico(self, medico):
        if not isinstance(medico, Medico):
            raise TypeError("El parámetro debe ser una instancia de Medico")
        if medico in self.medicos:
            raise ValueError("El médico ya está registrado")
        self.medicos.append(medico)
        
    def agregar_paciente(self, paciente):
        if not isinstance(paciente, Paciente):
            raise TypeError("El parámetro debe ser una instancia de Paciente")
        if paciente in self.pacientes:
            raise ValueError("El paciente ya está registrado")
        self.pacientes.append(paciente)
        self.historias_clinicas[paciente.dni] = HistoriaClinica(paciente)
        
    def programar_turno(self, paciente, medico, fecha):
        if not isinstance(paciente, Paciente) or paciente not in self.pacientes:
            raise ValueError("Paciente no registrado")
        if not isinstance(medico, Medico) or medico not in self.medicos:
            raise ValueError("Médico no registrado")
        if not isinstance(fecha, datetime):
            raise TypeError("La fecha debe ser una instancia de datetime")
            
        # Verificar disponibilidad
        for turno in self.turnos:
            if (turno.medico == medico and 
                turno.fecha.date() == fecha.date() and 
                turno.estado == "Programado"):
                raise ValueError("El médico ya tiene un turno en ese horario")
        
        turno = Turno(paciente, medico, fecha)
        self.turnos.append(turno)
        return turno
        
    def buscar_turnos_medico(self, medico, fecha=None):
        if not isinstance(medico, Medico):
            raise TypeError("El parámetro debe ser una instancia de Medico")
            
        turnos = [t for t in self.turnos if t.medico == medico]
        if fecha:
            if not isinstance(fecha, datetime):
                raise TypeError("La fecha debe ser una instancia de datetime")
            turnos = [t for t in turnos if t.fecha.date() == fecha.date()]
        return sorted(turnos, key=lambda x: x.fecha)
    
    def obtener_historia_clinica(self, paciente):
        if not isinstance(paciente, Paciente):
            raise TypeError("El parámetro debe ser una instancia de Paciente")
        return self.historias_clinicas.get(paciente.dni)
    
    def __str__(self):
        return (f"Clínica {self.nombre}\n"
                f"Médicos registrados: {len(self.medicos)}\n"
                f"Pacientes registrados: {len(self.pacientes)}\n"
                f"Turnos programados: {len([t for t in self.turnos if t.estado == 'Programado'])}")