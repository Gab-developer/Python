frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes'.format(frase.count('A')))
print('A primeira Letra A aparece na posição {}'.format(frase.find('A')+1))
print('A última letra A esta na posição {}'.format(frase.rfind('A')+1))
