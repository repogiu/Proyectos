# Ejercicio 5: Convertidor de temperaturas
# Realizar dos funciones para convertir de grados celsius
# a fahrenheit y viseversa.

# Función que convierte de celsius a fahrenheit
def celsius_fahrenheit(celsius):
    return celsius * 9 / 5 + 32 # La precedencia: multiplicación, división y suma

# Función que convierte de fahrenheit a celsius
def fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9 # Respetar la precedencia utilizando parentesis

celsius = float(input('Digite la temperatura en Celsius: '))
resultado = celsius_fahrenheit(celsius)
print(f'{celsius} Celsius equivale a  {resultado:.2f} Fahrenheit')

fahrenheit = float(input('Digite la temperatura en Fahrenheit: '))
resultado = fahrenheit_celsius(fahrenheit)
print(f'{fahrenheit} Fahrenheit equivale a  {resultado:.2f} Celsius')