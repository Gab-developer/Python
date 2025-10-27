ano = int(input('Em que ano você nasceu? '))
idade = 2023 - ano
oito = 18 - idade
alistamento = 2023 + oito
if idade == 18:
    print('\033[0;31mALISTE-SE IMEDIATAMENTE!!!')
elif idade > 18:
    print('Pendente com o serviço militar!')
else:
    print('Quem nasceu em {} ano tem {} anos de idade'.format(ano, idade))
    print('Ainda faltam {} anos para o seu alistamento!'.format(oito))
    print('Seu alistamento vai ser no ano de {}'.format(alistamento))
