#Faça um programa que receba dois valores float : um de altura e um de peso, para calcular o IMC. Por fim mostre o resultado.

altura = float(input('Informe a altura: '))
peso = float(input('Informe o peso: '))

IMC = peso/(altura * altura)

print('O IMC é %.2f'% (IMC))