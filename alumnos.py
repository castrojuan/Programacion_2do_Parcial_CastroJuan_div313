from validaciones import pedir_dni, pedir_nota, pedir_edad, pedir_texto

def buscar_dni(diccionario_alumnos: dict, dni: str)-> None:
    """
    Busca si un DNI específico existe dentro del diccionario de alumnos.

    :param diccionario_alumnos: Diccionario cuyas claves son los DNI de los alumnos.
    :type diccionario_alumnos: dict
    :param dni: El número de documento que se desea buscar.
    :type dni: str
    :return: El DNI encontrado si existe en el diccionario; de lo contrario, None.
    :rtype: str o None
    """
    for i in diccionario_alumnos:
        if i == dni:
            return i
    return None 

 

def registro_alumno(diccionario_alumnos: dict)-> dict:
    """
    Gestiona el flujo interactivo para registrar un nuevo alumno en el sistema.

    Solicita los datos del alumno (DNI, nombre, apellido, edad y nota) mediante consola,
    valida que el DNI no esté duplicado y guarda la información en el diccionario.

    :Argumentos: diccionario_alumnos: Diccionario actual de los alumnos registrados.
    :type diccionario_alumnos: dict
    :return: El diccionario de alumnos actualizado con el nuevo registro.
    :rtype: dict
    """
    print("\n-- REGISTRO DE ALUMNO --")

    
    dni = pedir_dni(" Ingrese el DNI: ") 
    while buscar_dni(diccionario_alumnos, dni) != None:
        print("El dni ingresado ya existe ")
        dni = pedir_dni(" Ingrese el DNI: ")

    
    nombre = pedir_texto(" Nombre del Alumno: ")
    apellido = pedir_texto(" Apellido del alumno: ")
    edad = pedir_edad(" Edad del alumno: ")
    nota = pedir_nota(" Ingrese la nota: ")

    
    diccionario_alumnos[dni] = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "nota": nota,
    }

    print("Registro almacenado con éxito.")
    print("Registro finalizado.")  
    
    
    return diccionario_alumnos



    
def listar_alumnos(diccionario_alumnos: dict)-> None:
    """
    Muestra en pantalla la lista completa de todos los alumnos registrados.

    Si no hay alumnos registrados en el sistema, despliega un mensaje informativo.

    :param diccionario_alumnos: Diccionario con la información de los alumnos a listar.
    :type diccionario_alumnos: dict
    :return: No retorna ningún valor (imprime directamente en consola).
    :rtype: None
    """
    if len(diccionario_alumnos) == 0:
        print(f"No hay alumnos registrados")
        return None

    print("==LISTADO DE ALUMNOS==:")

    for i in diccionario_alumnos:
        alumno = diccionario_alumnos[i]

        print("-----------")
        print(f"DNI: {i}")
        print(f"nombre:{alumno['nombre']}")
        print(f"apellido:{alumno['apellido']}")
        print(f"edad:{alumno['edad']}")
        print(f"nota:{alumno['nota']}")





def buscar_alumno(diccionario_alumnos: dict)-> None:
    """
    Solicita un DNI e imprime en pantalla la información del alumno correspondiente.

    Si el sistema está vacío o si el DNI buscado no existe, muestra un aviso descriptivo.

    :param diccionario_alumnos: Diccionario donde se realizará la búsqueda del alumno.
    :type diccionario_alumnos: dict
    :return: No retorna ningún valor (imprime directamente en consola).
    :rtype: None
    """
    if len(diccionario_alumnos) == 0:
            print(f"No hay alumnos registrados ")
            return None

    dni = pedir_dni("Ingrese el DNI a buscar ")

    dni_encontrado = buscar_dni(diccionario_alumnos, dni)

    if dni_encontrado != None:
        alumno = diccionario_alumnos[dni_encontrado]
        print(f"dni {dni_encontrado} ")
        print(f"nombre {alumno['nombre']} ")     #aca estoy cambiando diccionario_alumnos por alumno 
        print(f"apellido {alumno['apellido']} ")
        print(f"edad {alumno['edad']} ")
        print(f"nota {alumno['nota']} ")

        return None

    print("No se encontro al alumno")
    return None  
  


def modificar_alumno(diccionario_alumnos: dict)-> dict:
    """
    Busca un alumno por su DNI y permite modificar todos sus datos registrados.

    Si el diccionario está vacío, informa al usuario. Si encuentra al alumno,
    solicita los nuevos datos (nombre, apellido, edad, nota) a través de la consola
    y sobrescribe la información existente.

    :param diccionario_alumnos: Diccionario actual de los alumnos registrados.
    :type diccionario_alumnos: dict
    :return: El diccionario con los datos del alumno actualizados, o None si no hay registros.
    :rtype: dict o None
    """
    if len(diccionario_alumnos) == 0:
        print(f"No hay alumnos registrados")
        return None

    dni = pedir_dni("Ingrese el DNI a buscar")
    
    dni_encontrado = buscar_dni(diccionario_alumnos, dni)

    if dni_encontrado != None:
     
        nuevo_nombre = pedir_texto("Ingrese el nuevo nombre: ")
                
        nuevo_apellido = pedir_texto("Ingrese el nuevo apellido: ")
                
        nueva_edad = pedir_edad("Nueva Edad: ")
                    
        nueva_nota = pedir_nota("Nueva Nota: ")

        diccionario_alumnos[dni_encontrado] = {
           "nombre": nuevo_nombre,
           "apellido": nuevo_apellido,
           "edad": nueva_edad,
           "nota": nueva_nota, 
        } 

        print(f"alumno {dni_encontrado} modificado con exito") 

    return diccionario_alumnos       
            



def eliminar_alumno(diccionario_alumnos:dict)-> dict:
    """
    Busca un alumno por su DNI y lo elimina permanentemente del sistema.

    Si el diccionario no contiene alumnos, muestra un aviso. Si el DNI ingresado
    existe en los registros, remueve al alumno del diccionario.

    :param diccionario_alumnos: Diccionario actual de los alumnos registrados.
    :type diccionario_alumnos: dict
    :return: El diccionario actualizado sin el alumno eliminado, o None si no hay registros.
    :rtype: dict o None
    """
    if len(diccionario_alumnos) == 0:
            print(f"No hay alumnos registrados")
            return None
    
    dni = pedir_dni("Ingrese el DNI del alumno que desea eliminar: ")
        
    dni_encontrado = buscar_dni(diccionario_alumnos, dni)
    
    if dni_encontrado != None:
         
        del diccionario_alumnos[dni_encontrado] 
    
        print(f"alumno {dni_encontrado} eliminado con exito") 
    
    return diccionario_alumnos
