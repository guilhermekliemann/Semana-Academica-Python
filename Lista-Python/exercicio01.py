#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

tempC = float(input("Digite a temperatura em graus Celsius: "))

def calcF(tempC):
    return float((tempC * 1.8) + 32)

print("Temperatura em graus Fahrenheit:",calcF(tempC))