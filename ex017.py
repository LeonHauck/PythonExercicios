import math

# Solicita a entrada do usuário para os comprimentos dos catetos
cateto_oposto = float(input('Digite o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Digite o comprimento do cateto adjacente: '))

# Calcula a hipotenusa usando o teorema de Pitágoras
# Hipotenusa^2 = Cateto Oposto^2 + Cateto Adjacente^2
# Hipotenusa = sqrt(Cateto Oposto^2 + Cateto Adjacente^2)
hipotenusa = math.sqrt(cateto_oposto**2 + cateto_adjacente**2)

# Mostra o resultado
print(f'O comprimento da hipotenusa é: {hipotenusa:.2f}')
