s = float(input('Quantos Reais você tem na carteira?R$'))
d = s / 5.88
e = s / 6.24
print('Com R${} você pode comprar US${:.2f}!'.format(s , d))
print('Com R${} você pode comprar EUR€{:.2f}'.format(s , e ))