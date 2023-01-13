'''
# Giuliana Diaz Luna
# Clase 1
print("Hola Mundo")
# Clase 2:
miVariable = 3  # se asigna el tipo de dato
print(miVariable)
# Reutilizacion de variable (dinamica)
miVariable = "Hola a todos"
print(miVariable)  # print es una funcion porque permite ejecutar el codigo para imprimir datos
miVariable = 3.5
print(miVariable)

# Direccion de memoria
x = 10
y = 2
z = x + y
print(z)
print(id(x))  # la funcion id es para que nos muestre la direccion de la casilla de memoria de la variable x
# Las literales se escriben asi: x528, la variable y = x272, la variable z = x592 (son referencias de memoria)
print(id(y))
print(id(z))

# Clase 3: Los Tipos de datos son clases
abc: str = "Hola mundo"  # es referencia pero no dice que la variable abc es string
a = 10
print(type(a))  # type es un funcion que nos muestra el tipo de dato, nos muestra que la clase es de tipo int
b = 10.98
print(type(b))  # tipo flotante
c = True  # tipo booleano
print(type(c))
d = "Hola Profe"
print(type(d))

# Manejo de cadenas (string) Ejercio
miArtistaFavorito = "Harry Styles: "
caracteristicas = "El mejor cantante"
print("Mi artista favorito es:", miArtistaFavorito, caracteristicas)  # asigna espacios automaticamente
print("Mi artista favorito es: " + miArtistaFavorito + " " + caracteristicas)

numero1 = "10"
numero2 = "5"
print(numero1 + numero2)  # concatena la cadena
print(int(numero1) + int(numero2))  # convierte el string a entero

# Tipos booleanos(bool)
miBooleano = True
miBooleano = False
miBooleano = 3 > 2
print(miBooleano)

if miBooleano:
    print("Resultado verdadero")
else:
    print("Resultado falso")

# Procesar la entrada de usuario(input), funcion input (regresa un dato tipo string)
#resultado = input("Digite un numero: ")
#print(resultado)

# Conversion de la entrada de datos
num1 = int(input("Escribe el primer numero:"))
num2 = int(input("Escribe el segundo numero:"))
resultado = num1 + num2
print("El resultado de la suma es: ", resultado)

# Ejercicio:
titulo = input("Proporciona el nombre del libro: ")
autor = input("Proporciona el autor del libro: ")
print(titulo, "fue escrito por:", autor)


# Clase 4: Operadores aritmeticos
operandoA = 8
operandoB = 5

suma = operandoA + operandoB
print("El resultado de la suma es:", suma)
print(f"El resultado de la suma es: {suma}") # interpolacion: incluye la variable dentro del mensaje

resta = operandoA - operandoB
print(f"El resultado de la resta es: {resta}")

multiplicacion = operandoA * operandoB
print(f"El resultado de la multiplicacion es: {multiplicacion}")

division = operandoA / operandoB
print(f"El resultado de la division es: {division}") # nos devuelve un resultado flotante
division = operandoA // operandoB
print(f"El resulado entero de la division es: {division}") # nos devuelve el numero entero

modulo = operandoA % operandoB
print(f"El modulo o residuo es: {modulo}")

exponente = operandoA ** operandoB
print(f"El resultado del exponente es: {exponente}")

# Ejercicio rectangulo: calcular el area y el perimetro de un rectangulo
alto = int(input("Ingrese el alto del rectangulo:"))
ancho = int(input("Ingrese el ancho del rectangulo:"))
area = alto * ancho
perimetro = (alto + ancho) * 2   # darle prioridad primero a la suma con parentesis
print("El area del rectangulo es:", area, "y el perimetro es:", perimetro)

# Operadores de asignacion y comparación
miVariable = 10
print(miVariable) # imprime 10

# Operadores de reasignacion
miVariable = miVariable + 1
print(miVariable) # imprime 11

# Incremento con reasignacion
miVariable += 1
print(miVariable) # imprime 12

# miVariable = miVariable - 2
miVariable -= 2
print(miVariable) # al 12 le resta 2 e imprime 10

# miVarible = miVariable * 3
miVariable *= 3
print(miVariable) # imprime 30

# miVariable = miVariable / 2
miVariable /= 2
print(miVariable) # imprime 15.0 como flotante

# Concatenacion
palabra1 = 'Ho'
palabra2 = 'la'
resultado = palabra1 + palabra2
print(resultado)

# Repeticion
palabra3 = 'Hola'
resultado = palabra3 * 4
print(resultado)

# Operadores de comparacion

d = 5
b = 2
resultado = d == b  # comprobamos si son iguales
print(resultado)    # imprime False

# Operador diferente
resultado = d != b
print(resultado)

# Operador mayor que
resultado = d > b
print(resultado)

# Operador menor que
resultado = d < b
print(resultado)

# Operador menor o igual que
resultado = d <= b
print(resultado)

# Operador mayor o igual que
resultado = d >= b
print(resultado)

# Ejercicio numero par o impar
numero = int(input("Ingrese un numero: "))
print(f"El residuo de la division es: {numero % 2}")
if numero % 2 == 0:
    print(f"El numero {numero} es PAR")
else:
    print(f"El numero {numero} es IMPAR")

# Ejercicio: Es mayor de edad?
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Usted es mayor de edad")
else:
    print("Usted es menor de edad")

# variante
edadAdulta = 18
edadPersona = int(input("Digite su edad: "))
if edadPersona >= edadAdulta:
    print(f"Su edad es de {edadPersona} años, usted es mayor de edad")
else:
    print(f"Su edad es de {edadPersona} años, usted es menor de edad")

# Clase 5: Operadores logicos

# Operador and (binario)
a = False
b = False
resultado = a and b
print(resultado)

# Operador or (binario)
resultado = a or b
print(resultado)

# Operador not (unario)
resultado = not a
print(resultado)

# Ejercicio valor dentro de rango
numero = int(input("Ingrese un numero: "))
if numero >= 0 and numero <= 5:
    print(f"El numero {numero} se encuentra dentro del rango 0-5")
else:
    print(f"El numero {numero} se encuentra fuera del rango 0-5")

# Para el profe es:
valor = int(input("Ingrese un numero dentro del rango 0 al 5: "))
valorMinimo = 0
valorMaximo = 5
dentroRango = valor >= valorMinimo and valor <= valorMaximo
if dentroRango:
    print(f"El numero {valor} se encuentra dentro del rango")
else:
    print(f"El numero {valor} se encuentra fuera del rango")

# Otra variante
numero = int(input("Ingrese un numero: "))
if 0 <= numero <= 5:
    print(f"El numero {numero} se encuentra dentro del rango 0-5")
else:
    print(f"El numero {numero} se encuentra fuera del rango 0-5")


# Ejercicio con el operador or, not
# Preguntar si un padre puede asistir al juego de su hijo
# Verificamos si tiene vacaciones
# verificamos si tiene dia libre
vacaciones = True
diaDescanso = False
# operador or
if vacaciones or diaDescanso:
    print("Puede asistir al juego")
else:
    print("No puede asistir al juego")
# operador not
if not(vacaciones or diaDescanso):
    print("No puede asistir al juego")
else:
    print("Puede asistir al juego")


# Ejercicio rango entre 20 y 30 años con los operadores and y or
edad = int(input("Ingrese su edad: "))
if (20 <= edad <= 30):
# if (20<= edad < 30) or (30 <= edad < 40): con el operador or
    print(f"Su edad ingresada:{edad} esta entre los 20 y los 30 años")
else:
    print(f"Su edad ingresada:{edad} no esta entre los 20 y los 30 años")

# Con el operador and
edad = int(input("Ingrese su edad: "))
veinte = edad >= 20 and edad < 30
print(veinte) # imprime true o false
treinta = edad >= 30 and edad < 40
print(treinta)
if veinte or treinta:
    print('Estas dentro del rango los (20\'0) a (30\'0) años')
#if veinte or treinta:
#    print('Estas dentro del rango de los (20\'0)')
#elif treinta:
#   print('Estas dentro del rango de los (30\'0) años')
else:
    print("No estas dentro del rango de los (20'0) a (30'0) años")

# con el operador or
edad = int(input("Ingrese su edad: "))
if (20 <= edad < 30) or (30 <= edad < 40):
    print("Estas dentro del rango los (20'0) a (30'0) años")
else:
    print("No estas dentro del rango de los (20'0) a (30'0) años")

# Ejercicio: Mayor de dos numeros
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
if num1 > num2:
    print(f"El numero mayor es: {num1}")
else:
    print(f"El numero mayor es: {num2}")
'''
# Ejercicio: tienda de libros
print("Digite los siguientes datos del libro")
nombre = input("Ingrese el nombre del libro: ")
id = int(input("Ingrese el ID del libro: "))
precio = float(input("Ingrese el precio del libro: "))
envioGratis = input("Indicar si el envio es gratuito (Si/No): ")
if envioGratis == "Si":
    envio = "Sin costo"
elif envioGratis == "No":
    envio = "$100.00"
else:
    envio = "Opcion incorrecta, debe ingresar Si o No"
print(f"""

    Nombre: {nombre}
    ID: {id}
    Precio: {precio}
    Costo de envio: {envio}

""")

# Ejercicio tienda de libros - Para el profe:
print("Digite los siguientes datos del libro")
nombre = input("Ingrese el nombre del libro: ")
id = int(input("Ingrese el ID del libro: "))
precio = float(input("Ingrese el precio del libro: "))
envioGratis = input("Indicar si el envio es gratuito (True/False): ")
# para cambiar el tipo de dato string a booleano
if envioGratis == "True":
    envioGratis = True
elif envioGratis == "False":
    envioGratis = False
else:
    print("El valor ingresado es incorrecto, debe escribir True/False")
# imprimir en varias lineas con format
print(f'''

    Nombre: {nombre}
    ID: {id}
    Precio: {precio}
    Costo de envio: {envioGratis}
''')
