n1= int(input("Primeiro valor:"))
n2= int(input("Segundo valor:"))
n3= int(input("Terceiro valor:"))

if n1>n2:

    maior = n1
    menor = n2
else:

    maior = n2
    menor = n1

if maior < n3:
    
    maior = n3

if menor > n3:

    menor = n3

print("O maior valor digitado foi {}.".format(maior))
print("O menor valor digitado foi {}".format(menor))
