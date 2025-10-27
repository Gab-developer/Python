from random import randint
from time import sleep
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''Sua opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogada = int(input('Qual é sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('O jogador escolheu {}'.format(itens[jogada]))
print('O computador escolheu {}'.format(itens[computador]))
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')
if computador == 0:
    if jogada == 0:
        print('\033[0;36mEMPATE!')
    if jogada == 1:
        print('\033[0;32mJogador ganha!')
    if jogada == 2:
        print('\033[0;31mComputador ganha!')
if computador == 1:
    if jogada == 1:
        print('\033[0;36mEMPATE!')
    if jogada == 0:
        print('\033[0;31mComputador ganha!')
    if jogada == 2:
        print('\033[0;32mJogador ganha!')
if computador == 2:
    if jogada == 2:
        print('\033[0;36mEMPATE!')
    if jogada == 0:
        print('\033[0;32mJogador ganha!')
    if jogada == 1:
        print('\033[0;31mComputador ganha!')
