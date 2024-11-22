class Animal:
    def __init__(self, nome, tipo_mov):
        self.nome = nome  
        self.tipo_movimento = tipo_mov  

    def mover(self):
        print(f"O {self.nome} {self.tipo_movimento}.")