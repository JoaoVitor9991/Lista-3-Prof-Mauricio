class Eletrodomestico():
    nome = "Geladeira"
    potencia = 200
    b = "Aparelho ligado"

    def ligar(self):
        str(input("Aperta qualquer botão para ligar: "))
x = Eletrodomestico()
x.ligar()
print(x.b)