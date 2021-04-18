lista = []
pares = []
impares = []

while True:

    n = int(input('Digite um número:'))

    lista.append(n)

    if n%2==0:

        pares.append(n)

    else:

        impares.append(n)

    escolha = input('Deseja continuar? [S/ N]').upper()

    if escolha == 'N':
        break

print('-='*50)

lista.sort()
pares.sort()
impares.sort()


print(f'A lista completa é {lista}.')
print(f'A lista de pares é {pares}.')
print(f'A lista de ímpares é {impares}.')



