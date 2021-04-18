lista = []

while True:
 
    n =  (int(input('Digite um número:')))

    if n in lista:
        print('Valor duplicado!Não vou adicionar...')

    else:
        print('Valor adicionado com sucesso...')
        lista.append(n)

    escolha = input('Deseja continuar? [S/N]').upper()

    if escolha == 'N':
        break

print('-='*50)

lista.sort()

print('Você digitou os valores{}.'.format(lista))