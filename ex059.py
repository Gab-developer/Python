p1 = int(input('Primeiro valor: '))
p2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [1] Soma
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
opcao = int(input('Qual é sua opção?: '))
if opcao == 1:
    p3 = p1 + p2
    print('A soma desses números resulta em {}'.format(p3))
elif opcao == 2:
    p3 = p1 * p2
    print('A multiplicação desses números resulta em {}'.format(p3))
elif opcao == 3:
    if p1 > p2:
        print('O maior número é o {}'.format(p1))
    else:
        print('O maior número é o {}'.format(p2))
elif opcao == 4:
    print('Digie os números novamente:')
    p1 = int(input('Primeiro valor: '))
    p2 = int(input('Segundo valor: '))
elif opcao == 5:
    print('Finalizando o programa...')
else:
        print('Esse número é inválido, Tente novamente.')
print(' Fim do programa ')