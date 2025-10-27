print('\033[0;32m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('\033[0;32mAnalisador de Triângulos\033[m')
print('\033[0;32m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\033[m')
n1 = float(input('Digite o primeiro segmento: '))
n2 = float(input('Digite o segundo segmento: '))
n3 = float(input('Digite o terceiro segmento: '))
if n1 < n2 + n3 and n2 < n3 + n1 and n3 < n1 + n2:
    print('Eles formam um triãngulo')
else:
    print('Eles NÃo formam um triângulo')
