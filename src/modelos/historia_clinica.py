class HistoriaClinica:
    def __init__(self, paciente):
        if paciente is None:
            raise ValueError("El paciente no puede ser None.")
        self.__paciente__ = paciente
        self.__turnos__ = []
        self.__recetas__ = []

    def agregar_turno(self, turno):
        self.__turnos__.append(turno)

    def agregar_receta(self, receta):
        self.__recetas__.append(receta)

    def obtener_turnos(self):
        return list(self.__turnos__)

    def obtener_recetas(self):
        return list(self.__recetas__)

    def __str__(self):
        turnos_str = "\n".join(str(t) for t in self.__turnos__)
        recetas_str = "\n".join(str(r) for r in self.__recetas__)
        return (
            f"Historia Clínica de {self.__paciente__}\n"
            f"--- Turnos ---\n{turnos_str if turnos_str else 'Sin turnos.'}\n"
            f"--- Recetas ---\n{recetas_str if recetas_str else 'Sin recetas.'}"
        )