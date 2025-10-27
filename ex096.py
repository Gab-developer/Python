def area(l, c):
    a = largura * comprimento
    print(f'A área de um terreno {l}x{c} é {a}m²')


# Programa Principal:
largura = float(input('Digite a largura: '))
comprimento = float(input('Digite o comprimento: '))
area(largura, comprimento)