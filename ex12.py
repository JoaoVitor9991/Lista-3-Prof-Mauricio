class Filme():
    titulo = "Senhor Dos Anéis"
    duracao = 8
    def exibir(self):
        print(f"Título: {self.titulo} Duração: {self.duracao} Horas")
a = Filme()
a.exibir()