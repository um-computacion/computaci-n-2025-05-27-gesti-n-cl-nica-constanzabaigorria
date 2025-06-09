class Turno:
    def __init__(self, paciente, medico, fecha_hora, especialidad):
        if paciente is None:
            raise ValueError("El paciente no puede estar vacio.")
        if medico is None:
            raise ValueError("El médico no puede estar vacío.")
        if fecha_hora is None:
            raise ValueError("La fecha y hora no pueden estar vacíos.")
        if not especialidad or not isinstance(especialidad, str):
            raise ValueError("La especialidad no puede estar vacía.")
        self.__paciente__ = paciente
        self.__medico__ = medico
        self.__fecha_hora__ = fecha_hora
        self.__especialidad__ = especialidad

    def obtener_medico(self):
        return self.__medico__

    def obtener_fecha_hora(self):
        return self.__fecha_hora__

    def __str__(self):
        return (
            f"Turno: Paciente: {self.__paciente__} | "
            f"Médico: {self.__medico__} | "
            f"Especialidad: {self.__especialidad__} | "
            f"Fecha y hora: {self.__fecha_hora__}"
        )