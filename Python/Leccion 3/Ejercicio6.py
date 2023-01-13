# Ejercicio 6: Ingresar N enteros, visualizar
# la suma de los numeros
# pares de la lista, cuantos numeros pares existen y
# cual es el promedio de los numeros impares

sumaPares = 0
conteoPares = 0
sumaImpares = 0
conteoImpares = 0
promedioImpares = 0
contador = 0
maximo = 5
while contador < maximo:
     num = int(input("Ingrese un numero: "))
     contador += 1
     if num % 2 == 0:
          sumaPares += num
          conteoPares += 1
     else:
         sumaImpares += num
         conteoImpares += 1
         promedioImpares =sumaImpares/conteoImpares

print("Suma de numeros pares: ", sumaPares)
print("Cantidad de numeros pares: ", conteoPares)
print("Suma de numeros pares: ", sumaImpares)
print("Cantidad de numeros pares: ", conteoImpares)
print("Promedio de numeros impares: ", promedioImpares)