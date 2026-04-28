from math import sqrt
a = float(input('digite o cateto adjacente: '))
b = float(input('Digite o cateto oposto: '))
h = sqrt(a**2+b**2)
print('A hipotenusa desse triangulo retangulo é {:.2f}'.format(h))
