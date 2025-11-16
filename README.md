# Gestor de Biblioteca en Python

## Descripción
Este proyecto consiste en una aplicación de consola, sin interfáz gráfica, que permite gestionar los libros y socios de una biblioteca. El sistema permite cargar, almacenar y editar datos, como pueden ser la gestión de los préstamos y devoluciones. Todos los datos se guardan y leen desde archivos de texto.

## Requisitos
- Python 3.13.7 instalado
- Carpeta llamada `ficheros` con los archivos `libros.txt` y `socios.txt` en su interior. Debe estar en el mismo lugar en el que se encuentran los scripts.

## Instalación y ejecución
1. Descarga todos los archivos del proyecto: el programa principal (`main.py`), así como los módulos `libro.py`, `socio.py` y `funciones.py`.
2. Crea una carpeta llamada `ficheros` en la raíz del proyecto y añade ahí los archivos `libros.txt` y `socios.txt`.
3. Ejecuta el archivo principal con:
   ```bash
   python main.py
   ```

## Estructura del proyecto
- `main.py`: Programa principal que contiene el menú.
- `libro.py`: Definición de la clase Libro.
- `socio.py`: Definición de la clase Socio
- `funciones.py`: Funciones para cargar, guardar y manipular libros y socios.
- `ficheros/libros.txt` y `ficheros/socios.txt`: Archivos de datos de la biblioteca.

## Funcionamiento
Cuando inicias el programa, verás un menú con varias opciones. Puedes:

- Mostrar todos los libros
- Consultar los libros disponibles para préstamo
- Buscar libros por título
- Prestar libros a socios
- Registrar la devolución de un libro
- Mostrar socios y sus datos
- Añadir nuevos socios
- Visualizar qué socios tienen préstamos activos
- Salir (guardando los datos que acabas de cambiar en los archivos de texto)

## Autor
Proyecto realizado por Erika Martín Rivas para la clase de Python.

## Contacto
Si tienes cualquier duda o sugerencia, puedes encontrarme en el correo electrónico [ikdhe@plaiaundi.net].
