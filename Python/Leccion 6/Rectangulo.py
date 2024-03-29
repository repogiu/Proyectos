class Rectangulo:
    """
    Crear una clase llamada Rectangulo, debe tenér 2 atributos: altura y base
    el nombre del método será calcular_area (snake_case) utilizando la formula:
    area = base * altura. Pero la base y la altura deben ser ingresadas por
    el usuario y los objetos deben ser tres.
    """
    # metodo inicializar
    def __init__(self, altura, base):
        # inicializamos los atributos
        self.altura = altura
        self.base = base

    def calcular_area(self):
        return self.base * self.altura

base = int(input('Digite el número para la base del rectangulo: '))
altura = int(input('Digite el número para la altura del rectangulo: '))
# creamos el objeto rectangulo1 (instanciamos el objeto de la clase)
rectangulo1 = Rectangulo(base, altura)
print(f'El area del rectangulo es: {rectangulo1.calcular_area()}')