class Persona:
    # Variable de clase
    contador_personas = 0

    # Metodo de clase: contexto estatico
    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_personas += 1 # vamos incrementando
        return cls.contador_personas

    # Metodo dunder init: contexto dinamico
    def __init__(self, nombre, edad):
        # Persona.contador_personas += 1 # sin el metodo de clase
        # self.id_persona = Persona.contador_personas # sin el metodo de clase
        self.id_persona = Persona.generar_siguiente_valor()
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona [{self.id_persona} = {self.nombre} {self.edad}]'


persona1 = Persona('Ariel', 40)
print(persona1)
persona2 = Persona('Osvaldo', 45)
print(persona2)
persona3 = Persona('Liliana', 35)
print(persona3)

Persona.generar_siguiente_valor() # incrementamos el  identificador a 4 sin crear objeto

persona4 = Persona('Natalia', 35) # se asigna el id 5
print(persona4)
print(f'Valor contador personas: {Persona.contador_personas}')