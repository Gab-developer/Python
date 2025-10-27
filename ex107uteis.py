def metade(n):
    met = n/2
    return met


def dobro(n):
    return n * 2


def aumento(n):
    tant = n / 100 * 5
    aum = n + tant
    return aum


def diminuir(n):
    tant = n / 100 * 13
    dim = n - tant
    return dim

def resumo(n=0, a=10, d=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t\tR${n}')
    print(f'Dobro do preço: \t\tR${dobro(n):.2f}')
    print(f'Metade do preço: \t\tR${metade(n):.2f}')
    print(f'Com {a}% de aumento: \tR${aumento(n):.2f}')
    print(f'Com {d}% de redução: \tR${diminuir(n):.2f}')
    print('-' * 30)
