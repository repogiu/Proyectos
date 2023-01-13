# Ejercicio: Calcular estacion del año
# Pedir al usuario que ingrese un mes del año, el valor debe ser entre 1 y 12,
# luego le decimos en que estacion esta

mes = int(input("Digite un mes del año (1 - 12): "))
estacion = None
if mes == 1 or mes == 2 or mes == 3:
    estacion = "Verano"
elif mes == 4 or mes == 5 or mes == 6:
    estacion = "Otoño"
elif mes == 7 or mes == 8 or mes == 9:
    estacion= "Invierno"
elif mes == 10 or mes == 11 or mes == 12:
    estacion= "Primavera"
else:
    estacion = "Error, no hay numero para ese mes"
print (f"Para el mes {mes} la estacion es: {estacion}")