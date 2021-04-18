lista = (int(input('Digite um número:')), 
int(input('Digite outro número:')),
int(input('Digite mais um número:')), 
int(input('Digite o último número:')))



print(f'Você digitou os valores {lista}.')

print(f'O valor 9 aparece {lista.count(9)} vezes.')


if 3 in lista:
    print('O valor 3 apareceu na {}ª posição.'.format(lista.index(3)+1))
else:
    print('O número 3 não foi digitado.')


print('Os valores pares digitados foram',end = ' ')

for n in lista:
    if n%2==0:
        print(n, end = ' ')

print('.')

 


