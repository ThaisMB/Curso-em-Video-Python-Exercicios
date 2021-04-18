def ficha(nome_jog='<desconhecido>', num_gols=0):
    if nome_jog=='':
        nome_jog='<desconhecido>'
    if num_gols=='':
        num_gols=0
    print(f'O jogador {nome_jog} fez {num_gols} gol(s) no campeonato.')




nome=str(input('Nome do Jogador:')).strip()
gols=str(input('Número de Gols:')).strip()
if gols.isnumeric():
    gols=int(gols)
ficha(nome, gols)