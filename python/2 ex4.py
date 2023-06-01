#Crie um programa que receba três notas de 0 até 10 (faça as validações para aceitar apenas esse
# intervalo), depois faça o cálculo da média aritmética e então mostre a média calculada e também se o aluno
# passou ou não. A escola aceita média 7 (sete) acima para aprovação.

x = float(input('Informe a 1° nota: '))
y = float(input('Informe a 2° nota: '))
z = float(input('Informe a 3° nota: '))

if (x >= 0 and x <= 10) and (y >= 0 and y <= 10) and (z >= 0 and z <= 10):
    print('As notas são válidas.')
else:
    print('As notas não são válidas.')

média = (x+y+z)/3

print('A média das notas é %.2f '% (média))

if média >= 7:
    print("Aluno aprovado!")
elif média < 7 and média >= 0:
    print("Aluno reprovado!")
else:
    print("Média inválida")
