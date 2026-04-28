import random
p = str(input('Primeiro Aluno'))
s = str(input('Segundo Aluno'))
t = str(input('Terceiro Aluno'))
q = str(input('Quarto Aluno'))
qui = str(input('Quinto Aluno'))
g = [p , s , t , q , qui]
print('A Ordem de apresentação será ')
random.shuffle(g)
print(g)
