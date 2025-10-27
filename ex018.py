import math
an = float(input('Digite o ângulo: '))
sen = math.sin(math.radians(an))
print('O ângulo {} possue o seno de {:.2f}'.format(an, sen))
cos = math.cos(math.radians(an))
print('O ãngulo {} possue o cosseno de {:.2f}'.format(an, cos))
tan = math.tan(math.radians(an))
print('O algulo {} possue a tangente de {:.2f}'.format(an, tan))
