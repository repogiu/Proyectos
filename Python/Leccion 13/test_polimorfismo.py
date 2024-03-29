from Empleado import Empleado
from Gerente import Gerente


def imprimir_detalles(objeto): # Este es el método para aprender lo que es el polimorfismo
    # print(objeto)  # De manera indirecta llama al str de la clase Empleado o Gerente
    print(type(objeto))  # Esto es para saber el tipo de dato que recibe
    print(objeto.mostrar_detalles())
    if isinstance(objeto, Gerente):
        print(objeto.departamento)


empleado = Empleado('Ariel', 50000)
imprimir_detalles(empleado) # apunta a la clase Empleado

gerente = Gerente('Natalia', 60000, 'Sistemas')
imprimir_detalles(gerente)
