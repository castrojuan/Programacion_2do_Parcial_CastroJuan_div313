import json

def cargar_alumnos()-> dict:
    """
    Carga la información de los alumnos desde un archivo JSON y convierte las claves a enteros.

    Lee el archivo 'alumnos.json' y, debido a que el formato JSON guarda todas las 
    claves como cadenas de texto (str), transforma los DNI de texto a enteros (int) 
    para mantener la consistencia en el programa.

    :return: Un diccionario con los alumnos cargados, donde la clave es el DNI (int).
    :rtype: dict
    
    """
    with open("alumnos.json","r", encoding = "utf-8") as archivo:
        diccionario_alumnos = json.load(archivo)
    if len(diccionario_alumnos) == 0:
        return diccionario_alumnos

    for dni in list(diccionario_alumnos.keys()):
        diccionario_alumnos[int(dni)] = diccionario_alumnos.pop(dni)

    return diccionario_alumnos



def guardar_alumnos(diccionario_alumnos: dict)-> None:
    """
    Guarda el diccionario actual de alumnos en un archivo con formato JSON.

    Si el diccionario contiene registros, los convierte en una cadena de texto 
    con formato JSON estructurado (indentación de 4 espacios) y los escribe 
    en el archivo 'alumnos.json'.

    :param diccionario_alumnos: Diccionario de alumnos que se desea respaldar.
    :type diccionario_alumnos: dict
    :return: No retorna ningún valor.
    :rtype: None
    """
    if len(diccionario_alumnos) == 0:
            return diccionario_alumnos
    with open("alumnos.json", "w", encoding="utf-8") as archivo:
            texto_json = json.dumps(diccionario_alumnos, indent=4)
            archivo.write(texto_json)