#Escreva um algoritmo que solicita ao usuário dois números e uma operação (1 - Soma,
# 2 - Subtração, 3 - Divisão ou 4 - Multiplicação) e realiza a operação correspondente sobre os
# operandos fornecidos pelo usuário:

x = float(input('Informe um número: '))
y = float(input('Informe um número: '))
z = float(input('Digite 1 - Soma, 2 - Subtração, 3 - Divisão ou 4 - Multiplicação: '))

if z == 1:
    print(x + y)
if z == 2:
    print(x - y)
if z == 3:
    print(x/y)
if z == 4:
    print(x*y)
