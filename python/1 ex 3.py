#Receba (input) um valor em real (R$) e mostre a conversão para dólar americano e euro

real = float(input("Qual é o valor em reais a ser convertido? "))

print('O valor em dólar é %.2f' % (real/float(5.01)))
print('O valor em euro é %.2f' % (real/float(5.37)))