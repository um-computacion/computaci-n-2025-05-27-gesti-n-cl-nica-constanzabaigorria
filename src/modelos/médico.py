class Medico:
    def __init__(self, nombre: str, matricula: str):
        if not nombre or not isinstance(nombre, str):
            raise ValueError("El nombre no puede estar vacío.")
        if not matricula or not isinstance(matricula, str):
            raise ValueError("La matrícula no puede estar vacía.")
        self.__nombre__ = nombre
        self.__matricula__ = matricula
        self.__especialidades__ = []

    def agregar_especialidad(self, especialidad):
        # No permitir duplicados por nombre de especialidad
        for esp in self.__especialidades__:
            if esp.obtener_especialidad().lower() == especialidad.obtener_especialidad().lower():
                raise ValueError("Especialidad duplicada para este médico.")
        self.__especialidades__.append(especialidad)

    def obtener_matricula(self) -> str:
        return self.__matricula__

    def obtener_especialidad_para_dia(self, dia: str):
        dia = dia.lower()
        for esp in self.__especialidades__:
            if esp.verificar_dia(dia):
                return esp.obtener_especialidad()
        return None

    def __str__(self):
        especialidades_str = ", ".join(str(esp) for esp in self.__especialidades__)
        return f"Médico: {self.__nombre__} | Matrícula: {self.__matricula__} | Especialidades: {especialidades_str}"