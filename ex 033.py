n1 = int(input('Digite o primeiro número'))
n2 = int(input('Digite o segundo número'))
n3 = int(input('Digite o terceiro número'))
menor = n1
maior = n2
#Verificando o menor
if n2 < n3 and n2 < n1:
    menor = n2
if n3 < n2 and n3 < n1:
    menor = n3
#Verificando o Maior valor
if n1 > n2 and n1 > n3:
    maior = n1
if n3 > n1 and n3 > n2:
    maior = n3
print('O menor valor digitado foi:{}'.format(menor))
print('O maior valor digitado foi:{}'.format(maior))
