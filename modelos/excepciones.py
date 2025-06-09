class PacienteNoEncontradoException(Exception):
    # Excepción lanzada cuando no se encuentra un paciente en el sistema.
    def __init__(self, dni=None, mensaje="Paciente no encontrado"):
        self.dni = dni
        self.mensaje = f"{mensaje}: DNI {dni}" if dni else mensaje
        super().__init__(self.mensaje)

class MedicoNoEncontradoException(Exception):
   # Excepción lanzada cuando no se encuentra un médico en el sistema.
    def __init__(self, matricula=None, mensaje="Médico no encontrado"):
        self.matricula = matricula
        self.mensaje = f"{mensaje}: Matrícula {matricula}" if matricula else mensaje
        super().__init__(self.mensaje)

class MedicoNoDisponibleException(Exception):
    # Excepción lanzada cuando un médico no está disponible en el horario solicitado.
    def __init__(self, medico=None, fecha=None):
        self.medico = medico
        self.fecha = fecha
        mensaje = "Médico no disponible"
        if medico and fecha:
            mensaje = f"{mensaje}: {medico} en {fecha.strftime('%d/%m/%Y %H:%M')}"
        super().__init__(mensaje)

class TurnoOcupadoException(Exception):
    # Excepción lanzada cuando se intenta programar un turno en un horario ya ocupado.
    def __init__(self, fecha=None, medico=None):
        mensaje = "Turno ocupado"
        if fecha and medico:
            mensaje = f"{mensaje}: {fecha.strftime('%d/%m/%Y %H:%M')} con {medico}"
        super().__init__(mensaje)

class RecetaInvalidaException(Exception):
    # Excepción lanzada cuando una receta no cumple con los requisitos necesarios.
    def __init__(self, mensaje="Receta inválida"):
        super().__init__(mensaje)

class HistoriaClinicaNoEncontradaException(Exception):
    # Excepción lanzada cuando no se encuentra la historia clínica de un paciente.
    def __init__(self, paciente=None):
        mensaje = "Historia clínica no encontrada"
        if paciente:
            mensaje = f"{mensaje} para el paciente {paciente}"
        super().__init__(mensaje)