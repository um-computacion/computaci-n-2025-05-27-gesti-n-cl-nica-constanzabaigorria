from datetime import datetime

class Receta:
    def __init__(self, paciente, medico, medicamentos):
        if paciente is None:
            raise ValueError("El paciente no puede estar vacío.")
        if medico is None:
            raise ValueError("El médico no puede estar vacío.")
        if not medicamentos or not isinstance(medicamentos, list) or len(medicamentos) == 0:
            raise ValueError("Debe indicar al menos un medicamento.")
        self.__paciente__ = paciente
        self.__medico__ = medico
        self.__medicamentos__ = medicamentos
        self._fecha = datetime.now()

    def obtener_fecha(self):
        return self._fecha

    def __str__(self):
        meds = ", ".join(self.__medicamentos__)
        return (
            f"Receta: Paciente: {self.__paciente__} | "
            f"Médico: {self.__medico__} | "
            f"Medicamentos: {meds} | "
            f"Fecha: {self._fecha.strftime('%d/%m/%Y %H:%M')}"
        )