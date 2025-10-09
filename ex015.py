A = int(input("Por quantos dias o carro foi alugado ?"))
Km = float(input("Quantos km rodados ?"))
kmr = Km * 0.15
D = A * 60
Total = kmr + D
print(f'O total a pagar é de R${Total:.2f}')

