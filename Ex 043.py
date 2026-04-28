print('-'* 18)
print('Calculadora De IMC')
print('-'* 18)

peso = float(input('Peso em kg:'))
altura = float(input('Altura em metros:'))
calculo = peso / (altura ** 2)

print('Seu Imc é:{:.2f} '.format(calculo))

if calculo < 18.5:
    print('Você está abaixo do peso ideal')
elif calculo >= 18.5 and calculo < 25.0:
    print('Você esta no peso ideal')
elif calculo >= 25.0 and calculo < 30.0:
    print('Você está com sobrepeso')
elif calculo >= 30.0 and calculo < 35.0:
    print('Você está com obesidade grau I, Procure um medico Imediatamente')
elif calculo >= 35.0 and calculo < 40.0:
    print('Você está com obesidade grau II, Procure um medico Imediatamente')
elif calculo >= 40:
    print('Você está com obesidade grau III, Procure um medico Imediatamente')

