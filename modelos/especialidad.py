class Especialidad:
    
    def __init__(self, tipo:str, dias:list):
        self.__tipo__ = tipo
        self.__dias__ = dias
    
   
    @property
    def obtener_especialidad(self) -> str: 
        return self.__tipo__
    
    
    def verificar_dia(self, dia:str) -> bool: 
        return dia in self.__dias__ 
    
    
    def __str__(self) -> str:
        dias_str = '\n'.join(self.__dias__)  
        return f"Especialidad: {self.__tipo__}\nDías disponibles:\n{dias_str}"