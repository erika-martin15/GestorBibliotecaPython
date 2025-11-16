class Socio:
    def __init__(self, codigo, nombre, apellidos, dni, email, telefono, direccion, fecha_cumpleanios, codigo_libro):
        self.codigo = codigo
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
        self.fecha_cumpleanios = fecha_cumpleanios # He añadido la fecha de cumpleaños pensando en una futura funcionalidad. Esta podría ser que,
        # en el día del cumpleaños del socio, en caso de que pase a coger un libro prestado avise por consola al usuario de que es su cumpleaños.
        self.codigo_libro = codigo_libro