contador = 0
somador = 0

while True:

    n= int(input('Digite um número:'))

    if  n==999:
        break

    contador +=1
    somador += n

print(f'Você digitou {contador} números e a soma deles é {somador}.')


