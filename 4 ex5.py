#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a
# 10. O usuário deve informar de qual número ele deseja ver a tabuada.
while True:
    i = int(input('\nDigite um número de 0 a 10: '))
    x=0
    if i ==9:
        exit("error 404")
    while i >= 1 and i <= 10:
        print(f"{i} x {x} = {i*x}")
        x+=1
        if x==10:
            i =100

# and
# 0 and 0 =0
# 1and 0 = 0
# 0 and 1 =1
# 1 and 1 =1
#brenda