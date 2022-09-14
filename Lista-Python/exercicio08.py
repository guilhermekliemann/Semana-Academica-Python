# Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):
# Atributos: Nome, Fome, Saúde e Idade b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade
# Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi, este humor 
# é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo 
# para armazenar esta informação por que ela pode ser calculada a qualquer momento.

class BichinhoVirtual:
    def __init__(self, nome, humor = None, fome = 100, saude = 100, idade = 1):
        self.nome = nome
        self.humor = humor
        self.fome = fome
        self.saude = saude
        self.idade = idade
    
    def alterar(self):
        ent = input("Qual atributo você deseja alterar: ")
        if ent == 'nome':
            aux = input("Digite um novo nome: ")
            self.nome = aux
        elif ent == 'fome':
            aux = int(input("Digite a nova fome: "))
            self.fome = aux
        elif ent == 'saude':
            aux = int(input("Digite a nova saude: "))
            self.saude = aux
        elif ent == 'idade':
            aux = int(input("Digite a nova idade: "))
            self.idade = aux
        else:
            print("Atributo inválido!")            
    
    def retornar(self):
        ent = input("Qual atributo você deseja retornar: ")
        if ent == 'nome':
            print("Nome:",self.nome)
        elif ent == 'humor':
            print("Humor:", self.humor)
        elif ent == 'fome':
            print("Fome:", self.fome)
        elif ent == 'saude':
            print("Saude:", self.saude)
        elif ent == 'idade':
            print("Idade:", self.idade)
        else:
            print("Atributo inválido!")
            
    def calcHumor(self):
        if self.fome > 50 and self.saude > 50:
            self.humor = "Feliz"
        else:
            self.humor = "Triste"
                         
bv1 = BichinhoVirtual('Bardo')

bv1.calcHumor()
print("\nNome:", bv1.nome, "\nHumor:", bv1.humor, "\nFome:", bv1.fome, "\nSaude:", bv1.saude, "\nIdade:", bv1.idade, "\n")

bv1.alterar()
bv1.retornar()

bv1.calcHumor()