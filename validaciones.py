

def validar_textos(texto: str)-> bool:
    """
    Valida que el texto contenga únicamente letras (A-Z, a-z) y espacios,
    y que no esté completamente vacío.

    Args:
        texto (str): La cadena de caracteres a validar.

    Returns:
        bool: True si el texto es válido y no está vacío, False en caso contrario.
    """

    for i in range(len(texto)):
        caracter = texto[i]  
        minuscula = "a" <= caracter <= "z"
        mayuscula = "A" <= caracter <= "Z" 
        espacio = caracter == " "

        if not (minuscula or mayuscula or espacio):
            print("solo debe ingresar letras")
            return False

    return texto.strip() != ""
    
    

 

def validar_entero_no_negativo(texto: str)-> bool:
    """
    Valida si una cadena de texto representa un número entero no negativo (solo dígitos).

    Args:
        texto (str): La cadena de texto a validar.

    Returns:
        bool: True si el texto contiene solo dígitos y no está vacío, False de lo contrario.
    """
    
    if texto == "":
        print(f" No ingreso ningun numero ")
        return False
    for i in range(len(texto)): 
        if texto[i] < "0" or texto[i] > "9":
            return False
        
    return True


def pedir_texto(mensaje: str)-> str:
    """
    Solicita un texto al usuario por consola y lo valida repetidamente 
    hasta que cumpla con las condiciones de validar_textos.

    Args:
        mensaje (str): El mensaje que se mostrará al usuario al pedir el dato.

    Returns:
        str: El texto válido ingresado por el usuario.
    """
    texto = input(mensaje)
    while not validar_textos(texto):
        print(f"nombre invalido")
        texto = input(mensaje)
        
    return texto


def pedir_entero(mensaje: str)-> int:
    """
    Solicita un número entero al usuario por consola y lo valida repetidamente
    hasta que se ingrese un número entero no negativo válido.

    Args:
        mensaje (str): El mensaje que se mostrará al usuario al pedir el dato.

    Returns:
        int: El número entero validado y convertido.
    """
    numero = input(mensaje)
    while not validar_entero_no_negativo(numero):
        print(f"no es un nro entero")
        numero = input(mensaje)

    return int(numero)


def pedir_dni(mensaje: str)-> int:
    """
    Solicita y valida un número de DNI, asegurando que sea un entero de exactamente 8 dígitos.

    Args:
        mensaje (str): El mensaje que se mostrará al usuario al pedir el DNI.

    Returns:
        int: Un número de DNI válido (entre 10,000,000 y 99,999,999).
    """
    documento = pedir_entero(mensaje)
    while documento < 10000000 or documento > 99999999:
        print(f"Error, el dni debe tener 8 digitos")
        documento = pedir_entero(mensaje)

    return documento 


def pedir_edad(mensaje:str)-> int:
    """
    Solicita y valida una edad, asegurando que se encuentre en el rango de 4 a 80 años.

    Args:
        mensaje (str): El mensaje que se mostrará al usuario al pedir la edad.

    Returns:
        int: Una edad válida entre 4 y 80 inclusive.
    """
    edad = pedir_entero(mensaje)
    while edad < 4 or edad > 80:
        print(f"Error, la edad debe ser entre 4 y 80 años")
        edad = pedir_entero(mensaje)

    return edad 


def pedir_nota(mensaje:str)-> int:
    """
    Solicita y valida una nota académica, asegurando que esté en el rango de 0 a 10.

    Args:
        mensaje (str): El mensaje que se mostrará al usuario al pedir la nota.

    Returns:
        int: Una nota válida entre 0 y 10 inclusive.
    """
    nota = pedir_entero(mensaje)
    while nota < 0 or nota > 10:
        print(f"La nota debe estar entre 0 y 10")
        nota = pedir_entero(mensaje)

    return nota










    