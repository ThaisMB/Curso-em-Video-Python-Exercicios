frase = input('Digite uma frase:')

split = frase.split()


junto = ''.join(split).upper()

inverso = junto[len(junto)::-1]

print('A frase {} escrita ao contrário fica {}.'.format(junto,inverso))

if junto==inverso:

    print('A frase "{}" é um PALÍNDRMO!'.format(frase))

else:

    print('A frase "{}" NÃO É um PALÍNDROMO!'.format(frase))