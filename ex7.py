class Produto():
    nome = "Arroz"
    preco = 50 
    def desconto(self):
        Desconto = self.preco - 5
        print(Desconto)
a = Produto()
a.desconto()