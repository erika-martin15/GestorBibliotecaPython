# Importamos las clases Libro y Socio.
from libro import Libro
from socio import Socio

# Cargamos TODOS los libros
def cargar_libros(archivo):
    libros = [] # Creamos una lista vacía para los libros del txt.
    # Vamos a abrir el archivo SOLO para lectura, ya que es la función que vamos a utilizar para cargar los libros al principio del programa.
    with open(archivo, 'r', encoding='utf-8') as f:
        # Iteramos línea a línea el documento.
        for linea in f:
            frases = linea.strip().split(';') # Quitamos los espacios en blanco del final y proncipio de la línea. Además, indicamos que las partes están divididas con un punto y coma. "Frases" será una lista que contenga los elementos (en este caso, de Libros).
            # Creamos el Libro con cada campo necesario.
            libro = Libro( # Accedemos a los elementos según su posición en la lista.
                frases[0],  # Código
                frases[1],  # Título
                frases[2],  # Autor
                frases[3],  # Fecha de publicación
                frases[4],  # Número de páginas
                frases[5],  # Género
                frases[6],  # ISBN
                frases[7],  # Editorial
                frases[8]  # Código del socio (si está prestado)
            )
            # Vamos a añadir el nuevo libro que hemos creado a la lista.
            libros.append(libro)
            # Avisamos al usuario de cuántos libros hemos cargado, para responder mejor al ejercicio.

        print(f'Se han cargado {len(libros)} libros.') # 'len' nos dirá la cantidad de libros.
        return libros

# Haremos lo mismo que antes pero para los socios.
def cargar_socios(archivo):
    socios = []
    with open(archivo, 'r', encoding='utf-8') as f:
        for linea in f:
            frases = linea.strip().split(';')
            socio = Socio(
                frases[0],  # Código
                frases[1],  # Nombre
                frases[2],  # Apellidos
                frases[3],  # DNI
                frases[4],  # Correo electrónico
                frases[5],  # Teléfono
                frases[6],  # Dirección
                frases[7],  # Fecha de cumpleaños
                frases[8]  # Código del libro prestado (si existe)
            )
            socios.append(socio)
        print(f'Se han cargado {len(socios)} socios.')
        return socios

# ------- FUNCIONES QUE GUARDAN DATOS ----------
# Escribimos los LIBROS.
def guardar_libros(libros):
    # Esta vez, como queremos ESCRIBIR en el fichero, utilizaremos la 'w' de 'write' en vez de la 'r' de 'read'.
    # Otra opción podría haber sido crear una función de escritura y lectura, pero he decidido crear dos para que sea más sencillo de entender.
    archivo = open('ficheros/libros.txt', 'w', encoding='utf-8')

    # Recorremos todos los libros
    for libro in libros:
        # Creamos una línea con todos los datos, separándolos por punto comas, tal y como están en el archivo original.
        linea = libro.codigo + ';'
        linea = linea + libro.titulo + ";"
        linea = linea + libro.autor + ";"
        linea = linea + libro.fecha_publicacion + ";"
        linea = linea + libro.num_paginas + ";"
        linea = linea + libro.genero + ";"
        linea = linea + libro.isbn + ";"
        linea = linea + libro.editorial + ";"
        linea = linea + libro.codigo_socio
        linea = linea + "\n" # Añadimos un salto de línea al final, para respetar el formato.

        # Escribimos la línea en el archivo.
        archivo.write(linea)

    archivo.close() # Cerramos el archivo.

# Escribimos los SOCIOS
def guardar_socios(socios):
    archivo = open('ficheros/socios.txt', 'w', encoding='utf-8')

    for socio in socios:
        linea = socio.codigo + ";"
        linea = linea + socio.nombre + ";"
        linea = linea + socio.apellidos + ";"
        linea = linea + socio.dni + ";"
        linea = linea + socio.email + ";"
        linea = linea + socio.telefono + ";"
        linea = linea + socio.direccion + ";"
        linea = linea + socio.fecha_cumpleanios + ";"
        linea = linea + socio.codigo_libro
        linea = linea + "\n"
        archivo.write(linea)

    archivo.close()

# ------- FUNCIONES QUE MUESTRAN DATOS ----------
# Mostramos TODOS los socios.
def mostrar_socios(socios):
    # Lo visualizaremos en modo de tabla.
    print('\n' + '='*90)
    print(' '*35 + 'LISTA DE SOCIOS')
    print('='*90)
    # Este será el encabezado de dicha tabla. Le añadiremos más espacio en el nombre y el correo electrónico, ya que ocupan más espacio.
    print(f"{'Código':<10} {'Nombre completo':<30} {'Email':<30} {'Tiene libro':<15}")
    print("-"*90)

    for socio in socios:
        nombre_completo = f"{socio.nombre} {socio.apellidos}"
        # Si el apartado de 'codigo_libro' NO está vacío, la columna 'Tiene Libro' mostrará un 'Sí'.
        if socio.codigo_libro.strip() != "":
            tiene_libro = "Sí"
        else:
            tiene_libro = "No"
        # Imprimimos los datos de los socios, con el mismo espacio que le hemos dado a cada dato en el encabezado.
        print(f"{socio.codigo:<10} {nombre_completo:<30} {socio.email:<30} {tiene_libro:<15}")

    # Cerramos la tabla.
    print("="*90)

