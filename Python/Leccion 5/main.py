# Comenzamos con Funciones
# mi_funcion() # No se puede llamar antes de definir a una función
# Definimos una función
def mi_funcion(): # Para identificar a la función utilizamos paréntesis
    print('Saludos a todos lo alumnos de la Tecnicatura')

mi_funcion() # Estamos llamando a la función
mi_funcion() # Se puede llamar a una función N cantidad de veces

# Desempaquetado de listas o list Unpacking
def show(name, lastName):
    print(name+' '+lastName)

person = ["Ariel", "Betancud"] # definimos una lista
show(person[0], person[1]) # Pasamos uno por uno los datos de la lista a la función
show(*person)

person2 = ("Osvaldo", "Giordanini") # desempaquetamos a través de una tupla
show(*person2)

person3 = {"lastName": "Lucero", "name": "Natalia"} # Diccionario
show(**person3) # dos asterisco uno para clave y otro para valor

######################################################################################################
# Repaso for-else
numbers = [1, 2, 3, 4, 5] # Aun con el la lista vacia se va a ejecutar el else
for n in numbers:
    print(n)
    if n == 3:
        break # Esta es la unica manera para que no se ejecute el else
else:
    print('Proceso finalizado')

#######################################################################################################
# List comprehension, lista de comprensión
lista = ["Paolo", "Rodrigo", "LuPe", "Pepe"]
comprension = [p for p in lista if p[2] == 'P'] # regresa LuPe
comprension = [p for p in lista if p[0] == 'P'] # regresa Paolo y Pepe
print(comprension)

diccionario = [{"name": "Quilmes", "country": "Arg"},
           {"name": "Corona", "country": "Mx"},
           {"name": "Stella Artois", "country": "Belgium"},
           ]
Arg = [b for b in diccionario if b["country"] == "Arg"]
print(Arg)
print(diccionario)

################################################################################
# Paso de Argumentos (funciones)
def mi_funcion2(name, lastName): # estos son parametros
    print("Saludos a todos lo que ven a través del canal de YouTube")
    print(f'Nombre: {name}, Apellido: {lastName}')

# Llamadas
mi_funcion2('Jorge', 'Lucero') # le pasamos los argumentos a la fx
mi_funcion2('Ariel', 'Betancud')
mi_funcion2('Analia', 'Pedrosa')

# La palabra return en funciones
# Creamos una función para sumar
def sumar(a, b):
    return a + b

# resultado = sumar(78, 22)
# print(f'El resultado de la suma es: {resultado}')
print(f'El resultado de la suma es: {sumar(55, 45)}')

# Valores por default en Argumentos
def sumar2(a = 0, b = 0): # Le damos un valor por default
    return a + b
resultado = sumar2()
print(f'Resultado de la suma: {resultado}')
print(f'Resultado de la suma: {sumar2(22, 66)}')

# Argumentos, variables  en funciones
def listarNombres(*nombres): # Normalmente se utiliza: *args, cuando no sabemos cuantos argumentos vamos a recibir
    for nombre in nombres: # Se va a convertir en una tupla que no puede ser modificada
        print(nombre)
listarNombres('Lucas', 'José', 'Claudia', 'Rosa', 'María')
listarNombres('Marcos', 'Daniel', 'Romina', 'Pepe', 'Marcela', 'Carlos')

#########################################################
# Funciones con diccionario

def listarTerminos(**terminos): # Lo mas utilizado es **kwargs para recibir los argumentos
    for llave, valor in terminos.items(): # kwargs significa: key word argument
        print(f'{llave} : {valor}')

# llamamos a la funcion
listarTerminos() # No recibe nada, nada se va a mostrar
listarTerminos(IDE='Integrated Development Enviroment', PK='Primary Key') # la llave no hace falta comillas simples
listarTerminos(Nombre='Leonel Messi')

# Lista de elementos con funciones (convertir)
def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)
nombres2 = ['Tito', 'Pedro', 'Carlos']
desplegarNombres(nombres2)
desplegarNombres('Carla')

# desplegarNombres(10, 11) # No es un objeto iterable
desplegarNombres((10, 11)) # La convertimos a una tupla con doble parentesis, en un solo elemento no olvidar la coma ((10,))
desplegarNombres([22, 55]) # La convertimos en una lista

# Funciones Recursivas con factorial ( necesita un caso base y un caso recursivo)
def factorial(numero):
    if numero == 1: # Caso Base
        return 1
    else:
        return numero * factorial(numero-1) # Caso Recursivo
# En codigo duro
numeroFactorial = int(input('Digite el numero para calcular el factorial: '))
resultado = factorial(numeroFactorial)
print(f'El factorial del número {numeroFactorial} es: {resultado}')

