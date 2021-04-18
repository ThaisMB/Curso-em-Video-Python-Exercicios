resposta = 'S'
contador = 0
soma = 0
maior = 0
menor = 0


while resposta=='S':

    n= float(input('Digite um número:'))

    contador += 1
    soma += n

    if contador==1:
        maior = n 
        menor = n
    
    elif maior<=n:
       maior = n

    elif menor>n:
        menor=n

    

    resposta = input('Deseja continuar? [S / N]').upper()

média = soma/contador

print('Você digitou {} números e a média foi {}.'.format(contador, média))
print('O maior valor foi {} e o menor valor foi {}.'.format(maior, menor))
