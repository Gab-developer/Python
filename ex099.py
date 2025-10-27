from time import sleep
def maior(*num):
    print('=-'*30)
    print('Analisando os valores passados...')
    sleep(1)
    print(f'{num} Foram informados {len(num)} valores no total!')
    maximo = max(num)
    print(f'O maior valor é o {maximo}')


maior(2, 4, 2, 6 ,4 ,8)
maior(2, 4, 3, 2)
maior(1, 3)
maior(10)
