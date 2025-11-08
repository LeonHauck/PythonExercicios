frase = str(input('Digite uma frase: ')).strip().upper()
print(f'A frase tem {frase.count("A")} letras A')
print(f'A primeira letra A apareceu na posição {frase.find("A")+1}')
print(f'A ultima letra A apareceu na posição {frase.rfind("A")+1}')

