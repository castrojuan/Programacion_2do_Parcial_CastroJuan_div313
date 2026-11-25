from alumnos import registro_alumno, listar_alumnos, buscar_alumno, modificar_alumno, eliminar_alumno
from estadisticas import mostrar_estadisticas
from archivo import guardar_alumnos, cargar_alumnos

display_menu = False

diccionario_alumnos = cargar_alumnos()

while not display_menu:
        
    print("\n======== GESTIÓN DE ALUMNOS ========")
    print("1. Registrar alumno\n2. Listar alumnos\n3. Buscar alumno")
    print("4. Modificar alumno\n5. Eliminar alumno\n6. Ver estadísticas")
    print("7. Salir\n====================================")

    opcion = input("Seleccione una opcion:  ")

    match opcion:
        case "1": 
            registro_alumno(diccionario_alumnos)
            guardar_alumnos(diccionario_alumnos)      
    
            
        case "2": 
            listar_alumnos(diccionario_alumnos)
            
    
            
        case "3": 
            buscar_alumno(diccionario_alumnos)
        
            
        case "4": 
            modificar_alumno(diccionario_alumnos)
            guardar_alumnos(diccionario_alumnos)
        
            
        case "5": 
            eliminar_alumno(diccionario_alumnos)
            guardar_alumnos(diccionario_alumnos)
        
            
        case "6": 
            mostrar_estadisticas(diccionario_alumnos)
        
        
        case "7":
            print("Saliendo del sistema...")
            display_menu = True
                    
        case _:
            print("Opción inválida. Intente de nuevo.")
                    

        