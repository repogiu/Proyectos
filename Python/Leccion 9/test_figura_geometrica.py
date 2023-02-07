# Clase para testear

from Cuadrado import Cuadrado
from FiguraGeometrica import FiguraGeometrica
from Rectangulo import Rectangulo

print('Creación de objeto clase Cuadrado'.center(50, '_'))
cuadrado1 = Cuadrado(8, 'Azul') # le pasamos los argumentos
cuadrado1.alto = 7
# cuadrado1.ancho = 7
# print(cuadrado1.ancho)
# print(cuadrado1.alto)
print(f'Cálculo del área del cuadrado: {cuadrado1.calcular_area()}')

# MRO = Method Resolution Order
# print(Cuadrado.mro())

print(cuadrado1) # aqui muestra el metodo dunder str de la clase cuadrada


print('Creación de objeto clase Rectangulo'.center(50, '_'))
rectangulo1 = Rectangulo(3, 9, 'verde')
rectangulo1.ancho = 8
print(f'Calculo del area del rectangulo: {rectangulo1.calcular_area()}')
print(rectangulo1) # aqui nos muestra el metodo str

# figura1 = FiguraGeometrica() No se puede instanciar, es abstracta
print(Cuadrado.mro())