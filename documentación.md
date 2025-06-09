# Manual de Instrucciones - Sistema de Gestión Clínica

## 📋 Índice
1. Requisitos del Sistema
2. Instalación
3. Ejecución del Sistema
4. Funcionalidades
5. Mensajes de Error Comunes

## 1. Requisitos del Sistema
- Python 3.7 o superior
- Terminal o consola de comandos
- Estructura de directorios correcta:
```
clinica/
├── modelos/
│   ├── __init__.py
│   ├── clase_paciente.py
│   ├── médico.py
│   ├── clinica.py
│   ├── turno.py
│   ├── receta.py
│   └── excepciones.py
├── cli/
│   ├── __init__.py
│   └── cli.py
└── test/
    ├── __init__.py
    └── tests_*.py
```

## 2. Instalación
1. Clone o descargue el repositorio:
```bash
git clone <url-del-repositorio>
cd computaci-n-2025-05-27-gesti-n-cl-nica-constanzabaigorria
```

## 3. Ejecución del Sistema
Para iniciar el sistema, ejecute en la terminal:
```bash
python3 main.py
```

## 4. Funcionalidades

### 4.1 Menú Principal
El sistema muestra las siguientes opciones:
```
Sistema de gestión de clínica
--------------------------------------------------
1 - Agregar paciente
2 - Agregar médico
3 - Programar turno
4 - Agregar especialidad a médico
5 - Emitir receta
6 - Ver historia clínica
7 - Ver todos los turnos
8 - Ver todos los pacientes
9 - Ver todos los médicos
0 - Salir
```

### 4.2 Agregar Paciente
1. Seleccione opción `1`
2. Ingrese:
   - Nombre completo
   - DNI
   - Fecha de nacimiento (formato: dd/mm/aaaa)

### 4.3 Agregar Médico
1. Seleccione opción `2`
2. Ingrese:
   - Nombre completo
   - Matrícula profesional
   - Especialidades y días de atención
     - Para cada especialidad:
       - Nombre de la especialidad
       - Días de atención (separados por comas)
     - Presione Enter sin texto para finalizar

### 4.4 Programar Turno
1. Seleccione opción `3`
2. Ingrese:
   - DNI del paciente
   - Matrícula del médico
   - Especialidad
   - Fecha (formato: dd/mm/aaaa)
   - Hora (formato: HH:MM)

### 4.5 Agregar Especialidad a Médico
1. Seleccione opción `4`
2. Ingrese:
   - Matrícula del médico
   - Nombre de la especialidad
   - Días de atención (separados por comas)

### 4.6 Emitir Receta
1. Seleccione opción `5`
2. Ingrese:
   - DNI del paciente
   - Matrícula del médico
   - Medicamentos (uno por línea, Enter sin texto para finalizar)

### 4.7 Ver Historia Clínica
1. Seleccione opción `6`
2. Ingrese el DNI del paciente

### 4.8-4.10 Consultas
- Opción `7`: Ver todos los turnos
- Opción `8`: Ver todos los pacientes
- Opción `9`: Ver todos los médicos

## 5. Mensajes de Error Comunes

### Pacientes
- "Paciente ya registrado": El DNI ya existe en el sistema
- "DNI inválido": Formato de DNI incorrecto

### Médicos
- "Médico ya registrado": La matrícula ya existe
- "Médico no disponible": El médico no atiende en la fecha/especialidad solicitada

### Turnos
- "Turno ocupado": El médico ya tiene un turno en ese horario
- "Especialidad no disponible": El médico no atiende esa especialidad ese día

### Recetas
- "Debe indicar al menos un medicamento": No se ingresaron medicamentos
- "Paciente/Médico no encontrado": DNI o matrícula incorrectos

## 6. Ejecutar Tests
Para ejecutar las pruebas unitarias:
```bash
cd test
python3 -m unittest discover -v
```

## 7. Salir del Sistema
Seleccione la opción `0` en el menú principal o presione `Ctrl+C`