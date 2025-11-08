frase = str(input('Digite seu nome completo: ')).strip().upper()
print(f'Seu nome completo é: {frase}')
print(f'Seu primeiro nome é: {frase.split()[0]}')
print(f'Seu ultimo nome é: {frase.split()[-1]}')

