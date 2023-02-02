class Persona:  # creacion de una clase
    # identacion
    # pass
    def __init__(self, nombre, apellido, edad, *args, **kwargs):  # se lo llama metodo init Dunder, enviamos los argumentos
        # se respeta la tabulacion para estar dentro del metodo
        self.nombre = nombre
        self.apellido = apellido
        self._dni = dni # atributo encapsulado de manera sugerida
        self.edad = edad
        self.args = args # primero va la tupla y luego el diccionario
        self.kwargs = kwargs

    # def __init__(self): # se lo llama metodo init Dunder
    # self.nombre = "Giuliana"
    # self.apellido = "Diaz"
    # self.edad = 37


    def mostrar_detalle(self):  # self es igual a this en Java
            print( # asi accedemos a los atributos de otro metodo de la misma clase
                f'La clase Persona tiene los siguientes datos: {self.nombre} {self.apellido} {self._dni} {self._dni} {self.edad}, la dirección es: {self.args}, los datos importantes son: {self.wkargs}')

# Fuera de la identacion de la  clase creamos las instancias de la clase con objetos
# Creacion del objeto 1
# persona1 = Persona()

persona1 = Persona("Giuliana", "Diaz", 31646497, 37)

print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

print(type(Persona))

# Creacion del objeto 2
persona2 = Persona("Gael", "Diaz", 57102647, 4)
print(f'El objeto 2 de la clase Persona es: {persona2.nombre} {persona2.apellido} y su edad es: {persona2.edad} años')

# Modificamos atributos del objeto 1
persona1.nombre = "Paola"
persona1.apellido = "Luna"
persona1.edad = "37"
print(
    f'El objeto 1 modificado de la clase Persona es: {persona1.nombre} {persona1.apellido} y su edad es: {persona1.edad} años')

# Los metodos son: el comportamiento que van a tener los objetos (acciones)
# Otra forma de acceder a los atributos de un metodo_  Llamamos a los objetos desde el metodo mostrar_detalle()
persona1.mostrar_detalle() # La referencia en este caso se pasa de manera automatica
persona2.mostrar_detalle()

# ya no se usa
Persona.mostrar_detalle(persona1) # Debemos pasarle una referencia para el self o dará error

# Creamos atributos desde un objeto, sin que este atributo este cargado
# en el metodo init, no comparte ese atributo con los demas objetos
persona1.telefono = '44445555289'
print(persona1.telefono)
print(f'Telefono de persona 1: {persona1.nombre} {persona1.telefono}') # Hemos creado un atributo de un objeto

# print(persona2.telefono) el objeto persona2 no tiene este atributo, da error

persona3 = Persona('Romeo', 'Romero', 35789456, 22, 'Teléfono', '2614445557', 'Calle Lopez', 823, 'Manzana', 77, 'Casa', 18, Altura=1.83, Peso=105, CFavorito='Azul', Auto='Citroen', Modelo=2021)
persona3.mostrar_detalle()

# print(persona3._dni) # esto no se debe utilizar(esta encapsulado), esto dice que desconocemos python
# persona3.__nombre # Esta totalmente encapsulado
