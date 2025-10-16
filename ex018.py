import math

# Solicita o ângulo ao usuário
graus = float(input('Digite o ângulo em graus: '))

# Converte o ângulo de graus para radianos
radianos = math.radians(graus)

# Calcula o seno, cosseno e tangente
seno = math.sin(radianos)
cosseno = math.cos(radianos)
tangente = math.tan(radianos)

# Exibe os resultados formatados
print(f'O seno de {graus}° é aproximadamente {seno:.2f}')
print(f'O cosseno de {graus}° é aproximadamente {cosseno:.2f}')
print(f'A tangente de {graus}° é aproximadamente {tangente:.2f}')
