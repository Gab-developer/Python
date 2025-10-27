def fatorial(num, show=False):
    """
    --> Calcula o valor do fatorial de um número!
    :para num: Número que você deseja saber o fatorial
    :para show: Comando (opcional) para ver o cálculo da conta!
    :return: O valor do fatorial de um número "n"
    """
    f = 1
    print('=-'*15)
    for c in range(num, 0, -1):
        if show == True:
            print(c, end='')
            if c > 1:
                print(' X ', end='')
            else:
                print(' = ',end='')
        f *= c
    return f


numer = int(input('Qual fatorial você deseja?: '))
print(fatorial(numer, show=True))