numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro',
           'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
           'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze',
           'Quinze', 'Desseseis', 'Dessesete', 'Dezoito',
           'Dezenove', 'Vinte')
while True:
    num = int(input('Digite um número de 0 à 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente. ',end='')
print(f'Você digitou o número {numeros[num]}')