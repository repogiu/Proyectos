# Clase 8: Ciclo while (mientras o durante con un n° indeterminado de iteraciones)
#condicion = True
#while condicion:
#    print("ciclo infinito")
#else:
#    print("Fin del ciclo infinito")
'''
contador = 0
while contador < 78:
    print("Ejecutamos nuestro ciclo while ", contador)
    contador += 1 # si no lo incrementamos seguiria siendo infinito ( va a seguir siendo 0
# si es falso
else:
    print("Fin del ciclo while")

# Ejercicio: imprimir numeros del 0 al 5 con el ciclo while
maximo = 5
contador = 0
while contador <= maximo:
    print(contador)
    contador += 1

# Ejercicio: imprimir numeros del 1 al 5 de manera descendente con el Ciclo while
minimo = 1
contador = 5
while contador >= minimo:
    print(contador)
    contador -= 1

# Ciclo for (para hasta con paso hacer, con un n° determinado de iteraciones)
cadena = "Hello" # una cadena es un arreglo de caracteres
for letra in cadena: # recorre indice por indice
    print(letra)
else:
    print("Fin del ciclo for")

# Palabra reservada break
for letra in "Alemania":
    if letra == "a":
        print(f"Letra encontrada: {letra}")
        break
else:
    print("Fin del ciclo for")

# Palabra reservada continue
# ejercicio: imprimir los numeros pares que se encuentra dentro de un rango de datos
for i in range(6):
    if i % 2 == 0:
    print(f"Valor: {i}")

for i in range(6):
    if i % 2 != 0: # cuando encuentre un numero impar, continua ( la saltea)
        continue
    print(f"Valor: {i}")


# Ejercicio año bisiesto
# Diseñar un programa que ingresado un año, nos devuelva por consola
# si es un año bisiesto o no, repetir la accion hasta que el usuario lo decida-

condicion = 1
while condicion == 1:
     anio = int(input("Ingrese el año: "))
     if anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0:
         print("El año es bisiesto")
     else:
         print("El año no es bisiesto")
     condicion = int(input("Ingrese 1 si desea continuar, de lo contrario ingrese el 2: "))

# Ejercicio Calcular la suma de N primeros numeros

# Con el ciclo while

num = int(input("Ingrese un numero: "))
contador = 0
suma = 0
while contador <= num:
     suma += contador
     contador += 1
print(f"La suma de los {num} primeros numeros es {suma}")

# Con el ciclo for

num = int(input("Ingrese un numero: "))
suma = 0
for i in range(1,num+1):
     suma += i
print(f"La suma de los {num} primeros numeros es {suma}")


# Ejercicio: leer 10 numeros e imprimir
# cuantos son pares, impares y neutros

contador = 0
maximo = 10
sumapares = 0
sumaimpares = 0
sumaneutros = 0
while contador < maximo:
     num = int(input("Ingrese un numero: "))
     contador += 1
     if num % 2 == 0 and num != 0:
          sumapares += 1
     elif num % 2 != 0:
          sumaimpares += 1
     else:
          sumaneutros += 1
print("Cantidad de numeros pares: ", sumapares)
print("Cantidad de numeros impares: ", sumaimpares)
print("Cantidad de numeros neutros: ", sumaneutros)'''

# Ejercicio: Suponga que se tiene un conjunto de calificaciones de un grupo de 10 alumnos
# Realizar un algoritmo para calcular la calificacion promedio y la calificacion mas baja de todo el grupo
contador = 0
maximo = 10
sumacalif = 0
promediocalif = 0
califmasbaja = 10
while contador < maximo:
     calificacion = int(input("Ingrese las calificaciones: "))
     sumacalif += calificacion
     contador += 1
     if calificacion < califmasbaja:
          califmasbaja = calificacion
promediocalif = sumacalif / contador
print(f"La calificacion promedio es {promediocalif}")
print(f"La calificacion mas baja es {califmasbaja}")