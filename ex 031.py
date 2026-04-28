v = float(input('Qual é a distancia da viagem em km?'))
if v <=200:
    print('A viajem custará o valor de:R${:.2f}'.format(v * 0.50))
else:
    print('A viajem custará o valor de:R${:.2f}'.format(v * 0.45))