def mostrar_estadisticas(diccionario_alumnos:dict)-> None:
    """Imprime un resumen estadístico de las calificaciones de los alumnos.

    Si el diccionario está vacío, muestra un aviso y finaliza sin calcular métricas.

    Args:
        diccionario_alumnos: Diccionario que asocia el identificador de cada
            alumno con sus datos, incluyendo su ``"nota"``.
    """
    print("\n--- ESTADÍSTICAS ---")

    if len(diccionario_alumnos) == 0:
        print("No hay alumnos para calcular estadísticas.")
        return None
    
    contar_alumnos(diccionario_alumnos)
    promedio_notas(diccionario_alumnos)
    alumno_mayor_nota(diccionario_alumnos)
    mostrar_aprobados(diccionario_alumnos)
    mostrar_desaprobados(diccionario_alumnos)





def contar_alumnos(diccionario_alumnos: dict)-> int:
    """Calcula e imprime la cantidad total de alumnos registrados.

    Args:
        diccionario_alumnos: Diccionario con los registros de los alumnos.

    Returns:
        La cantidad total de alumnos.
    """

    total = len(diccionario_alumnos)
    print(f"la cantidad total de alumnos es {total}")

    return total





def promedio_notas(diccionario_alumnos: dict)-> float:
    """Calcula e imprime el promedio general de las notas de los alumnos.

    Nota: asume que ``diccionario_alumnos`` no está vacío para evitar división por cero.

    Args:
        diccionario_alumnos: Diccionario con los datos de los alumnos y su ``"nota"``.

    Returns:
        El promedio aritmético de todas las notas.
    """
    suma_notas = 0

    for alumno in diccionario_alumnos.values():
        suma_notas += alumno["nota"] 

    promedio_total = suma_notas/len(diccionario_alumnos)
    print(f"Promedio total {promedio_total:.2f}") 

    return (promedio_total)





def alumno_mayor_nota(diccionario_alumnos: dict):
    
    nota_mas_alta = 0
    nombre_mejor_nota = ""
    apellido_mejor_nota = ""
    
    for alumno in diccionario_alumnos.values():
        
        if alumno["nota"] > nota_mas_alta:
            nota_mas_alta = alumno["nota"]
            nombre_mejor_nota = alumno["nombre"]
            apellido_mejor_nota = alumno["apellido"]


    print(f"El alumno con mayor nota es {nombre_mejor_nota} {apellido_mejor_nota} con un {nota_mas_alta:.2f}")        

    return nombre_mejor_nota, apellido_mejor_nota, nota_mas_alta




def mostrar_aprobados(diccionario_alumnos: dict)-> int:
    """Cuenta e imprime cuántos alumnos tienen una nota mayor o igual a 6.

    Args:
        diccionario_alumnos: Diccionario con los datos de los alumnos y su ``"nota"``.

    Returns:
        La cantidad de alumnos aprobados.
    """
    aprobados = 0

    for alumno in diccionario_alumnos.values():
        
        if alumno["nota"] >= 6:
            aprobados += 1

    print(f"La cantidad de alumnos aprobados {aprobados} ")

    return aprobados





def mostrar_desaprobados(diccionario_alumnos:dict)-> int:
    """Cuenta e imprime cuántos alumnos tienen una nota menor a 6.

    Args:
        diccionario_alumnos: Diccionario con los datos de los alumnos y su ``"nota"``.

    Returns:
        La cantidad de alumnos desaprobados.
    """
    desaprobados = 0

    for alumno in diccionario_alumnos.values():
        
        if alumno["nota"] < 6:
            desaprobados += 1

    print(f"La cantidad de alumnos desaprobados {desaprobados} ")

    return desaprobados 
    






