nome =str(input('Qual o seu nome completo?')).strip()
s = nome.split()
print('Seu primeiro nome é {}'.format(s[0]))
print('Seu ultimo nome é {}'.format(s[len(s)-1]))