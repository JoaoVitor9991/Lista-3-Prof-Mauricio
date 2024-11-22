class Livro():
    titulo= "Anjo da Noite"
    autor = "Bryant Walker"
    def exibir(self):
        print(f"Autor: {self.autor} Titulo: {self.titulo}")
seila = Livro()
seila.exibir()