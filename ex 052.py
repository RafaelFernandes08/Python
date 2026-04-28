num = int(input('Digite um número para verificar se ele é primo:'))
primo = 0
for c in range (1 , num + 1):
    if num % c == 0:
        print('{} É divisivel por {}'.format(num , c))
        primo += 1
    else:
        print('{} Não é divisivel por {}'.format(num , c))
print('{} foi divisivel {} vezes'.format(num , primo))
if primo == 2:
    print('{} é primo'.format(num))
else:
    print('{} Não é um numero primo'.format(num))