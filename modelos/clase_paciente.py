import datetime 
class Paciente:
  
    def __init__(self, nombre:str, dni:str, fecha_nacimiento:datetime.date):
        self.__nombre__ = nombre
        self.__dni__ = dni
        self.__fecha_nacmimiento__ = fecha_nacimiento
    
    
    @property 
    def obtener_dni(self) -> str:
        return self.__dni__
    
    
    def __str__(self) -> str:
        return f"Paciente: {self.__nombre__}\nDNI: {self.__dni__}\nFecha de Nacimiento: {self.__fecha_nacmimiento__}"