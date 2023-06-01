x = float(input('Informe a 1° nota: '))
y = float(input('Informe a 2° nota: '))
z = float(input('Informe a 3° nota: '))

if (x >= 0 and x <= 10) and (y >= 0 and y <= 10) and (z >= 0 and z <= 10):
    print('As notas são válidas.')
else:
    print('As notas não são válidas.')

MP = (x*1 + y*1.5 + z*2)/ 4.5
print('A média ponderada das notas é %.2f '% (MP))

if MP == 0:
    print("SR")
if MP < 0:
    print("Inválido.")
elif MP < 2:
    print("II")
elif MP < 5:
    print("MI")
elif MP < 7:
    print("MS")
elif MP < 9:
    print("MM")
elif MP >= 9:
    print("SS")



