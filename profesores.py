# profesores.py

profesores = []

def agregar_profesor(nombre, cedula, curso):
    profesor = {
        "nombre": nombre,
        "cedula": cedula,
        "curso": curso
    }
    profesores.append(profesor)

def consultar_profesores():
    return profesores
