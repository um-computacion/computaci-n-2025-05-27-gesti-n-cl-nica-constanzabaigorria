class Paciente:
    def __init__(self, nombre: str, dni: str, fecha_nacimiento: str):
        if not nombre or not isinstance(nombre, str):
            raise ValueError("El nombre no puede estar vacío.")
        if not dni or not isinstance(dni, str):
            raise ValueError("El DNI no puede estar vacío.")
        if not fecha_nacimiento or not isinstance(fecha_nacimiento, str):
            raise ValueError("La fecha de nacimiento no puede estar vacía.")
        self.__nombre__ = nombre
        self.__dni__ = dni
        self.__fecha_nacimiento__ = fecha_nacimiento

    def obtener_dni(self) -> str:
        return self.__dni__

    def __str__(self) -> str:
        return f"Paciente: {self.__nombre__} | DNI: {self.__dni__} | Nacimiento: {self.__fecha_nacimiento__}"