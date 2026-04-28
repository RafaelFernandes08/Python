casa = float(input('Qual o valor da casa que você pretende comprar? R$'))
salario = float(input('Qual é o seu salário? R$'))
anos = float(input('Em quantos anos você pretende pagar a casa?'))
mensal = casa / (12 * anos)
validar = (salario * 30) / 100
print('O valor prestação será de {:.2f}'.format(mensal))
if  validar >= mensal:
    print('O seu emprestimo foi aprovado')
else:
    print('O seu não foi aprovado')
