# class Persona(Object): La clase persona hereda de la clase object
class Persona:  # Esta clase hereda de la clase Object, se hace automaticamente
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

# Metodo dunder_str_(): es un metodo de la clase Object
    def __str__(self):  # Override = sobreescribir los atributos, lo que va a mostrar va a ser de tipo cadena
        return f'Persona:  [ Nombre: {self._nombre}, Edad: {self._edad} ]'


class Empleado(Persona):  # Esta clase es hija de la clase persona
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad) # aqui sobreescribimo el metodo init de la clase padre. para hacer uso de los atributos de la clase persona usamos el metodo constructor super() y llamamos al metodo init de la clase persona
        self._sueldo = sueldo

    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self, sueldo):
        self._sueldo = sueldo

    def __str__(self):
        return f'Empleado: [ Sueldo: {self._sueldo}] {super().__str__()}' # aqui sobreescribimos el metodo str de la clase persona

# Creacion de objetos
emplado1 = Empleado('Ariel', 40, 75000)
# Mostramos el metodo get
print(emplado1.nombre)
print(emplado1.edad)
print(emplado1.sueldo)

# Tarea: encapsular los atributos y agregar los métodos getters and setters
# Crear otro objeto, pasar los datos para nombre, edad y sueldo
# Mostrar estos datos, luego modificar y mostrar nuevamente

empleado2 = Empleado('Liliana', 38, 70000)
print(empleado2.nombre)
print(empleado2.edad)
print(empleado2.sueldo)
empleado2.nombre = 'Natalia'
empleado2.edad = 35
empleado2.sueldo = 75000
print(empleado2.nombre)
print(empleado2.edad)
print(empleado2.sueldo)