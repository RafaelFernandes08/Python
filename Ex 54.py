from datetime import date
maior = 0
menor= 0
ano_atual = date.today().year
for i in range (1 , 8):
    c = int(input('Em que ano a {}º pessoa nasceu?'.format(i)))
    if ano_atual - c >= 18:
        maior += 1
    else:
        menor += 1
print('Das sete pessoas {} são de maior e {} são de menor'.format(maior , menor))
