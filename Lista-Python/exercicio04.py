#Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

vet1 = [0,1,2,3,4,5,6,7,8,9]
vet2 = [9,8,7,6,5,4,3,2,1,0]
vet3 = [5,7,3,8,2,7,3,7,4,5]
vet4 = []

for i in range(10):
    vet4.append(vet1[i])
    vet4.append(vet2[i])
    vet4.append(vet3[i])
    
print(vet4)