peso = 0

maior = 0

menor = 500

for c in range (1,6):

    peso = float(input('Qual o peso da {}º pessoa? (kg)'.format(c)))

    if peso>maior:

        maior = peso

    elif peso<menor:

        menor = peso

print('O maior peso lido foi de {} kg.'.format(maior))

print('O menor peso lido foi de {} kg.'.format(menor))

