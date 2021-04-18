produtos = ('livro', 50.00, 'caderno', 30.00, 'lápis', 3.00, 'lapis de cor', 20.00, 'papel sulfite', 18.00, 'grampeador', 8.00)

print('-'*40)
print('     LISTAGEM DE PRODUTOS')
print('-'*40)

for cont in range(0, len(produtos)):

    if cont%2==0:

        print(f'{produtos[cont]:.<30}',end = '')

    else:

        print(f'R${produtos[cont]:>6.2f}')

print('-'*40)
