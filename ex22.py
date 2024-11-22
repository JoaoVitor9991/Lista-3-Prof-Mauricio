class Agenda:
    def xd (self):
        self.contatos = []  

    def adicionar_contato(self, nome, telefone):
        contato = {"nome": nome, "telefone": telefone}
        self.contatos.append(contato)
        print(f"Contato {nome} adicionado com sucesso!")

    def listar_contatos(self):
        if not self.contatos:
            print("A agenda está vazia.")
        else:
            print("Contatos na agenda:")
            for i, contato in enumerate(self.contatos, start=1):
                print(f"{i}. Nome: {contato['nome']}, Telefone: {contato['telefone']}")


agenda = Agenda()
agenda.adicionar_contato("João", "1234-5678")
agenda.adicionar_contato("Maria", "9876-5432")
agenda.listar_contatos()