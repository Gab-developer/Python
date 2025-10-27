from time import sleep


def contador(i, f, p):
    for c in range(i, f, p):
        print(c, end=' ')
        sleep(0.3)
    print()


print('=-'*20)
print('Contagem de 1 até 10 indo de 1 em 1:')
contador(1, 11, 1)
print('=-'*20)
print('Contagem de 10 até 0 indo de 2 em 2:')
contador(10, -2, -2)
print('Agora, personalize a SUA contagem!: ')
inicio = int(input('Início: '))
final = int(input('Final: '))
passo = int(input('Passo: '))
print('=-'*20)
print(f'Contagem de {inicio} até {final} indo de {passo} em {passo}')
contador(inicio, final, passo)