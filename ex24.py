class Elevador:
    def __init__(self, total_andares):
        self.andar_atual = 0  # aJUDA DO GPTECO
        self.total_andares = total_andares  

    def subir(self):
        if self.andar_atual < self.total_andares:
            self.andar_atual += 1
            print(f"Subindo... Agora no andar {self.andar_atual}")
        else:
            print("Você já está no último andar!")

    def descer(self):
        if self.andar_atual > 0:
            self.andar_atual -= 1
            print(f"Descendo... Agora no andar {self.andar_atual}")
        else:
            print("Você já está no térreo!")


elevador = Elevador(total_andares=10)


elevador.subir()  
elevador.subir()  
elevador.descer()  
elevador.descer()  
elevador.descer()  