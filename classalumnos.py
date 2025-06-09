
import alumnos
import profesores
import cursos

class SistemaEscolar:
    def __init__(self):
        pass  # No necesitas atributos por ahora

    def mostrar_menu(self):
        while True:
            print("\n--- Sistema Escolar ---")
            print("1. Agregar/Consultar Alumnos")
            print("2. Agregar/Consultar Profesores")
            print("3. Agregar/Consultar Cursos")
            print("4. Ver Reporte")
            print("5. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                self.menu_alumnos()
            elif opcion == '2':
                self.menu_profesores()
            elif opcion == '3':
                self.menu_cursos()
            elif opcion == '4':
                self.generar_reporte()
            elif opcion == '5':
                print("Saliendo del sistema...")
                break
            else:
                print("Opción inválida. Intente nuevamente.")

    def menu_alumnos(self):
        sub = input("a) Agregar Alumno\nb) Consultar Alumnos\nSeleccione: ").lower()
        if sub == 'a':
            nombre = input("Nombre alumno: ")
            cedula = input("Cédula alumno: ")
            curso = input("Curso alumno (código): ")
            if not cursos.existe_curso(curso):
                print("Error: El curso no existe.")
                return
            nota = input("Nota alumno (0-100): ")
            alumnos.agregar_alumno(nombre, cedula, curso, nota)
        elif sub == 'b':
            for a in alumnos.consultar_alumnos():
                print(a)

    def menu_profesores(self):
        sub = input("a) Agregar Profesor\nb) Consultar Profesores\nSeleccione: ").lower()
        if sub == 'a':
            nombre = input("Nombre profesor: ")
            cedula = input("Cédula profesor: ")
            curso = input("Curso que imparte (código): ")
            if not cursos.existe_curso(curso):
                print("Error: El curso no existe.")
                return
            profesores.agregar_profesor(nombre, cedula, curso)
        elif sub == 'b':
            for p in profesores.consultar_profesores():
                print(p)

    def menu_cursos(self):
        sub = input("a) Agregar Curso\nb) Consultar Cursos\nSeleccione: ").lower()
        if sub == 'a':
            codigo = input("Código del curso: ")
            nombre = input("Nombre del curso: ")
            cursos.agregar_curso(codigo, nombre)
        elif sub == 'b':
            for c in cursos.consultar_cursos():
                print(c)

    def generar_reporte(self):
        total = len(alumnos.consultar_alumnos())
        prom = alumnos.promedio_general()
        aprobados, aplazados, reprobados = alumnos.clasificacion()
        superiores = alumnos.cantidad_superiores_al_promedio()

        print("\n--- REPORTE GENERAL ---")
        print(f"Total de estudiantes: {total}")
        print(f"Promedio general de notas: {prom:.2f}")
        print(f"Aprobados: {len(aprobados)}")
        print(f"Aplazados: {len(aplazados)}")
        print(f"Reprobados: {len(reprobados)}")
        print(f"Notas superiores al promedio: {superiores}")

if __name__ == "__main__":
    sistema = SistemaEscolar()
    sistema.mostrar_menu()

