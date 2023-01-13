# Ejercicio 7:
# Dadas las horas trabajadas de 5 personas y la tarifa de pago,
# calcular el salario
# la sumatoria de todos los salarios

i=0
horas=0
tarifa=0.00
sumatoriaSalario=0.00

for i in range(0,4):
    print(f"Salario del empleado {i+1}")
    horas = int(input("Digite las horas trabajadas: "))

    tarifa =int(input("Digite la tarifa por hora: "))
    salario = horas * tarifa
    print(f"El salario es:${salario}")
    sumatoriaSalario +=salario

    print("")

    print(f"La suma de todos los salarios es: ${sumatoriaSalario:.2f}")
