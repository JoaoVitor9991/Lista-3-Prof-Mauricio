class Altura():
    altura = 1,75

    def verificar(self):
        o = float(input("Digite a sua altura: "))
        if o > 1.75:
            print("Você é mais alto que 1.75. ")
        else:
            print("Você não é maior que 1.75.")

a= Altura()
a.verificar()

