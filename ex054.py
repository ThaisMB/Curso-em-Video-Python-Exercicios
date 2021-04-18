from datetime import date

maiores = 0
menores = 0

for c in range (1,8):

    ano=int(input('Em que ano a {}º nasceu?'.format(c)))

    atual= date.today().year

    if atual-ano>21:
        maiores += 1

    else:
        menores += 1

print('Ao todo tivemos {} pessoas maiores de idade.'.format(maiores))

print('E também tivemos {} pessoas menores de idade.'.format(menores))
