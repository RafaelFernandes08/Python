print('-' *16)
print('Lojas Americanas')
print('-' *16)
compras = float(input('Valor total das compras: R$'))
print('Formas de pagamento')
print('1 - à vista dinheiro/cheque')
print('2 - à vista no cartão')
print('3 - em até 2x no cartão')
print('4 - 3x ou mais no cartão')
metodo = int(input('Opção de pagamento:'))

if metodo == 1:
    print('Sua compra no valor de R${:.2f}, sendo paga à vista dinheiro/cheque receberá um desconto de 10%'.format(compras))
    print('O novo valor será de R${:.2f}'.format(compras - (compras * 0.10)))
elif metodo == 2:
    print('Sua compra no valor de R${:.2f}, sendo paga à vista no cartão receberá um desconto de 5%'.format(compras))
    print('O novo valor será de R${:.2f}'.format(compras - (compras * 0.05)))
elif metodo == 3:
    print('Sua compra no valor de R${:.2f}, sendo paga em até 2x no cartão não receberá juros'.format(compras))
    print('O valor final será de:R${:.2f}'.format(compras))
    print('E sera pago em duas parcelas no valor de:R${:.2F}'.format(compras / 2))
elif metodo == 4:
    print('Sua compra no valor de R${:.2f}, sendo paga 3x ou mais no cartão receberá 20% de juros'.format(compras))
    print('O novo valor será de R${:.2f}'.format(compras + (compras * 0.20)))
    if metodo == 4:
        p = int(input('Em quantas vezes você pretende parcelar:'))
        print(' A compra será parcelada em {} vezes, O valor de cada parcela será de R${:.2f}'.format(p , (compras + (compras * 0.20))/ p))
else:
    print('Opção invalida, Selecione uma da 4 opções.')



