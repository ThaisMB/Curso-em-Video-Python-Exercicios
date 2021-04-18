contagem = ('zero', 'un', 'deux', 'trois', 'quatre', 'cinq', 'six', 'sept','huit', 'neuf', 'dix','onze', 'douze', 'treize', 'quatorze', 'quinzze', 'seize','dix-sept', 'dix-huit', 'dix-neuf', 'vingt')

n= int(input('Entrez un nombre entre 0 et 20:'))

if 0>n or n>20:
    n = int(input('Réessaye!Entrez un nombre entre 0 et 20:'))

print(f'Vouz avez entré le nombre {contagem[n]}!')