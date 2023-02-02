from Persona2 import Persona2
# from Persona2 import *     # si el modulo Persona2 tiene muchas clases ponemos *
print('Creación de objetos'.center(50, '-'))

if __name__ == '__main__': # solo muestra el codigo de la clase PruebaPersona2
    persona5 = Persona2('Lionel', 'Messi', 35)
    persona5.mostrar_detalles()

    print(__name__)


# Destructor de objetos
print('Eliminación de Objetos'.center(50, '-')) # 30 caracteres(width) y agregamos el guion medio(fillchar)
del persona5