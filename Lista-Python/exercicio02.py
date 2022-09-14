#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

h = float(input("Qual a sua altura: "))
sexo = input("Qual o seu sexo(M ou F): ")

def calcIMC(h, sexo):
    if(sexo == 'M'):
        return (72.7 * h) - 58
    else:
        return (62.1 * h) - 44.7

print(calcIMC(h, sexo))