#Crie uma função que recebe dois parâmetros e faz a soma, produto, divisão e subtração desses
# parâmetros após isso implemente a aplicação dessa função em outro programa e mostra o resultado no
# segundo programa

def oper(x,y):
     x = float(input('Informe um número: '))
     y = float(input('Informe um número: '))

     resultado = (x+y, x*y, x/y, x-y)
     print (resultado)
