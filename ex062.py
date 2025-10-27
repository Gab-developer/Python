print('Gerador de PA')
print('=-'*10)
primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro_termo
cont = 1
quantidade_de_termos = 10
while True:
    print('{}'.format(termo),end='')
    print(' -> ' if cont < quantidade_de_termos else ' PAUSA ', end='')
    termo = termo + razao
    cont += 1
    if cont >= quantidade_de_termos:
        cont = 0
        segunda = int(input('\nQuais termos você quer mostrar?: '))
        quantidade_de_termos = segunda
        if quantidade_de_termos == 0:
            break
print('Fim do programa!')