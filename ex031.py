distancia= int(input("Qual a distância da viagem?"))

if distancia<200:
    passagem= distancia*50/100
else:
    passagem= distancia*45/100

print("Você está prestes a começar um viagem de {} quilômetros.".format(distancia))
print("Sua passagem custará R${:.2f}.".format(passagem))