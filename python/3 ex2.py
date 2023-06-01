#Faça uma função que receba uma variável e mostre na tela se ele for múltiplo de 2
def multiplo():
    x = float(input('Informe um valor: '))

    if x%2==0:
        print('O número é múltiplo de 2.')
    else:
        print('O número não é múltiplo de 2.')

multiplo()