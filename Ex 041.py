from datetime import datetime

ano = datetime.now().year

atleta = int(input('Ano de Nascimento:'))

idade = ano - atleta

print('O atleta têm {} anos'.format(idade))

if idade < 10:
    print('O atleta pertence a categoria:MIRIM')

elif idade > 10 and idade < 15:
    print('O atleta pertence a categoria:INFANTIL')

elif idade > 14 and idade < 20:
    print('O atleta pertence a categoria:Júnior')

elif idade > 19 and idade < 26:
    print('O atleta pertence a categoria:SÊNIOR')

else:
    print('O atleta pertence a categoria:MASTER')