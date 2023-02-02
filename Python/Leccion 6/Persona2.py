class Persona2:
    def __init__(self, nombre, apellido, edad):  # Esta encapsulado
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalles(self):
        print(f'Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}')

    # Método Getter
    @property  # decorador
    def nombre(self):
        print('Estamos utilizando el método get')
        return self._nombre

    # Método Setter
    @nombre.setter
    def nombre(self, nombre):
        print('Estamos utilizando el método set')
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

# metodo destructor
    def __del__(self):
        print(f'Persona2: {self._nombre} {self._apellido} {self._edad}')


if __name__ == '__main__': # solo muestra el codigo de la clase Persona2
    # creamos el objeto persona 1 para instanciar la clase Persona2 y le pasamos los parametros de los atributos de la clase
    persona1 = Persona2('Ariel', 'Betancud', 41)
    print(persona1.nombre)  # llamamos al método getter y lo mostramos

    persona1.nombre = 'Juan Pedro'  # modificamos el parametro por el metodo set. Llamamos el método setter
    print(persona1.nombre)  # llamamos al método getter
    print(persona1.mostrar_detalles())  # Llamamos el método mostrar_detalle
    # Atributo read-only (solo lectura) sería la edad porque no tiene el método set para modificarla
    print(persona1.edad) # se muestra la edad por el metodo getter

    persona1.edad = 40 # da error si no tenemos definido el metodo setter
    persona1._edad = 40 # permite modificar pero no es una sintaxis recomendada
    # print(persona2._nombre)   # sintaxis no recomendada

    # Tarea crear tres objetos más, utilizando los métodos getter and setter
    # para modificar, y mostrar los cambios con el método mostrar_detalles

    # Objeto número uno de la tarea
    # creamos el objeto persona 2
    persona2 = Persona2('Flor', 'Romer', 23)
    # mostramos el metodo get
    print(persona2.nombre)
    print(persona2.apellido)
    print(persona2.edad)
    # modificamos los atributos por medio del metodo set
    persona2.nombre = 'Florencia'
    persona2.apellido = 'Romero'
    persona2.edad = 22
    # mostramos el metodo mostrar_detalle
    print(persona2.mostrar_detalles())

    # Objeto número dos de la tarea
    persona3 = Persona2('Caro', 'Felisa', 21)
    print(persona3.nombre)
    print(persona3.apellido)
    print(persona3.edad)
    persona3.nombre = 'Carolina'
    persona3.apellido = 'Felix'
    persona3.edad = 31
    print(persona3.mostrar_detalles())

    # Objeto número tres de la tarea
    persona4 = Persona2('Naty', 'Lucer', 35)
    print(persona4.nombre)
    print(persona4.apellido)
    print(persona4.edad)
    persona4.nombre = 'Natalia'
    persona4.apellido = 'Lucero'
    persona4.edad = 33
    print(persona4.mostrar_detalles())

# Comprobacion del modulo principal en ejecucion: nos dice desde donde se esta ejecutando el codigo.
    print(__name__)

