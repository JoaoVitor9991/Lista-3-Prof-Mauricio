class Aluno():
    nome = "João Vitor"
    nota = 10
    def amedia(self):
        if self.nota >=7:
            print(f"{self.nome} está aprovado.")
        else:
            print(f"{self.nome} está reprovado. ")
a = Aluno()
media = a.amedia()

