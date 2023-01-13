
# Clase 6: veremos sentencias if/else
'''condicion = True
# condicion = 10 imprime TRue
# condicion = " " imprime false ( porque esta vacia)
if condicion:
# if condicion == True;
    print("Condicion Verdadera")
elif condicion == False:
    print("Condicion Falsa")
else:
    print("Condicion sin especificar") # cuando condicion= "Hola", no es igual ni a TRue ni False


condicion = 10
if condicion == True:
    print("Condicion Verdadera")
elif condicion == False:
    print("Condicion Falsa")
else:
    print("Condicion sin especificar")


# Conversion de numero a texto
num = int(input("Digite un numero en el rango del 1 al 3: "))
# numTexto = ""
if num == 1:
    numTexto = "Numero uno"
elif num == 2:
     numTexto = "Numero dos"
elif num == 3:
    numTexto = "Numero tres"
else:
    numTexto = "Has ingresado un numero fuera de rango"
print(f"El numero ingresado es: {num} - {numTexto}")'''

# Sintaxis simplificada del if/else con el Operador ternario: recomendable solamente para pequeños codigos
condicion = True
if condicion:
   print("Condicion verdadera")
else:
   print("Condicion falsa")

# operador ternario
print("Condicion verdadera") if condicion else print("Condicion falsa")