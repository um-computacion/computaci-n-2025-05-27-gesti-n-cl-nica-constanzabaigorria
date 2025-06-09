from datetime import datetime 
from modelos.clinica import Clinica
from modelos.clase_paciente import Paciente
from modelos.médico import Medico
from modelos.especialidad import Especialidad
from modelos.excepciones import (
    PacienteNoEncontradoException,
    MedicoNoEncontradoException,
    MedicoNoDisponibleException,
    TurnoOcupadoException,
    RecetaInvalidaException,
    HistoriaClinicaNoEncontradaException
)
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modelos.clinica import Clinica

class CLI:
    def __init__(self):
        self.clinica = Clinica("Clínica San Martín")

    def menu(self):
        print("\nSistema de gestión de clínica")
        print("-" * 50)
        print("1 - Agregar paciente")
        print("2 - Agregar médico")
        print("3 - Programar turno")
        print("4 - Ver turnos de médico")
        print("5 - Ver historia clínica")
        print("6 - Ver todos los pacientes")
        print("7 - Ver todos los médicos")
        print("0 - Salir")

    def ejecutar(self):
        while True:
            self.menu()
            try:
                opcion = input("\nSeleccione una opción: ").strip()
                
                if opcion == "0":
                    print("\nHasta luego!")
                    break
                elif opcion == "1":
                    self.agregar_paciente()
                elif opcion == "2":
                    self.agregar_medico()
                elif opcion == "3":
                    self.programar_turno()
                elif opcion == "4":
                    self.ver_turnos_medico()
                elif opcion == "5":
                    self.ver_historia_clinica()
                elif opcion == "6":
                    self.ver_todos_los_pacientes()
                elif opcion == "7":
                    self.ver_todos_los_medicos()
                else:
                    print("Opción inválida")
            except KeyboardInterrupt:
                print("\nPrograma terminado")
                break
            except Exception as e:
                print(f"Error: {e}")

    def agregar_paciente(self):
        print("\nAgregar Paciente")
        print("-" * 50)
        try:
            nombre = input("Nombre completo: ").strip()
            dni = input("DNI: ").strip()
            
            paciente = Paciente(nombre, dni)
            self.clinica.agregar_paciente(paciente)

            print(f"\nPaciente agregado: {paciente}")
            print(f"{paciente}")

        except ValueError as e:
            print(f"Error en los datos: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")
        
        input("\nPresione Enter para continuar...")

    def agregar_medico(self):
        print("\nAgregar Médico")
        print("-" * 50)
        try:
            nombre = input("Nombre completo de médico: ").strip()
            matricula = input("Matrícula: ").strip()
            
            medico = Medico(nombre, matricula)

            print("\nAgregue especialidades (Enter sin escribir nada para terminar): ")

            while True:
                especialidad_nombre = input("Especialidad: ").strip()
                if not especialidad_nombre:
                    break

                dias = self.solicitar_dias_atencion()
                if dias:
                    try:
                        especialidad = Especialidad(especialidad_nombre, dias)
                        medico.agregar_especialidad(especialidad)
                        print(f"Especialidad '{especialidad_nombre}' agregada")
                    except ValueError as e:
                        print(f"Error: {e}")
                        continue
                else:
                    print("No se proporcionaron dias validos")
                    continue

            self.clinica.agregar_medico(medico)
            print(f"\nMédico agregado: {medico}")
            print(f"{medico}")
        
        except ValueError as e:
            print(f"Error en los datos: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

        input("\nPresione Enter para continuar...")

    def solicitar_dias_atencion(self):
        print("Dias disponibles: lunes, martes, miercoles, jueves, viernes, sabado, domingo")
        dias_input = input("Dias de atencion: (separados por comas): ").strip()

        if not dias_input:
            return []
        
        dias = [dia.strip() for dia in dias_input.split(",") if dia.strip()]
        return dias
    
    def programar_turno(self):
        print("\nProgramar Turno")
        print("-" * 50)
        try:
            # Mostrar pacientes y médicos disponibles
            print("\nPacientes registrados:")
            for p in self.clinica.pacientes:
                print(f"- {p}")
            
            print("\nMédicos registrados:")
            for m in self.clinica.medicos:
                print(f"- {m}")
            
            # Solicitar datos
            dni = input("\nDNI del paciente: ").strip()
            matricula = input("Matrícula del médico: ").strip()
            especialidad = input("Especialidad del médico: ").strip()

            fecha = self.solicitar_fecha()
            
            # Buscar paciente y médico
            paciente = next((p for p in self.clinica.pacientes if p.dni == dni), None)
            medico = next((m for m in self.clinica.medicos if m.matricula == matricula), None)
            
            if not paciente:
                raise PacienteNoEncontradoException(dni)
            if not medico:
                raise MedicoNoEncontradoException(matricula)
            
            turno = self.clinica.programar_turno(paciente, medico, fecha, especialidad)
            print(f"\nTurno programado: {turno}")
            
        except (PacienteNoEncontradoException, MedicoNoEncontradoException,
                MedicoNoDisponibleException, TurnoOcupadoException) as e:
            print(f"Error: {e}")
        
        input("\nPresione Enter para continuar...")

    def solicitar_fecha(self):
        while True:
            try:
                fecha = input("Fecha (dd/mm/yyyy HH:MM): ").strip()
                return datetime.strptime(fecha, "%d/%m/%Y %H:%M")
            except ValueError:
                print("Formato inválido. Use dd/mm/yyyy HH:MM")

    def agregar_especialidad_a_medico(self):
        print("\nAgregar especialidad a medico")
        print("-" * 50)

        try:
            matricula = input("Matricula del medico: ").strip()

            medico = self.clinica.obtener_medico_por_matricula(matricula)

            especialidad_nombre = input("Nombre especialidad: ").strip()
            dias = self.solicitar_dias_atencion()

            if dias:
                especialidad = Especialidad(especialidad_nombre, dias)
                medico.agregar_especialidad(especialidad)

                print("Especialidad agregada")
                print(f"{especialidad}")
            else:
                print("Dias invalidos")
        
        except MedicoNoEncontradoException as e:
            print(f"{e}")
        except ValueError as e:
            print(f"Error en los datos: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

        input("\nEnter para continuar")

    def emitir_receta(self):
        print("\nEmitir receta")
        print("-" * 50)

        try:
            dni = input("DNI del paciente: ").strip()
            matricula = input("Matricula medico: ").strip()

            print("\nMedicamentos (Enter sin nada para terminar): ")
            medicamentos = []
            
            while True:
                medicamento = input("Medicamento: ").strip()
                if not medicamento: 
                    break
                medicamentos.append(medicamento)

            if not medicamentos:
                print("Debe ingresar por lo menos un medicamento")
                return
            
            self.clinica.emitir_receta(dni, matricula, medicamentos)

            print("Receta emitida")
            print(f"Paciente DNI: {dni}")
            print(f"Medico: {matricula}")
            print(f"Medicamentos: {', '.join(medicamentos)}")
        
        except (PacienteNoEncontradoException, MedicoNoEncontradoException,
                RecetaInvalidaException) as e:
            print(f"{e}")
        except ValueError as e:
            print(f"Error en los datos: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

        input("\nEnter para continuar")

    def ver_turnos_medico(self):
        print("\nVer Turnos de Médico")
        print("-" * 50)
        try:
            matricula = input("Matrícula del médico: ").strip()
            fecha = input("Fecha (dd/mm/yyyy) o Enter para todos: ").strip()
            
            medico = next((m for m in self.clinica.medicos if m.matricula == matricula), None)
            if not medico:
                raise MedicoNoEncontradoException(matricula)
            
            if fecha:
                fecha = datetime.strptime(fecha, "%d/%m/%Y")
                turnos = self.clinica.buscar_turnos_medico(medico, fecha)
            else:
                turnos = self.clinica.buscar_turnos_medico(medico)
            
            if not turnos:
                print("No hay turnos registrados")
            else:
                for turno in turnos:
                    print(turno)
                    
        except MedicoNoEncontradoException as e:
            print(f"Error: {e}")
        
        input("\nPresione Enter para continuar...")

    def ver_historia_clinica(self):
        print("\nVer Historia Clínica")
        print("-" * 50)
        try:
            dni = input("DNI del paciente: ").strip()
            paciente = next((p for p in self.clinica.pacientes if p.dni == dni), None)
            
            if not paciente:
                raise PacienteNoEncontradoException(dni)
            
            historia = self.clinica.obtener_historia_clinica(paciente)
            print("\n", historia)
            
        except (PacienteNoEncontradoException, HistoriaClinicaNoEncontradaException) as e:
            print(f"Error: {e}")
        
        input("\nPresione Enter para continuar...")

    def ver_todos_los_pacientes(self):
        print("\nPacientes Registrados")
        print("-" * 50)
        if not self.clinica.pacientes:
            print("No hay pacientes registrados")
        else:
            for i, paciente in enumerate(self.clinica.pacientes, 1):
                print(f"{i}. {paciente}")
        
        input("\nPresione Enter para continuar...")

    def ver_todos_los_medicos(self):
        print("\nMédicos Registrados")
        print("-" * 50)
        if not self.clinica.medicos:
            print("No hay médicos registrados")
        else:
            for i, medico in enumerate(self.clinica.medicos, 1):
                print(f"{i}. {medico}")
        
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    cli = CLI()
    cli.ejecutar()

