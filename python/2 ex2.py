#Desenvolva um programa que recebe dois números inteiros e retorna o maior deles.

x = int(input('Digite um número: '))
y = int(input('Digite outro número: '))

if x > y:
    print('O maior número é', x)
elif y > x:
    print('O maior número é', y)
else:
    print('Os números são iguais.')