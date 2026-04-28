km = float(input('Quantos km o carro alugado percorreu?'))
dia = int(input('Quantos dias esse carro ficou alugado?'))
d = km * 60
k = dia * 0.15
t = d + k
print('O valor total a ser pago pelo aluguel do carro é de R${:.2f}'.format(t))
