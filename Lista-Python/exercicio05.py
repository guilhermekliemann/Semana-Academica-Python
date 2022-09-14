#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

notas = []
media = 0.0

for i in range(4):
    msg = float(input("Nota: "))
    notas.append(msg)
    media += notas[i]
    
print("Média das notas:", media/4)