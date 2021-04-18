num = []

num.append(int(input('Digite um valor:')))
print('Valor adicionado ao final da lista...')

n1 = int(input('Digite um valor:'))
num.insert(0,n1)
print('Valor adicionado na posição 0 da lista...')

n2 = int(input('Digite um valor:'))
num.insert(1,n2)
print('Valor adicionado na posição 1 da lista...')

num.append(int(input('Digite um valor:')))
print('Valor adicionado ao final da lista...')

n3 = int(input('Digite um valor:'))
num.insert(0,n3)
print('Valor adicionado na posição 0 da lista...')

print('-='*50)

print(f'Os números digitados em ordem foram {num}.')
