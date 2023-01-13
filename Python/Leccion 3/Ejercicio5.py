# calcular el factorial de un numero mayor o igual a 0

num = int((input('Ingrese un numero para factorizar: ')))
factorial = 1

if num != 0:
    for i in range(1, num + 1):
        factorial = factorial * i
else:
    print('Numero invalido factorial de 0 y numeros negativos es 1 ')
print(f'su numero : {num} tiene como factorial : {factorial}')



# lo realizamos sin la funcion range

num = int(input('Ingrese un numero  para factorizar: '))
i = 2
factorial = 1
if num != 0:

    while i <= num:
        factorial *= i
        i += 1

print(f'su numero : {num} tiene como factorial : {factorial}')