from random import randint
def sortear(lista):
    for c in range(0, 5):
        lista.append(randint(1, 10))


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares, temos: {soma}')


numeros = list()
sortear(numeros)
somaPar(numeros)
print(numeros)








