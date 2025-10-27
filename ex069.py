cont = 0
while True:
    cont += 1
    print('-'*30)
    print('CADASTRE UMA PESSOA!')
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: '.upper())
    print('-'*30)
    escolha = input('Deseja continuar? [S/N]: '.upper())
    if escolha == 'N':
        break
if idade < 18:
    cont = cont - 1
if sexo == 'F':
    cont = cont - 1
print(f'NO total, você cadastrou {cont} pessoas')
print(f'{cont} tem mais de 18 anos')
print(f'Ao todo, foram cadastrados {cont} Homen(s)')