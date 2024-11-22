class Banco():
    saldo = 1000
    def depositar(self):
        mm =float(input(("Digite o valor que gostaria de depositar: ")))
        self.saldo + mm 

    def sacar(self):
        oi = float(input("Digite a quantidade que deseja sacar: "))
        self.saldo = self.saldo - oi
a = Banco()
a.depositar()
a.sacar()
