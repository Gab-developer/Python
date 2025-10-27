perfil = {}
lista = []
cont = soma = 0
listamulheres = []
listaacima = []
while True:
    perfil.clear()
    perfil['nome'] = str(input('Nome: '))
    perfil['idade'] = int(input('Idade: '))
    soma += perfil['idade']
    perfil['sexo'] = str(input('Sexo [M/F]: ')).upper()
    if perfil['sexo'] in 'fF':
        listamulheres.append(perfil['nome'])
    cont += 1
    lista.append(perfil.copy())
    opcao = str(input('Deseja continuar? [S/N]: '))
    if opcao in 'nN':
        break
media = soma / len(lista)
if perfil['idade'] > media:
    listaacima.append(perfil['nome'])
print('-='*30)
print(f'A) No total, foram cadastradas {cont} pessoas')
print(f'B) A média das idades é de {media:.1f}')
print(f'C) As mulheres cadastradas foram {listamulheres}')
print(f'D) Pessoas que estão acima da média:'
      f'{listaacima}')


