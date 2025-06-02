# alumnos.py

alumnos = []

def agregar_alumno(nombre, cedula, curso, nota):
    alumno = {
        "nombre": nombre,
        "cedula": cedula,
        "curso": curso,
        "nota": float(nota)
    }
    alumnos.append(alumno)

def consultar_alumnos():
    return alumnos

def promedio_general():
    if not alumnos:
        return 0
    return sum(a["nota"] for a in alumnos) / len(alumnos)

def clasificacion():
    aprobados = [a for a in alumnos if a["nota"] > 70]
    aplazados = [a for a in alumnos if 60 <= a["nota"] <= 69]
    reprobados = [a for a in alumnos if a["nota"] < 60]
    return aprobados, aplazados, reprobados

def cantidad_superiores_al_promedio():
    prom = promedio_general()
    return len([a for a in alumnos if a["nota"] > prom])
