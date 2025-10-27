from random import randint
computador = randint(0, 10)
print('Sou seu computador!')
print('Acabei de pensar em um número de 1 à 10!')
print('Será que você consegue descobrir qual é?')
acertou = False
qnts = 0
while not acertou:
    palpite = int(input('Qual é o seu palpite?: '))
    qnts += 1
    if palpite == computador:
        acertou = True
    else:
        if palpite < computador:
            print('Mais... Tente novamente: ')
        else:
            print('Menos... Tente novamente: ')
print('Parabéns, você acertou com {} palpites!'.format(qnts))
