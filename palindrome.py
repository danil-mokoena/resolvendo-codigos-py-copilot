# Programa para verificar se uma palavra é um palíndromo

# Entrada de dados
palavra = input("Digite uma palavra: ")

# Processamento — inverter a string
palavra_invertida = palavra[::-1]

# Comparação entre a palavra original e a invertida
if palavra.lower() == palavra_invertida.lower():
    print("A palavra é um palíndromo!")
else:
    print("A palavra não é um palíndromo.")