# Mostramos TODOS los libros.
def mostrar_libros(libros, socios):
    print('\n' + '='*130)
    print(' '*55 + 'Libros')
    print('='*130)

    print(f'{'Código':<8} {'Titulo':<50} {'Autor':<30} {'Estado':<35}')
    print('-'*130)

    for libro in libros:
        if libro.codigo_socio.strip() == '': # Si no tiene código de socio, es que el libro está disponible para prestarlo.
            estado = 'Disponible'
        else:
            nombre_socio = 'No determinado' # Inicializamos la variable con un dato provisional.
            for socio in socios:
                if socio.codigo == libro.codigo_socio: # Si el código de un socio es el mismo que el del libro, logramos su nombre completo.
                    nombre_socio = f'{socio.nombre} {socio.apellidos}'
                    break
            estado = f'Prestado a {nombre_socio}'

        print(f'{libro.codigo:<8} {libro.titulo:<50} {libro.autor:<30} {estado:<35}')

    print('='*130)

# Mostramos los libros DISPONIBLES
def mostrar_libros_disponibles(libros):
    print('\n' + '='*100)
    print(' '*35 + 'LIBROS DISPONIBLES')
    print('='*100)

    print(f'{'Código':<8} {'Título':<50} {'Autor':<30}')
    print('-'*100)

    libros_disponibles = 0 # Creamos una variable que nos sirva como contador de los libros que están disponibles.
    for libro in libros:
        if libro.codigo_socio.strip() == '': # Si no tiene código de socio, lo consideramos disponible y lo imprimimos.
            print(f"{libro.codigo:<8} {libro.titulo:<50} {libro.autor:<30}")
            libros_disponibles = libros_disponibles + 1 # Sumamos al contador.

    if libros_disponibles == 0:
        print('No hay libros disponibles.')

    print('='*100)

# Mostrar el préstamo ACTIVO que tiene cada socio.
def mostrar_prestamo_socio(libros, socios):
    print('\n' + '=' * 100)
    print(' ' * 30 + 'SOCIOS CON LIBROS PRESTADOS')
    print('=' * 100)

    print(f"{'Código':<8} {'Nombre':<30} {'Libro prestado':<50}")
    print('-'*100)

    # Haremos lo mismo que hemos hecho al mostrar los libros disponibles. Cogeremos un contador y buscaremos que un código de libro coincida con el código de libro del usuario.
    socios_prestamos = 0
    for socio in socios:
        if socio.codigo_libro.strip() != '':
            titulo_libro = 'Titulo desconocido'

            for libro in libros:
                if libro.codigo == socio.codigo_libro:
                    titulo_libro = libro.titulo
                    break

            nombre_socio = f'{socio.nombre} {socio.apellidos}'

            print(f"{socio.codigo:<8} {nombre_socio:<30} {titulo_libro:<50}")
            socios_prestamos = socios_prestamos + 1

    if socios_prestamos == 0:
        print('No hay prestamos activos en este momento.')

    print('='*100)

# ------- FUNCIONES QUE REALIZAN BÚSQUEDAS ----------
# Buscamos un libro por su TÍTULO
def buscar_libro(libros):
    usuario_titulo = (input('Introduce la palabra que quieres buscar: ')).lower() # Preguntamos al usuario por la palabra que quiera buscar y la convertimos a minúsculas.

    print("\n" + "="*100)
    print(" "*35 + "RESULTADOS DE LA BÚSQUEDA")
    print("="*100)

    print(f"{'Código':<8} {'Título':<50} {'Autor':<30}")
    print("-" * 100)

    titulo_encontrado = 0
    for libro in libros:
        titulo_formato = libro.titulo.lower() # Convertimos también a minúsculas el título del libro del txt, para facilitar la búsqueda.

        if usuario_titulo in titulo_formato:
            print(f"{libro.codigo:<8} {libro.titulo:<50} {libro.autor:<30}")
            titulo_encontrado = titulo_encontrado + 1

    if titulo_encontrado == 0:
        print('No se han encontrado libros que contengan esa palabra en el título.')
    else:
        print(f'Se han encontrado {titulo_encontrado} libro/os.') # Decimos qué cantidad de libros con esa palabra hemos encontrado.

    print('='*100)

