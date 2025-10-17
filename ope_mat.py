#Vamos solicitar como entrada depois números, e depois vamos executar operações matemáticas simples.

#Números:
num1 = int(input ("Digite o primeiro número: "))
num2 = int(input ("Digite o segundo número: "))

#Operação:
operacao = input("Digite a operação matemática desejada (+, -, * ou /): ")

#Variáveis:
if operacao == '+':
    print(num1 + num2)
elif operacao == '-':
    print(num1 - num2)
elif operacao == '*':
    print (num1 * num2)
elif operacao == '/':
    print (num1 / num2)  
else: 
    print("Operação Inválida!")