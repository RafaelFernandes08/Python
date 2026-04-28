frase = str(input('Digite uma frase:')).strip().upper()
print('A frase têm {} Letras a'.format(frase.count('A')))
print('A primeira letra a aparece na posição {}'.format(frase.find('A')+1))
print('A ultima Letra a aparece na posição {}'.format(frase.rfind('A')+1))