def leiaint(msg):
    while True:
        valor = 0
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            break
        else:
            print('\033[0;31mERRO: Digite um valor inteiro!\033[m')
    return valor


n = leiaint('Digite um Inteiro: ')
print(f'Você acabou de digitar o número {n}')


def leiaFloat(msg):
    while True:
        valor = 0
        n = str(input(msg))
        if n.isdecimal():
            valor = int(n)
            print(f'Você acabou de digitar o número {n}')
            break
        else:
            print('\033[0;31mERRO: Digite um valor real!\033[m')
    return valor


n = leiaFloat('Digite um Real: ')
