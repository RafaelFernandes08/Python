p = int(input('Primeiro Segmento:'))
s = int(input('Segundo Segmento:'))
t = int(input('Terceiro Segmento:'))

if p + s < t or p + t < s or s + t < p:
    print('Não podemos formar um triângulo')
elif p == s and p == t:
    print('Podemos formar um Triângulo Equilátero')
elif p == s or s == p or t == s or t == p:
    print('Podemos formar um triângulo Isósceles')
else:
    print('Temos um Triângulo Escaleno')
