class Livro:
    def __init__(self, titulo, autor, preco, estoque):
        self.titulo = titulo
        self.autor = autor
        self.preco = preco
        self.estoque = estoque  

    def adicionar_estoque(self, quantidade):
        if quantidade > 0:
            self.estoque += quantidade
            print(f"{quantidade} unidades adicionadas. Estoque atual: {self.estoque}")
        else:
            print("Quantidade inválida para adicionar ao estoque.")

    def remover_estoque(self, quantidade):
        
        if 0 < quantidade <= self.estoque:
            self.estoque -= quantidade
            print(f"{quantidade} unidades removidas. Estoque atual: {self.estoque}")
        else:
            print("Quantidade inválida ou insuficiente no estoque.")

    def exibir_informacoes(self):
        print(f"Livro: {self.titulo}, Autor: {self.autor}, Preço: {self.preco}, Estoque: {self.estoque}")


livro = Livro("O ultimo suspiro", "João Armando", 39.90, 10)
livro.exibir_informacoes()
livro.adicionar_estoque(5)
livro.remover_estoque(3)
livro.exibir_informacoes()