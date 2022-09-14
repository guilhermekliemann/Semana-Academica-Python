# Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser 
# compostos pelos elementos intercalados dos dois outros vetores.

vet1 = [0,1,2,3,4,5,6,7,8,9]
vet2 = [9,8,7,6,5,4,3,2,1,0]
vet3 = []

for i in range(10):
    vet3.append(vet1[i])
    vet3.append(vet2[i])
    
print(vet3)