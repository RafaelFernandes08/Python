from random import randint
num = randint(1,5)
print('pensando em um número....')
u = (int(input('Adivinhe o numero de 1 a 5 que eu pensei:')))
if u == num:
    print('Parabens,Você ganhou!')
else:
    print('Você Perdeu! o número que eu pensei era {}'.format(num))
