velo = int(input('Qual a velocidade que o carro estava em Km: '))
multa = (velo - 80) * 7
if velo <= 80:
    print('Está tudo certo!')
else:
    print('Você foi multado')
    print('A sua multa foi de {} reais'.format(multa))