# ------- FUNCIONES QUE GESTIONAN LIBROS ----------
# PRESTAMOS un libro a un socio.
def prestar_libro(libros, socios):
    usuario_titulo = (input('Introduce el título del libro a prestar: ')).lower()
    usuario_dni = input("Introduce el DNI del socio: ")

    # Buscamos el libro con el título que ha introducido el usuario.
    libro_encontrado = ''
    for libro in libros:
        titulo_libro = libro.titulo.lower()
        if usuario_titulo in titulo_libro: # Si lo encontramos, le damos el valor del título a la variable 'libro_encontrado'.
            libro_encontrado = libro
            break

    # Buscamos al socio por su DNI.
    socio_encontrado = ''
    for socio in socios:
        if socio.dni == usuario_dni:
            socio_encontrado = socio
            break

    # Comenzamos con las validaciones.
    if socio_encontrado == '':
        print('No se encontró ningún socio con ese DNI.')
        return

    if libro_encontrado == '':
        print('No se encontró ningún libro con ese título.')
        return

    if libro_encontrado.codigo_socio.strip() != '':
        print('El libro ya ha sido prestado a otra persona.')
        return

    if socio_encontrado.codigo_libro.strip() != '':
        print('El usuario ya tiene un préstamo anterior sin devolver.')
        return

    # Una vez hechas las comprobaciones, asignamos el libro al socio.
    libro_encontrado.codigo_socio = socio_encontrado.codigo
    socio_encontrado.codigo_libro = libro_encontrado.codigo

    print(f'{libro_encontrado.titulo} prestado correctamente a {socio_encontrado.nombre} {socio_encontrado.apellidos}.')

def devolver_libro(libros, socios):
    usuario_titulo = (input('Introduce el título del libro a devolver: ')).lower()

    libro_encontrado = ''
    for libro in libros:
        titulo_libro = libro.titulo.lower()
        if usuario_titulo in titulo_libro:
            libro_encontrado = libro
            break

    # Realizamos las validaciones.
    if libro_encontrado == '':
        print('No se encontró ningún libro con ese título.')
        return

    # Damos a la variable el valor del código del socio que tenía el libro prestado.
    codigo_socio_devolucion = libro_encontrado.codigo_socio.strip()

    if codigo_socio_devolucion == '':
        print('El libro está disponible, no había sido prestado.')
        return

    # Quitamos el préstamo al socio.
    libro_encontrado.codigo_socio = ''
    for socio in socios:
        if socio.codigo == codigo_socio_devolucion:
            socio.codigo_libro = ''
            break

    print(f'{libro_encontrado.titulo} devuelto a la biblioteca. Devolución realizada por {codigo_socio_devolucion.nombre} {codigo_socio_devolucion.apellidos}.')

# ------- FUNCIONES QUE GESTIONAN USUARIOS ----------

def anadir_socio(socios):
    print('---- AÑADIR UN NUEVO SOCIO ----')
    nuevo_codigo = (input('Código del socio: ')).strip()
    nuevo_nombre = (input('Nombre: ')).strip()
    nuevo_apellidos = (input('Apellidos: ')).strip()
    nuevo_dni = (input('DNI: ')).strip()
    nuevo_email = (input('Email: ')).strip()
    nuevo_telefono = (input('Telefono: ')).strip()
    nuevo_direccion = (input('Dirección: ')).strip()
    nuevo_fecha_cumple = (input('Fecha de cumpleaños (AAAA-MM-DD): ')).strip()

    # Realizamos las comprobaciones.
    if nuevo_codigo == '':
        print('No se puede dejar el campo de código vacío.')
        return

    if nuevo_nombre == '':
        print('No se puede dejar el campo de nombre vacío.')
        return

    if nuevo_apellidos == '':
        print('No se puede dejar el campo de apellidos vacío.')
        return

    if nuevo_dni == '':
        print('No se puede dejar el campo de DNI vacío.')
        return
    for socio in socios:
        if socio.dni == nuevo_dni:
            print('Ya existe un socio con ese número de identificación (DNI)')

    if nuevo_email == '':
        print('No se puede dejar el campo de email vacío.')
        return
    if '@' not in nuevo_email: # Si no detecta una arroba en el correo electrónico, lo dará por no válido.
        print('Formato de email incorrecto. El email debe contener un arroba(@)')

    if len(nuevo_fecha_cumple) != 10:
        print('Número demasiado corto. La fecha debe tener el formato AAAA-MM-DD.')
        return
    if nuevo_fecha_cumple[4] != '-' or nuevo_fecha_cumple[7] != '-':
        print('Formato erróneo. La fecha debe tener el formato AAAA-MM-DD.')

    # Creamos el nuevo socio
    nuevo_socio = Socio(nuevo_codigo, nuevo_nombre, nuevo_apellidos, nuevo_dni, nuevo_email, nuevo_telefono, nuevo_direccion, nuevo_fecha_cumple, "")
    socios.append(nuevo_socio) # Lo añadimos a la lista.

    print('Socio añadido correctamente.')