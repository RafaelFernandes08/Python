nome = str(input('Qual é o seu nome?'))

if nome.upper() == 'RAFAEL':
    print('Que nome bonito!')

elif nome.upper() == 'Ronaldo' or nome.upper() == 'MESSI':
    print('Que nome diferente!')
else:
    print('Que nome normal!')
print('Tenha um bom dia, {}'.format(nome))