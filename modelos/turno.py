from datetime import datetime
from clase_paciente import Paciente
from médico import Medico
from especialidad import Especialidad

class Turno:
    def __init__(self, paciente: Paciente, medico: Medico, fecha: datetime, duracion: int = 30):
        if not isinstance(paciente, Paciente):
            raise TypeError("El paciente debe ser una instancia de la clase Paciente")
        if not isinstance(medico, Medico):
            raise TypeError("El médico debe ser una instancia de la clase Medico")
        if not isinstance(fecha, datetime):
            raise TypeError("La fecha debe ser una instancia de datetime")
        
        self.paciente = paciente
        self.medico = medico
        self.fecha = fecha
        self.duracion = duracion  # duración en minutos
        self.estado = "Programado"  # Programado, Completado, Cancelado
        
    def cancelar(self):
        self.estado = "Cancelado"
        
    def completar(self):
        self.estado = "Completado"
        
    def reprogramar(self, nueva_fecha: datetime):
        if not isinstance(nueva_fecha, datetime):
            raise TypeError("La nueva fecha debe ser una instancia de datetime")
        self.fecha = nueva_fecha
        self.estado = "Programado"
        
    def __str__(self):
        return (f"Turno de {self.paciente} con {self.medico} "
                f"el {self.fecha.strftime('%d/%m/%Y %H:%M')} "
                f"- Estado: {self.estado}")