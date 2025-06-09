from datetime import date
from clase_paciente import Paciente
from médico import Medico

class Receta:
    def __init__(self, paciente, medico, medicamentos, fecha=None):
        self.paciente = paciente  # clase Paciente
        self.medico = medico      # clase Médico
        self.medicamentos = medicamentos  # lista de medicamentos
        self.fecha = fecha if fecha else date.today()

    def agregar_medicamento(self, medicamento):
        self.medicamentos.append(medicamento)

    def __str__(self):
        meds = ', '.join(self.medicamentos)
        return f"Receta para {self.paciente}, emitida por {self.medico} el {self.fecha}: {meds}"