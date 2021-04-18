velocidade= int(input('Qual a velocidade atual do carro?'))

if velocidade<=80:
    print("Tenha um bom dia! Dirija com segurança!")

else:
    multa= (velocidade-80)*7

    print("""MULTADO!Você excedeu o limite de velocidade que é 80 km/h.
    Você deve pagar uma multa de R${:.2f}!""".format(multa))