from datetime import datetime
from .clase_paciente import Paciente
from .receta import Receta
from .médico import Medico

class HistoriaClinica:
    def __init__(self, paciente):
        if not isinstance(paciente, Paciente):
            raise TypeError("El paciente debe ser una instancia de la clase Paciente")
        
        self.paciente = paciente
        self.consultas = []
        self.recetas = []
        self.fecha_creacion = datetime.now()
        
    def agregar_consulta(self, fecha, motivo, diagnostico, medico):
        if not isinstance(fecha, datetime):
            raise TypeError("La fecha debe ser una instancia de datetime")
        if not isinstance(medico, Medico):
            raise TypeError("El médico debe ser una instancia de la clase Medico")
        if not isinstance(motivo, str) or not motivo.strip():
            raise ValueError("El motivo no puede estar vacío")
        if not isinstance(diagnostico, str) or not diagnostico.strip():
            raise ValueError("El diagnóstico no puede estar vacío")
            
        consulta = {
            'fecha': fecha,
            'motivo': motivo.strip(),
            'diagnostico': diagnostico.strip(),
            'medico': medico,
            'fecha_registro': datetime.now()
        }
        self.consultas.append(consulta)
        
    def agregar_receta(self, receta):
        if not isinstance(receta, Receta):
            raise TypeError("El parámetro debe ser una instancia de Receta")
        if receta.paciente != self.paciente:
            raise ValueError("La receta no corresponde a este paciente")
        self.recetas.append(receta)
        
    def obtener_consultas(self):
        return sorted(self.consultas, key=lambda x: x['fecha'], reverse=True)
    
    def obtener_recetas(self):
        return sorted(self.recetas, key=lambda x: x.fecha, reverse=True)
    
    def buscar_consultas_por_fecha(self, fecha):
        if not isinstance(fecha, datetime):
            raise TypeError("La fecha debe ser una instancia de datetime")
        return [consulta for consulta in self.consultas 
                if consulta['fecha'].date() == fecha.date()]
    
    def __str__(self):
        return (f"Historia Clínica de {self.paciente}\n"
                f"Fecha de creación: {self.fecha_creacion.strftime('%d/%m/%Y')}\n"
                f"Cantidad de consultas: {len(self.consultas)}\n"
                f"Cantidad de recetas: {len(self.recetas)}")