somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ""
totmulher20 = 0
for p in range(1, 5):
    print('----- {}° PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('[M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 =+ 1
mediaidade = somaidade / 4
print('A média de idade do grupo é de {:.1f} anos.'.format(mediaidade))
print('O homem mais velho tem {} anos e seu nome é {}.'.format(maioridadehomem, nomevelho))
if totmulher20 == 1:
    print('Ao todo, é apenas {} mulher com menos de 20 anos.'.format(totmulher20))
else:
    print('Ao todo, são {} mulheres com menos de 20 anos.'.format(totmulher20))
