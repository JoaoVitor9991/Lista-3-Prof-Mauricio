class Temperatura():
    def converter(self, c):
        f = (c * 9/5) + 32
        return f
temp = Temperatura()
temp_c = float(input("Digite o grau: "))
temp_f = temp.converter(temp_c)
print(f"A temperatura em Farhenheit é {temp_f}")
