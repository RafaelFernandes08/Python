n1 = int(input('Digite um valor:'))
n2 = int(input('Digite um valor:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma vale:{} A multiplicação vale:{} A divisão vale:{:.3f}'.format(s , m , d), end = ' ')
print('A divisão inteira vale:{} A potência vale:{}'.format(di , e))