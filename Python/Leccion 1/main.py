# Giuliana Diaz Luna
# Clase 1
print("Hola Mundo")
# Clase 2:
miVariable = 3
print(miVariable)
miVariable = "Hola a todos"
print(miVariable)
miVariable = 3.5
print(miVariable)
x = 10
y = 2
z = x + y
print(id(x))
# Las literales se escriben x528, la variable y = x272, la variable z = x592
print(id(y))
print(id(z))

#Clase 3: Tipos de datos
a = 10
print(type(a))
b = 10.98
print(type(b))
#c = true
#print(type(c))
d = "Hola Profe"
print(type(d))

# Manejo de cadenas (string)
miArtistaFavorito = "Harry Styles"
caracteristicas = "El mejor cantante"
print("Mi artista favorito es: "+miArtistaFavorito,caracteristicas)

numero1 = "8"
numero2 = "5"
print(numero1+numero2)
print(int(numero1)+int(numero2))

# Tipos booleanos
miBooleano = 3 > 2
print(miBooleano)

if miBooleano:
    print("Resultado verdadero")
else:
    print("Resultado falso")

# Procesar la entrada de usuario(input), funcion
resultado= input ("Digite un numero: ")
print(resultado)
# Conversion de la entrada de datos
num1 = int(input("Escribe el primer numero:"))
num2 = int(input("Escribe el segundo numero:"))
resultado= num1 + num2
print("El resultado de la suma es: ",resultado)

#Clase 4: Operadores aritmeticos
operandoA = 8
operandoB = 5
suma = operandoA + operandoB
print(f"El resultado de la suma es: {suma}")
resta = operandoA - operandoB
print(f"El resultado de la resta es: {resta}")
multiplicacion = operandoA * operandoB
print((f"El resultado de la operacion es: {multiplicacion}"))
division = operandoA / operandoB
print(f"El resultado de la division es: {division}")
division = operandoA // operandoB
print(f"El resulado entero de la division es: {division}")
modulo = operandoA % operandoB
print(f"El resulado de la division o modulo es: {modulo}")
exponente = operandoA ** operandoB
print(f"El resultado del exponente es: {exponente}")

# Ejercicio rectangulo
alto = int(input("Ingrese el alto del rectangulo:"))
ancho = int(input("Ingrese el ancho del rectangulo:"))
area = alto * ancho
perimetro = (alto + ancho) * 2
print("El area del rectangulo es:",area, "y el perimetro es:",perimetro)


miVariable = 10
print(miVariable)

# Operadores de reasignacion
miVariable = miVariable + 1
print(miVariable)

miVariable += 1
print(miVariable)

# miVariable = miVariable - 2
miVariable -= 2
print(miVariable)

# miVarible = miVariable * 3
miVariable *= 3
print(miVariable)

# miVariable = miVariable / 2
miVariable /= 2
print(miVariable)

# Operadores de comparacion

d = 5
b = 2
resultado = d == b # comprobamos si son iguales
print(resultado)

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

# Ejercicio par o impar
numero = int(input("Ingrese un numero: "))
print(f"El residuo de la division es {numero % 2}")
if numero % 2 == 0:
    print(f"El numero {numero} es par")
else:
    print(f"El numero {numero} es impar")

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

# Clase 5: Operadores parte 2
# Operador and
a = False
b = False
resultado = a and b
print(resultado)

# Operador or
resultado = a or b
print(resultado)

# Operador not
resultado = not a
print(resultado)

# Ejercicio valor dentro de rango
numero = int(input("Ingrese un numero: "))
if numero >= 0 and numero <= 5:
    print(f"El numero {numero} se encuentra dentro del rango 0-5")
else:
    print(f"El numero {numero} se encuentra fuera del rango 0-5")

# Para el profe es:
valor = int(input("Ingrese un valor: "))
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
vacaciones = False
diaDescanso = False
if not (vacaciones or diaDescanso):
    print("No puede asistir al juego")
else:
    print("Puede asistir al juego")

# Ejercicio rango entre 20 y 30 años
edad = int(input("Ingrese su edad: "))
if 20 <= edad <= 30:
    print("Su edad esta entre los 20 y los 30 años")
else:
    print("Su edad no esta entre los 20 y los 30 años")

# Para el profe:
edad = int(input("Ingrese su edad: "))
veinte = edad >= 20 and edad < 30
print(veinte)
treinta = edad >= 30 and edad < 40
print(treinta)
if veinte:
    print("Estas dentro del rango los (20'0) años")
elif treinta:
    print("Estas dentro del rango los (30'0) años")
else:
    print("No estas dentro del rango de los (20'0) a (30'0) años")

# sintaxis resumida
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
if envioGratis == "True":
    envioGratis = True
elif envioGratis == "False":
    envioGratis = False
else:
    print("El valor ingresado es incorrecto, debe escribir True/False")
print(f"""

    Nombre: {nombre}
    ID: {id}
    Precio: {precio}
    Costo de envio: {envioGratis}
""")