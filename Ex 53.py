nome = str(input('Digite um nome ou uma frase:').upper())
nome = (nome.replace(' ' , ''))
inverso = (nome[::-1])
if nome == inverso:
    print(inverso)
    print('{} é um palíndromo'.format(nome))
else:
    print(inverso)
    print('{} não é um palíndromo'.format(nome))

