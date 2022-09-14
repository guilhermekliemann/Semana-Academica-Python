# Classe Pessoa: Crie uma classe que modele uma pessoa:
# Atributos: nome, idade, peso e altura
# Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que 
# nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        
    def envelhecer(self):
        print("\nEnvelhecer!")
        self.idade += 1
    
    def engordar(self):
        print("\nEngordar!")
        self.peso += 1.0
    
    def emagrecer(self):
        print("\nEmagrecer!")
        self.peso -= 1.0
        
    def crescer(self):
        print("\nCrescer!")
        if(self.idade < 21): 
            self.altura += 5
    
pessoa1 = Pessoa('Guilherme', 19, 70.0, 185)

print("Nome:", pessoa1.nome, "\nIdade:", pessoa1.idade, "anos\nPeso:", pessoa1.peso, "kg\nAltura:", pessoa1.altura, "cm")  

pessoa1.envelhecer()
pessoa1.engordar()
pessoa1.engordar()
pessoa1.engordar()
pessoa1.emagrecer()
pessoa1.crescer()

print("\nNome:", pessoa1.nome, "\nIdade:", pessoa1.idade, "anos\nPeso:", pessoa1.peso, "kg\nAltura:", pessoa1.altura, "cm")      