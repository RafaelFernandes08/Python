import math
an = float(input('Digite o angulo que deseja:'))
sen = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tg = math.tan(math.radians(an))
print('O seno do angulo {} é {:.2f}'.format(an , sen))
print('O cosseno do angulo {} é {:.2f}'.format(an , cos))
print('A Tangente do angulo {} é {:.2f}'.format(an , tg))
