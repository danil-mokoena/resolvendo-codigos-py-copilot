#Agora vamos solicitar uma string e um número inteiro como entrada. Depois, teremos que repetir a string o número de vezes retornado. 

string = input("Digite uma string: ")
numero = int(input("Digite um número inteiro: "))

#O código mais simples para a impressão do resultado seria este:
#print(string * numero)

#Porém, no código acima, o resultado sai sem espaços, o que torna o texto confuso. Para que seja impresso com espaçamento entre os resultados, podemos utilizar o seguinte código:
print((string + " ") * numero)