salario = float(input('Qual é o salário do funcionario?'))
if salario > 1250.00:
    aumento = salario + (salario * 10 / 100)
else:
    aumento = salario + (salario * 15 / 100)
if salario > 1250.00:
    print('Esse funcionario recebera um aumento de 10%')
else:
    print('Esse funcionario receberá um aumento de 15%')
print('O novo salário desse funcionario será de {:.2f}'.format(aumento))