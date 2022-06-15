#Ejercicio 1
#Deberemos plasmar la expresion en una expresion algoritmica, es decir en codigo

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))
resultado = (a**3*(b**2-2*a*c))/(2*b)
print(f"El resultado es: {resultado}")


# Ejercicio 2
a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
resultado = ((3+5*8)<3 and ((-6/3*4)+2<2)) or (a>b)
if resultado == True:
    print("El resultado es verdadero")
else:
    print("El resultado es falso")


# Ejercicio 3
a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
aux = a
a = b
b = aux
print(f"El valor de a es: {a}")
print(f"El valor de b es: {b}")

# Otra forma
a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
a,b=b,a
print(f"El valor de a es: {a}")
print(f"El valor de b es: {b}")


# Ejercicio 4
import math
r = float(input("Ingrese el valor del radio: "))
area = math.pi*r**2
longitud = 2*math.pi*r
print(f"El area del circulo es: {area:.2f}")
print(f"La longitud del circulo es: {longitud:.2f}")
