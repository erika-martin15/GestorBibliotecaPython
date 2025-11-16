# Importamos todas las funciones que vamos a utilizar. Para no crear un archivo 'main' demasiado largo, he creado un segundo documento que las albergue todas.
from funciones import cargar_libros, cargar_socios, mostrar_libros, mostrar_socios, mostrar_libros_disponibles, \
    buscar_libro, prestar_libro, devolver_libro, mostrar_prestamo_socio, anadir_socio, guardar_libros, guardar_socios


# Creamos una función con las opciones del programa. Lo formatearemos para que tenga la apariencia más agradable para el usuario.
def mostrar_menu():
    print('\n' + '-'*60) # Repetirá el guión 60 veces.
    print('GESTOR DE BIBLIOTECA')
    print('-'*60)
    print('0. Mostrar todos los libros')
    print('1. Mostrar todos los libros DISPONIBLES')
    print('2. Buscar libro por título')
    print('3. Prestar un libro')
    print('4. Devolver un libro')
    print('5. Mostrar socios con un préstamo activo')
    print('6. Mostrar todos los socios')
    print('7. Añadir un nuevo socio')
    print('8. Cerrar sesión')
    print('-'*60)

# El programa principal. Solo se ejecutará en el 'main'.
if __name__ == '__main__':
    # Cargamos los archivos de 'libros' y 'socios'.
    libros = cargar_libros('ficheros/libros.txt')
    socios = cargar_socios('ficheros/socios.txt')

    # Entramos en un bucle infinito hasta que el usuario le dé al botón de 'Salir' (8).
    while True:
        mostrar_menu() # Cargamos la función que muestra el menú.
        opcion = input("Escoge una opción: ") # Solicitamos al usuario su elección.

        if opcion == '0':
            mostrar_libros(libros, socios)
        elif opcion == '1':
            mostrar_libros_disponibles(libros)
        elif opcion == '2':
            buscar_libro(libros)
        elif opcion == '3':
            prestar_libro(libros, socios)
        elif opcion == '4':
            devolver_libro(libros, socios)
        elif opcion == '5':
            mostrar_prestamo_socio(libros, socios)
        elif opcion == '6':
            mostrar_socios(socios)
        elif opcion == '7':
            anadir_socio(socios)
        elif opcion == '8': # Si el usuario procede a salir, guardaremos en los archivos de texto los cambios realizados.
            print("¡Gracias por usar nuestro servicio!")
            guardar_libros(libros)
            guardar_socios(socios)
            print('Tus datos han sido guardados correctamente.')
            print('Cerrando el programa...')
            break # Salimos del programa.
        else:
            # Si el usuario no introduce un número entre el 0 y el 8, se le informará.
            print("Opción no válida.")