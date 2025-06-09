class Especialidad:
    DIAS_VALIDOS = [
        "lunes", "martes", "miércoles", "miercoles", "jueves", "viernes", "sábado", "sabado", "domingo"
    ]

    def __init__(self, tipo: str, dias: list):
        if not tipo or not isinstance(tipo, str):
            raise ValueError("El tipo de especialidad no puede estar vacío.")
        if not dias or not isinstance(dias, list):
            raise ValueError("La lista de días no puede estar vacía.")
        # Normalizar y validar días
        dias_normalizados = []
        for dia in dias:
            if not isinstance(dia, str):
                raise ValueError("Día inválido.")
            dia_lower = dia.lower()
            # Permitir disintas formas de "miércoles" y "sábado"
            if dia_lower not in self.DIAS_VALIDOS:
                raise ValueError(f"Día inválido: {dia}")
            # Normalizar a "miércoles" y "sábado"
            if dia_lower == "miercoles":
                dia_lower = "miércoles"
            if dia_lower == "sabado":
                dia_lower = "sábado"
            dias_normalizados.append(dia_lower)
        self.__tipo__ = tipo
        self.__dias__ = dias_normalizados

    def obtener_especialidad(self) -> str:
        return self.__tipo__

    def verificar_dia(self, dia: str) -> bool:
        if not isinstance(dia, str):
            return False
        dia_lower = dia.lower()
        if dia_lower == "miercoles":
            dia_lower = "miércoles"
        if dia_lower == "sabado":
            dia_lower = "sábado"
        return dia_lower in self.__dias__

    def __str__(self):
        dias_str = ", ".join(self.__dias__)
        return f"{self.__tipo__} (Días: {dias_str})"