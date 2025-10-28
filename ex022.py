nome = str(input('Digite seu nome:'))
print(f'{nome}')
nome = nome.strip()
print(f'Seu nome em maiúsulas é {nome.upper()}')
print(f'Seu nome em minúscualas é {nome.lower()}')
print(f'Seu nome ao todo tem {len(nome) - nome.count(" ")} letras.')
print(f'Seu primeiro nome tem {nome.find(' ')} letras.')


