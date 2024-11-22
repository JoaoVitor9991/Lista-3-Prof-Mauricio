class Veiculo():
    modelo = "Ax345"
    velocidade = 200
    def aumentar(self):
        a_vel = float(input("Aumente a velocidade "))
        self.velocidade = self.velocidade + a_vel
        
x = Veiculo()
x.aumentar()
print(x.velocidade)