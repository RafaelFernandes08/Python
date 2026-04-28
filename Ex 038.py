ano = int(input('Ano de nascimento? '))
idade = 2026 - ano
print('Você tem {} ano(s).'.format(idade))

if idade < 18:
    tempo = 18 - idade
    an = 2025 + tempo
    print('Faltam {} ano(s) para seu alistamento!'.format(tempo))
    print('Você deve se alistar em {}!'.format(an))
elif idade > 18:
    at = idade - 18
    ann = 2025 - at
    print('Você deveria ter se alistado há {} ano(s).'.format(at))
    print('Você deveria ter se alistado em {}.'.format(ann))
else:
    print('Você deve se alistar IMEDIATAMENTE!')
