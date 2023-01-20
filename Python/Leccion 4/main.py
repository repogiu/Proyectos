# lista = Ariel , Liliana, Natalia, Osvaldo
# Colecciones en Python

# Las listas es lo que se conoce en otros lenguajes como arreglos o vectores
# Sintaxis
nombres = ['Naty', 'Osvaldo', 'Lily', 'Ariel']
print(nombres)
print(nombres[0:2]) # Solo muestra los dos primeros elementos, el indice 0, 1 pero no el indice 2
# ir del inicio de la lista al indice (sin incluirlo)
print(nombres[ :3]) # Indices a mostrar 0, 1, 2
# Desde el indice indicado hasta el final
print(nombres[1: ])
# nos muestra el ultimo elemento si no conocemos
print(nombres[-1])
# nos muestra el penultimo elemento
print(nombres[-2])

# Modificamos un valor
nombres[2] = 'Liliana'
nombres[0] = 'Natalia'
print(nombres)

# Iterar una lista: muestra nombre por nombre
for nombre in nombres: # nombre es singular, la lista es plural
    print(nombre)
else: # al terminar de recorrer los elementos de la lista imprime
    print('Se acabaron los elementos de la lista')

# Preguntamos cuantos elementos tiene con la funcion len
print(len(nombres)) # le pasamos como parametro la lista

# Agregamos un elemento con el operador punto que permite acceder a la funcion append para ingresar Marcelo a la lista, que se agrega al ultimo..
# una lista puede tener diferentes tipos de datos
nombres.append('Marcelo')
nombres.append([1, 2, 3]) # ingresa un lista dentro de la lista nombre
nombres.append(True) # agregamos un booleano
nombres.append(10.45) # agreamos un flotante
nombres.append([4, 5]) # agregamos otra lista
nombres.append(7) # agregamos un entero
print(nombres)

# Insertar un elemento en un indice especifico con la funcion insert
nombres.insert(1, 'Alberto') # alberto es el objeto
print(nombres)
nombres.insert(3, 'Debora')
print(nombres)

# Eliminamos un elemento con la funcion remove
nombres.remove('Alberto')
print(nombres)

# Eliminar el ùltimo elemento de la lista
nombres.pop()
print(nombres)

# Eliminar un indice especifico
del nombres[2] # del significa delete (eliminar)
print(nombres)

# Eliminar, borrar o limpiar todos los elementos
nombres.clear()
print(nombres)

# Eliminar la lista
del nombres
# print(nombres) # Aquí nos mostrará un error porque ya fue eliminada

##########################################################################
# Definimos una tupla
cocina = ('cuchara', 'cuchillo', 'tenedor')
print(len(cocina))

# Acceder a un elemento, para esto utilizamos corchetes no parentesis
print(cocina[0])
# mostrar de manera inversa
print(cocina[-1])

# Acceder a un rango
print(cocina[0:2]) # nos muestra los dos primeros numeros

# Esto no es una tupla
verduras = ('papa')

# Ejemplo
verduras = ('papa',) # Una tupla necesita aunque sea de un elemento: la coma
# de lo contrario solo seria un tipo str cadena

# Recorremos los elementos de la tupla cocina
for cocinar in cocina: # Print esta usando \n para saltos de líneas
    print(cocinar) # sin salto de linea
    print(cocinar, end=' ') # Usamos end= para eliminar los saltos de líneas

# conversion de tupla a lista y de lista a tupla para modificar algun elemento de la tupla
cocinaLista = list(cocina) # convertimos a lista
cocinaLista[0] = 'Plato'   # modificamos
cocina = tuple(cocinaLista) # convertimos a tupla
print('\n', cocina)

# esto es para eliminar una tupla
#del cocina
#print(cocina)

########################################################################
# Tipo set: coleccion sin orden sin indice
planetas = {'Marte', 'Júpiter', 'Venus'}
print(len(planetas)) # Usamos la función len = length significa largo

# Preguntamos si un elemento existe dentro de set
print('Júpiter' in planetas)
print('Júpiter' not in planetas)

# Agregar un elemento
planetas.add('Tierra') # add es una función
print(planetas)

# Eliminar elementos, puede arrojar un error si el elemento no existe
planetas.remove('Júpiter') # Esta función ante un mal ingreso u inexistencia del elemento da error
print(planetas)
planetas.discard('tierra') # Esta función elimina si esta bien escrito, si esta mal escrito no nos presenta ningun error pero no borra el elemento
print(planetas)

