total = 0
mmil= 0
quantidade=0

print('--'*30)
print('     \033[34mLOJA BARATÃO\033[m')
print('--'*30)
  
while True:

    nome = input('Digite o nome do produto:')
    preço = float(input('Preço:R$'))

    total += preço
    quantidade += 1

    if quantidade == 1:
        menor = preço

    if preço>1000:
        mmil+=1

    if preço<menor:
        menor = preço
        barato = nome

    escolha = input('Deseja continuar? [S / N]').upper()

    if escolha !='S':
        print(f'O total das compras foi R${total :.2f}.')
        print(f'Temos {mmil} produtos custando mais de R$1000.00.')
        print(f'O produto mais barato foi {barato} que custa R${menor :.2f}.')
        break


   