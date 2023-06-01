#Faça um programa que retorna a hora que for digitada e cumprimente de acordo com o horário.

x = int(input('Digite a hora (0-23): '))

if x >= 0 and x < 6 :
    print("São", x,"horas.Boa Madrugada!")
elif x >= 6 and x < 12 :
    print('São', x,"horas.Bom Dia!")
elif x >= 12 and x < 18 :
    print("São", x, "horas.Boa Tarde!")
elif x > 18 and x <= 23 :
    print("São", x,"horas.Boa Noite!")
else :
    print('Hora inválida.')