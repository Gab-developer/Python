while True:
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro: '))
    print(
    '''    [1] Soma
        [2] Subtração
        [3] Multiplicação
        [4] Divisão'''
    )
    ask = int(input('Digite uma opção: '))

    if ask == 1:    
        r = n1 + n2
        print(f'A soma entre {n1} e {n2} é {r}')
        dnv = input('Deseja fazer outra conta [S/N]: ')
        if dnv == 'N':
            break

    elif ask == 2:
        r = n1 - n2
        print(f'A subtração entre {n1} e {n2} é {r}')
        dnv = input('Deseja fazer outra conta [S/N]: ')
        if dnv == 'N':
            break

            
    elif ask == 3:
        r = n1 * n2
        print(f'A multiplicação entre {n1} e {n2} é {r}')
        dnv = input('Deseja fazer outra conta [S/N]: ')
        if dnv == 'N':
            break
            

    elif ask == 4:
        if n1 > n2:
            r = n1 / n2
            print(f'A divisão entre {n1} e {n2} é {r}')
        if n1 == n2:
            print('O resultado é 1')
        else:
            print(f'{n1} não pode ser dividido por {n2}')
            dnv = input('Deseja fazer outra conta [S/N]: ')
            if dnv == 'N':
                break
