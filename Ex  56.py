#Primeira pessoa
p_nome = 0
p_idade = 0
p_sexo = 0
#Segunda pessoa
s_nome = 0
s_idade = 0
s_sexo = 0
#Terceira pessoa
t_pessoa = 0
t_idade = 0
t_sexo = 0
#Quarta pessoa
q_nome = 0
q_idade = 0
q_sexo = 0
#Coleta de dados
for p in range (1 , 5):
    print('{}ªPessoa'.format(p))
    nome = str(input('Nome:'))
    idade = int(input('Idade:'))
    sexo = str(input('M/F:'.upper()))
    if p == 1:
        p_nome = nome
        p_idade = idade
        p_sexo = sexo
    if p == 2:
        s_nome = nome
        s_idade = idade
        s_sexo = sexo
    if p == 3:
        t_nome = nome
        t_idade = idade
        t_sexo = sexo
    if p == 4:
        q_nome = nome
        q_idade = idade
        q_sexo = sexo
#Media de idade
print('A media de idade do grupo é:{} anos'.format((p_idade + s_idade + t_idade + q_idade) / 4))
