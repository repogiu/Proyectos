class Persona:  # creacion de una clase
    # identacion
    # pass
    def __init__(self, nombre, apellido, edad):  # se lo llama metodo init Dunder, enviamos los argumentos
        # se respeta la tabulacion para estar dentro del metodo
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    # def __init__(self): # se lo llama metodo init Dunder
    # self.nombre = "Giuliana"
    # self.apellido = "Diaz"
    # self.edad = 37

    def mostrar_detalle(self):
        print(
            f'Persona: {self.nombre} {self.apellido} {self.edad}')  # asi accedemos a los atributos de otro metodo de la misma clase


# Creacion del objeto 1
# persona1 = Persona()

persona1 = Persona("Giuliana", "Diaz", "37")

print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

print(type(Persona))

# Creacion del objeto 2
persona2 = Persona("Gael", "Diaz", "4")
print(f'El objeto 2 de la clase Persona es: {persona2.nombre} {persona2.apellido} y su edad es: {persona2.edad} años')

# Modificamos atributos del objeto 1
persona1.nombre = "Paola"
persona1.apellido = "Luna"
persona1.edad = "37"
print(
    f'El objeto 1 modificado de la clase Persona es: {persona1.nombre} {persona1.apellido} y su edad es: {persona1.edad} años')

# Los metodos son: el comportamiento que van a tener los objetos (acciones)
# Otra forma de acceder a los atributos de un metodo_  Llamamos a los objetos desde el metodo mostrar_detalle()
persona1.mostrar_detalle()
persona2.mostrar_detalle()
