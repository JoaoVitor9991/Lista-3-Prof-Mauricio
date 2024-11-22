class Data():
    data = 20
    mes = 11 
    ano = 2024
    def formatar(self):
        print(f"{self.data}/{self.mes}/{self.ano}")
v = Data()
v.formatar()