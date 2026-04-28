numero = int(input('Digite um número para descobrir a Tabuada:'))
for tabuada in range(1 , 11):
    print('{} x {} = {}'.format( numero , tabuada ,numero * tabuada))