# Limpiar set o conjunto vacio
planetas.clear()
print(planetas)

# Eliminar set o conjunto
del planetas
#print(planetas) # al eliminar nos muestra fun error

#######################################################################

# 'Maradona':10 Un diccionario esta compuesto por dos elementos
# UNA LLAVE Y UN VALOR
# dict(key,value)
diccionario = {
    'IDE': 'Integrated Development Environment',
    'POO': 'Programación Orientada a Objetos',
    'SABD': 'Sistema de Administración de Base de Datos'
}
# Verificar la cantidad de elementos del diccionario
print(len(diccionario))
print(diccionario)

# Acceder a un diccionario con la llave(key)
print(diccionario['IDE'])

# Otra forma de recuperar un elemento con la funcion get
print(diccionario.get('POO'))
print(diccionario.get('SABD'))

# Modificamos elementos
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario)

# Como recorrer los elementos
for termino in diccionario: # se accede solo las llaves
    print(termino)

# Otras maneras de acceder a un diccionario
for termino in diccionario.keys(): # Estamos usando una función
    print(termino) # Muestra solo las llaves

# Accedemos al diccionario completo, necesitamos una función items()
for termino, valor in diccionario.items():
    print(termino, valor)

# Muestra solo los valores usando la funcion values()
for valor in diccionario.values():
    print(valor)

# Comprobar la existencia de algun elemento
print('IDE' in diccionario) # devuelve un booleano

# Comprobar la inexistencia de algun elemento
print('IDE' not in diccionario) # devuelve un booleano

# Agregar un elemento, se agrega al ultimo
# no es posible agregar llaves duplicadas, si agregamos una llave existente sobreescribe con el nuevo valor
diccionario['PK'] = 'Primary key'
print(diccionario)

# Eliminar un elemento
diccionario.pop('SABD')
print(diccionario)

# Vaciar un diccionario
diccionario.clear()
print(diccionario)

# Eliminar diccionario
del diccionario # el diccionario se borro
print(diccionario) # da error porque el diccionario desaparecio
########################################################################

# Concatenamos listas
lista1 = [1, 2, 3, 1]
lista2 = [4, 5, 6, 1]
lista3 = lista1+lista2 # Concatenamos
print(lista3)

# Función para agregar varios elementos a una lista
lista3.extend([7, 8, 9, 1])
print(lista3)

# Función para ubicar en que indice esta el valor ingresado
print(lista3.index(5)) # el numero 5 esta en el indice 5
# print(lista3.index(0)) # esto daría un error por nos ser el elemento parte de la lista

# Como saber cuantos valores repetidos hay dentro de una lista
print(lista3.count(1)) # Cuenta cuantos valores iguales hay dentro de la lista

# Para poner al reves una lista pero no ordenados
lista3.reverse()
print(lista3)

# Para que una lista se multiplique repitiendo sus elementos
lista = [1,2,3] * 2
print(lista)
lista3 = lista3 * 2
print(lista3)

# Métodos de ordenamiento, en python es una función
lista3.sort() # Ordena los elementos ascendentemente
print(lista3)
lista3.sort(reverse=True) # Ordena descendentemente
print(lista3)

#####################################################
# Repaso de Tuplas
tupla = (4, 'Hola', 6.78, [1, 2, 78], 4, 'Hola') # Puede tener diferentes tipos de datos dentro
print(tupla)

# buscar un elementi
print(4 in tupla) # Acción booleana, su respuesta es de tipo booleana
# Lo que podemos usar dentro de tuplas son: index, count, len
# En tuplas se puede convertir de tupla a lista y de lista a tupla

######################################################
# Repaso de set o conjunto
# para definir un conjunto
conjunto2 = set() # unica forma de inicializarlo vacio
conjunto= {} # no se puede añadir mas elementos
conjunto1 = {'bye', }
conjunto2.add(7)
conjunto2.add('Hola')
print(conjunto2)
conjunto1.add('hola') # solo permite ingresar de a un elemento
print(conjunto1)
print(3 not in conjunto1) # Preguntamos si el número 3 NO esta en el conjunto1

# Como hacer la igualdad de dos conjuntos
print(conjunto1 == conjunto2) # Nos devuelve como respuesta un booleano

# Operaciones en conjuntos
# Union
conjunto3 = conjunto1 | conjunto2 # La línea une los dos conjuntos
print(conjunto3)

