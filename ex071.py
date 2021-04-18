print('='*30)
print('     BANCO CEV')
print('='*30)

valor = int(input('Qual valor você quer sacar?R$'))

notas50 = valor//50

resto50 = valor%50

notas20 = (resto50)//20

resto20 = resto50%20

notas10 = (resto20)//10

resto10 = resto20%10

notas1 = resto10//1


if notas50>0:

    print(f'Total de {notas50} de cédulas de R$50.00')

if notas20>0:

    print(f'Total de {notas20} de cédulas de R$20.00')

if notas10>0:

    print(f'Total de {notas10} de cédulas de R$10.00')

if notas1>0:

    print(f'Total de {notas1} de cédulas de R$1.00')

print('='*30)
print('Volte sempre ao BANCO CEV!Tenha um bom dia!')