import random
p = str(input('Primeiro Aluno:'))
s = str(input('Segundo Aluno:'))
t = str(input('Terceiro Aluno:'))
q = str(input('Quarto aluno:'))
g = (p , s , t ,q )
e = (random.choice(g))
print('O aluno escolhido foi {}'.format(e))
