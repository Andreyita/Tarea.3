# cursos.py

cursos = []

def agregar_curso(codigo, nombre):
    curso = {
        "codigo": codigo,
        "nombre": nombre
    }
    cursos.append(curso)

def consultar_cursos():
    return cursos

def existe_curso(codigo):
    return any(c["codigo"] == codigo for c in cursos)
