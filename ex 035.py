print('-=-=-'* 5)
print('Analisador de Triângulos')
print('-=-=-'* 5)
n1 = float(input('Digite o primeiro segmento:'))
n2 = float(input('Digite o segundo segmento:'))
n3 = float(input('Digite o terceiro segmento:'))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Esses segmentos podem formar um triângulo')
else:
    print('Esses segmentos não podem formar um triângulo')