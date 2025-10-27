import time
def ajuda(com):
    help(com)
    time.sleep(0.3)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)


# Programa principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA pyHELP')
    comando = str(input('Comando ou biblioteca --> '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Até logo!')