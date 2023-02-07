from FiguraGeometrica import FiguraGeometrica
from Color import Color


class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        # super.__init__(lado) # solo accede a la clase padre FiguraGeometrica
        FiguraGeometrica.__init__(self, lado, lado) # se pone si o si el self, un lado es el ancho y el otro lado es el alto
        Color.__init__(self, color)

    def calcular_area(self):
        return self.alto * self.ancho

# Sobreescribimo el metodo dunder str de la clase FiguraGeometrica y Color
    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}'