maiores = 0
homens = 0
m20 = 0

while True:

    print('-'*30)
    print('     CADASTRE UMA PESSOA')
    print('-'*30)

    idade = int(input('Idade:'))
    sexo = input('Sexo: [M / F]').upper()

    if sexo == 'M':
        homens += 1

    elif sexo == 'F' and idade<20:
        m20 += 1

    if idade>18:
        maiores += 1
    

    print('-'*30)
    escolha = input('Deseja continuar? [S / N]').upper()

    if escolha=='N':
        print(f'Total de pessoas maiores de 18 anos:{maiores}')
        print(f'Ao todo, temos {homens} homens cadastrados.')
        print(f'E temos {m20} mulheres com menos de 20 anos.')
        break

