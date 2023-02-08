# Clase para testear

from Cuadrado import Cuadrado
from FiguraGeometrica import FiguraGeometrica
from Rectangulo import Rectangulo

print('Creación de objeto clase Cuadrado'.center(50, '_'))
cuadrado1 = Cuadrado(8, 'Azul') # le pasamos los argumentos
# Reasignacion de valores
cuadrado1.alto = -7
# cuadrado1.ancho = 7
print(cuadrado1.ancho) # muestra el valor aceptado
print(cuadrado1.alto)
print(f'Cálculo del área del cuadrado: {cuadrado1.calcular_area()}')

# MRO = Method Resolution Order
# print(Cuadrado.mro())

print(cuadrado1) # aqui muestra el metodo dunder str de la clase cuadrada


print('Creación de objeto clase Rectangulo'.center(50, '_'))
rectangulo1 = Rectangulo(3, 9, 'verde')

# reasignacion de valores
rectangulo1.ancho = 8
print(f'Calculo del area del rectangulo: {rectangulo1.calcular_area()}')
print(rectangulo1) # aqui nos muestra el metodo str

# Clase Figura Geometrica como clase abstracta
# figura1 = FiguraGeometrica() Da error, No se puede instanciar, es abstracta
print(Cuadrado.mro())