#Faça uma função que ordene uma lista(de qualquer tamanho) de números inteiros de forma crescente

vet = [6,9,7,10,3,5,1,4,7,8,2]

def bubbleSort(vet):
    aux = None
    for i in range(1, 10):
        for j in range(0, 10):
            if(vet[j] > vet[j+1]):
                aux = vet[j]
                vet[j] = vet[j+1]
                vet[j+1] = aux
          
print("Lista não ordenada:")
print(vet)
      
bubbleSort(vet)

print("\Lista ordenada:")
print(vet)