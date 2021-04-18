a1 = 0
a2 = 1

print('-'*30)

print('     SEQUÊNCIA DE FIBONACCI')

print('-'*30)

contador = int(input('Quantos termos você quer mostrar?'))

print(a1,'-', end =' ')
print(a2, '-', end = ' ')

while contador>2:

    n= a1+a2

    print(n, end=' ')

    print('-', end=' ')

    a1 = a2

    a2 = n

    contador = contador-1

print('FIM')
