from abc import ABC, abstractmethod


# ABC significa: Abstract Base Class, convierte una clase en abstracta

class FiguraGeometrica(ABC): # el parametro ABC indica que ahora la clase Figura Geometrica es hija de la clase abstracta ABC
    def __init__(self, ancho, alto):
        if self._validar_valores(ancho): # equivale a if 0 < ancho < 10
            self._ancho = ancho
        else:
            self._ancho = 0
            print(f'Valor erroneo para el ancho: {ancho}')
        if self._validar_valores(alto): # equivale a if 0 < alto < 10
            self._alto = alto
        else:
            self._alto = 0
            print(f'Valor erroneo para el alto: {alto}')

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        if self._validar_valores(ancho): # validamos el metodos sett
            self._ancho = ancho
        else:
            print(f'valor erroneo ancho: {ancho}')

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        if self._validar_valores(alto):
            self._alto = alto
        else:
            print(f'valor erroneo alto: {alto}')

    # agregamos el metodo abstracto debajo del ultimo sett y arriba dem metodo str
    @abstractmethod # decorador
    def calcular_area(self): # el metodo calcular area es abtracto pero no se implementa, obliga a las clases hijas que implemente el metodo calcular_area
        pass

    def __str__(self):
        return f'FiguraGeometrica [Ancho: {self._ancho}, Alto: {self._alto}]'

    def _validar_valores(self, valor):  # Método encapsulado con guion bajo
        return True if 0 < valor < 10 else False # sintaxis simplificada