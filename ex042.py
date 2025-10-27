seg1 = float(input('Primeiro segmento: '))
seg2 = float(input('Segundo segmento: '))
seg3 = float(input('Terceiro segmento: '))
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg2 + seg1:
    print('Esses valores \033[0;32mPODEM\033[m formam um triângulo', end=' ')
    if seg1 == seg2 and seg2 == seg3:
        print('EQUILÁTETO!')
    if seg1 != seg2 != seg3 != seg1:
        print('ESCALENO!')
    else:
        print('ISÓCELES!')

else:
    print('Esses segmentos \033[0;31mNÃO\033[m formam um triângulo!')
