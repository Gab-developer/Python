sexo = str(input('Qual seu sexo? [M/F]: '))
b = sexo.upper()
z = b[0]
sexo = z
while sexo not in 'MmFf':
    a = input('Dado inválido... Tente novamente!: ')
    b = a.upper()
    z = b[0]
    sexo = z
print('Sexo {} registrado com sucesso!'.format(sexo))
