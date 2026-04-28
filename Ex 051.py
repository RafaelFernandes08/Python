print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)
pri = int(input('Primeiro Termo:'))
r = int(input('Razão:'))
t = 0
for t in range (1 , 11):
    pa = pri + (t - 1) * r
    print(pa)


