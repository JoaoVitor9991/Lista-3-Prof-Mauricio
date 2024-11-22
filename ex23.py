class Salario():
    nome = "João Vitor"
    sal = 1200
    def calc_sal(self):
        aumento = self.sal * 0.1
        novo_salario = self.sal + aumento 
        return novo_salario
s = Salario()
salario_com_aumento = s.calc_sal()
print(f"O salário de {s.nome} com aumento é: R$ {salario_com_aumento:.2f}")

