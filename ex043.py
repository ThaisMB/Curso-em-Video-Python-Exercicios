peso=float(input('Qual seu peso? (kg)')) 
altura= float(input('Qaul sua altura? (m)'))

IMC= peso/(altura**2)

print('O IMC dessa pessoa é de {:.2f}.'.format(IMC))

if IMC<18.5:
    print('Você está ABAIXO DO PESO!')

elif 18.5 <=IMC< 25:
    print('PARABÉNS! Você está na faixa de peso IDEAL!')

elif 25 <=IMC< 30:
    print('Você está em SOBREPESO!')

elif 30<=IMC<40:
    print('Você está em OBESIDADE!')

else:
    print('CUIDADO! Você está em OBESIDADE MÓRBIDA!')