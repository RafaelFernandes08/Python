pm = int(input('Primeiro termo:'))
razão = int(input('Digite a razão'))
calculo = pm + (10 - 1)* razão
for c in range ( pm  , calculo + 1 , razão):
    print(c)