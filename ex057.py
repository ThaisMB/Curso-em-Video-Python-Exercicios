sexo = input('Informe seu sexo: [M / F]').upper()



while sexo!='F' and sexo!='M':

    sexo = input('Dados inválidos. Por favor, informe seu sexo:').upper()

print('Sexo {} registrado com sucesso'.format(sexo))
