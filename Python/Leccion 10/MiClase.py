class MiClase:
    # Variable de clase, este atributo dará a cada objeto el mismo valor
    variable_clase = 'Esta es una variable de clase'

    def __init__(self, variable_instancia):  # La variable de instancia, da diferentes valores
        self.variable_instancia = variable_instancia

    # Método estático, se asocia a la clase
    @staticmethod
    def metodo_estatico():
        print(MiClase.variable_clase)

    # Metodo de clase: hace referencia a una clase
    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)

    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()
        print(self.variable_clase)
        print(self.variable_instancia)


print(MiClase.variable_clase)
miClase1 = MiClase('Esta es una variable de instancia')
print(miClase1.variable_instancia)
print(miClase1.variable_clase)

# creamos una variable de clase fuera de la identacion de MiClase
miClase2 = MiClase('Esta es otra prueba de variable de instancia')
print(miClase2.variable_instancia)
print(miClase2.variable_clase)

MiClase.variable_clase2 = 'Valor de variable de clase 2'
print(MiClase.variable_clase2)
print(miClase1.variable_clase2)
print(miClase2.variable_clase2)

# Llamada al metodo estatico
MiClase.metodo_estatico()

MiClase.metodo_clase()

#creamos un objeto y accedemos atravez del metodo de clase (contexto estatico) y del metodo de instancia /contexto dinamico)
miObjeto1 = MiClase('variable de instancia')
miObjeto1.metodo_clase()
miObjeto1.metodo_instancia()
