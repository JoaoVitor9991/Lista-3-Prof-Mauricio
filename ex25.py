class Pessoa:
    def aqui(self, altura, peso):
        self.altura = altura 
        self.peso = peso  

    def calcular_imc(self):
        
        if self.altura <= 0:
            return "Altura inválida para cálculo do IMC."
        imc = self.peso / (self.altura ** 2)
        return imc


pessoa = Pessoa(altura=1.75, peso=70)


imc = pessoa.calcular_imc()
print(f"O IMC da pessoa é: {imc:.2f}")