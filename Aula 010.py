n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
n3 = float(input('Digite a terceira nota:'))
m = (n1 + n2 + n3 )/3
if m >=6.0:
    print('O aluno teve uma media de {} e foi:Aprovado'.format(m))
else:
    print('O aluno teve uma media de {} e foi:Reprovado'.format(m))
