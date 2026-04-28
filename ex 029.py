velo = int(input('Qual a velocidade do Carro em km?'))
m = (velo - 80) * 7
if velo <=80:
    print('O carro está no limite de velocidade')
else:
    print('O carro levou uma multa de R${}'.format(m))