# Interseccion
conjunto3 = conjunto1 & conjunto2 # Que elemento tienen en comun
print(conjunto3)

# Diferencia
conjunto3 = conjunto1 - conjunto2 # Asigna el valor que esta en el conjunto1 y no en el conjunto2
print(conjunto3)
conjunto3 = conjunto2 - conjunto1
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2 # elementos que no comparten o que son diferentes entre ambos
print(conjunto3)

# Subconjuntos
conjunto3 = conjunto1 | conjunto2
print(conjunto2.issubset(conjunto3)) # Aquí preguntamos si un conjunto 2 es un subconjunto del conjunto 3
print(conjunto1.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto2))

# Superconjunto
print(conjunto3.issuperset(conjunto1)) # Preguntamos si los elementos del conjunto1 estan dentro del 3
print(conjunto3.issuperset(conjunto2)) # Si es verdadero quiere decir que el conjunto3 es un superconjunto
print(conjunto2.issuperset(conjunto3))

# Como saber si ambos conjuntos son disconexos, esto es si no comparten elementos en comun
print(conjunto1.isdisjoint(conjunto2)) #No hay cosas en comun

# Convertir un conjunto totalmente en inmutable
conjunto1 = frozenset # Esto hace que el conjunto sea totalmente inmutable
# No se puede agregar, modificar ni eliminar elementos del conjunto

#####################################################
# Repaso Diccionarios
diccionarioNuevo = {'Azul': 'Blue', 'Rojo': 'Red', 'Verde': 'Green', 'Amarillo': 'Yellow'}
print(diccionarioNuevo)

# Como eliminar
del (diccionarioNuevo['Azul'])
print(diccionarioNuevo)

# Los diccionarios pueden almacenar diferente tipos de datos
diccionario2 = {'Ariel': {'Edad': 40, 'Altura': 1.83}, 'Osvaldo': [45, 1.85], 'Natalia': [35, 1.67]}
print(diccionario2)

# Diccionario para datos de la selección Argentina (base de datos)
seleccionArgentina = {
    10: {'Nombre': 'Lionel Messi', 'Edad': 35, 'Altura': 1.70, 'Precio': '50 Millones', 'Posicion': 'Extremo Derecho'},
    11: {'Nombre': 'Ángel Di María', 'Edad': 34, 'Altura': 1.80, 'Precio': '12 Millones', 'Posicion': 'Extremo Derecho'},
    21: {'Nombre': 'Paulo Dybala', 'Edad': 28, 'Altura': 1.77, 'Precio': '35 Millones', 'Posicion': 'Media Punta'},
    19: {'Nombre': 'Nicolás Otamendi', 'Edad': 34, 'Altura': 1.83, 'Precio': '3.5 Millones', 'Posicion': 'Defensa Central'},
    1: {'Nombre': 'Franco Armani', 'Edad': 35, 'Altura': 1.89, 'Precio': '3.5 Millones', 'Posicion': 'Portero'}
}
print(seleccionArgentina[10])
print(seleccionArgentina.values()) # muestra los valores del diccionario

# Recorremos el diccionario

for llave in seleccionArgentina:
    print(llave) # muestra 10,11,21,19,1

for valor in seleccionArgentina.values():
    print(valor)

for llave, valor in seleccionArgentina.items():
    print(llave, valor)

# Como tarea agregar por lo menos 4 Jugadores mas al diccionario: seleccionArgentina
print('Tenemos cargados en el diccionario la cantidad de jugadores: ', end=' ')
print(len(seleccionArgentina))

#####################################################################################
# Metodo Pilas usando listas
pila = [1, 2, 3]

# Agregar elementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)

# Sacamos elementos desde el final
elementoBorrado = pila.pop() # Quita el último elemento y lo guarda en la variable elementoBorrado
print(f'Sacamos el elemento: {elementoBorrado}')
print(f'La pila ahora quedo así: {pila}')

# Colas con listas
# Estructura de datos de tipo fifo(first input / first output)
cola = ['Ariel', 'Osvaldo', 'Liliana', 'Pilar']

# Agregamos elementos al final de la cola
cola.append('Natalia')
cola.append('José')
print(cola)

# Sacamos elementos de la cola
seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

# Seguimos mostrando como recorrer un diccionario con el ciclo for
for i in seleccionArgentina:
    print(f'{i} -> {seleccionArgentina[i]}')
