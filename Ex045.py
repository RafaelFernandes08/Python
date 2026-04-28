from random import randint
import time
print('='*23)
print('Pedra, Papel ou Tesoura')
print('='*23)
print('Qual jogada você deseja:')
print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')
computador = randint( 1 , 3)
jogador = int(input('Escolha uma das opções:'))
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!')
print('-=-'*10)
print('O computador escolheu a opção {}'.format(computador))
print('O Jogador escolheu a opção {}'.format(jogador))
print('-=-'*10)
if jogador > 3 or jogador < 1:
    print('Opção invalida, escolha uma das opções validas')
if jogador == computador:
        print('O jogo empatou')
if jogador == 1 and computador == 2:
    print('O Computador venceu')
if jogador == 1 and computador == 3:
    print('O jogador venceu')
if jogador == 2 and computador == 1:
    print('O jogador venceu')
if jogador == 2 and computador == 3:
    print('O computador venceu')
if jogador == 3 and computador == 1:
    print('O computador venceu')
if jogador == 3 and computador == 2:
    print('O jogador venceu')



