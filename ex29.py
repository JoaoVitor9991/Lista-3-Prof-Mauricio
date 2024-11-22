class Jogo:
    def __init__(self, nome):
        self.nome = nome  
        self.pontuacao = 0  

    def iniciar(self):
        print(f"O jogo '{self.nome}' foi iniciado!")
        self.pontuacao = 0  

    def registrar_pontuacao(self, pontos):
        if pontos < 0:
            print("A pontuação não pode ser negativa!")
            return
        self.pontuacao += pontos
        print(f"{pontos} pontos adicionados! Pontuação total: {self.pontuacao}")

    def exibir_pontuacao(self):
        print(f"A pontuação atual no jogo '{self.nome}' é: {self.pontuacao}")