# Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. 
# A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo.
# Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é 
# opcional, com valor default zero e os demais atributos são obrigatórios.

class ContaCorrente:
    def __init__(self, numeroConta, nomeCorrentista, saldo = 0):
        self.numeroConta = numeroConta
        self.nomeCorrentista = nomeCorrentista
        self.saldo = saldo
        
    def alterarNome(self):
        nome = input("Digite o novo nome: ")
        self.nomeCorrentista = nome
        
    def deposito(self):
        valor = float(input("Digite um valor para depositar: "))
        if(valor > 0):
            self.saldo += valor
        else:
            print("Valor inválido!")
        
    def saque(self):
        valor = float(input("Digite um valor para saque: "))
        if(valor < self.saldo):
            self.saldo -= valor
        else:
            print("Erro ao sacar dinheiro!")
            
cc1 = ContaCorrente(159, 'Guilherme')

cc1.alterarNome()
cc1.deposito()
cc1.saque()

print("\nNúmero da Conta:", cc1.numeroConta, "\nNome do Correntista:", cc1.nomeCorrentista, "\nSaldo:", cc1.saldo)
    
        