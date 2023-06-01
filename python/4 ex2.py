#Escreva um algoritmo que solicita ao usuário N idades, o  programa apenas conta idades maiores
# ou iguais que 18. E ao final do código deve mostrar o número de usuários que tem +18. O programa
# deve solicitar valores até que o usuário entre com -1. (Usando while)

idade = 0
count = 0

while idade!= -1:
    idade = int(input('Informe a idade: '))

    if idade >= 18:
        count +=1
print('O número de usuários que têm 18 anos ou mais é', count)