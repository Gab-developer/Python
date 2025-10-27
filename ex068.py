import random
print('=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*15)
valor = int(input('Diga um valor: '))
escolha = str(input('Par ou Impar? [P/I]: ').upper())
computador = random.randint(0, 11)
soma = computador + valor
print(f'Você escolheu {valor} e o computador escolheu {computador}. A soma deu {soma}')
if escolha == 'P':
    if soma % 2 == 0:
        print('Você Venceu!!')
    else:
        print('Você perdeu!')
if escolha == 'I':
    if soma % 2 == 0:
        print('Você Perdeu!')
    else:
        print('Você Ganhou!!')