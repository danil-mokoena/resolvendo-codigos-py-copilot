# resolvendo-codigos-py-copilot
Bem-vindo ao meu repositório para o projeto: Resolvendo Códigos em Python da plataforma DIO utilizando, caso seja necessário, a plataforma Github Co-Pilot ou outra AI similar.

O projeto consiste em criar 5 arquivos em Python, cada qual com operações diferentes, para colocar em prática nossos conhecimentos em linguagem e lógica de programação, além de avaliar a assistência dada pelas AIs para codificação, quando aplicável e se necessária.

# 1 - Concatenando Dados 🐾
Descrição do desafio: Vamos receber dois dados diferentes do usuário e concatena-los em uma única string.

## 1.1 - O Desafio
Para este desafio, iremos concatenar dados de dois inputs diferentes. O código utilizado para definição dos inputs que iremos concatenar é:

```
info1 = input("Digite a primeira informação:")
info2 = input("Digite a segunda informação:")
```

Desta forma, definimos quais as informações que o sistema irá concatenar. Em seguida, utilizaremos a seguinte linha de código para concatenar as informações:
```
info_concatenada = info1 + " " + info2
```

Nota-se, também, o espaço entre as informações concatenadas, para que elas sejam exibidas de forma clara e legível. Por fim, foi confeccionada a seguinte linha de código para visualização da informação concatenada:
```
print("As informações concatenadas são: ", info_concatenada)
```

Com isso, teremos a visualização da concatenação das informações digitadas. Poderíamos, também, ter utilizado uma versão um pouco mais refinada e atual do código para visualização das informações, que seria:
```
print (f"As informações concatenadas são: {info1} {info2}")
```

O código final ficou com esta aparência:
```
#Vamos receber dois dados diferentes dos usuários e, depois disso, concatená-los.

info1 = input("Digite a primeira informação:")
info2 = input("Digite a segunda informação:")

info_concatenada = info1 + " " + info2

print("As informações concatenadas são: ", info_concatenada)

#Também poderíamos utilizar uma versão mais moderna e direta para alcançar o mesmo objetivo
#print (f"As informações concatenadas são: {info1} {info2}")
```

## 1.2 - Explicação Passo a Passo

🔹 1.2.1 - Entrada de dados
```
info1 = input("Digite a primeira informação: ")
info2 = input("Digite a segunda informação: ")
```
`input()` → exibe a mensagem na tela e espera que o usuário digite algo.
Tudo que o usuário digita é armazenado como string (texto).
Aqui, criamos duas variáveis:
- `info1` → guarda a primeira informação digitada pelo usuário
- `info2` → guarda a segunda informação digitada pelo usuário

🧩 Exemplo:<br>
- Usuário digita `Olá` → `info1 = "Olá"`<br>
- Usuário digita `Mundo` → `info2 = "Mundo"`

🔹 1.2.2 - Concatenação das informações
```
info_concatenada = info1 + " " + info2
```

- O operador `+` junta strings.<br>
- `" "` → adiciona um espaço entre as duas informações, para que não fiquem grudadas.

🧩 Exemplo:
```
info1 = "Olá"
info2 = "Mundo"
info_concatenada = "Olá" + " " + "Mundo" → "Olá Mundo"
```

🔹 1.2.3 - Exibição do resultado
```
print("As informações concatenadas são: ", info_concatenada)
```
- `print()` exibe o resultado na tela.
- O uso de `,` dentro do `print()` adiciona um espaço automático entre o texto fixo e a variável.

🖨️ Saída de exemplo: 
```
As informações concatenadas são:  Olá Mundo
```

🔹 1.2.4 - Versão moderna e direta (opcional)
```
print(f"As informações concatenadas são: {info1} {info2}")
```
`f-strings` permitem escrever o texto e inserir variáveis diretamente dentro das chaves `{}`.

O resultado será o mesmo, mas o código fica mais limpo e legível.

# 2 - Repetindo Textos ✏️
Descrição do desafio: Agora vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado.

## 2.1 O desafio
Para este desafio, iremos criar um texto que repete X vezes a string definida pelo usuário. O código para a definição da string que será repetida é:
```
string = input("Digite uma string: ")
```

Também criaremos um prompt para que o usuário decida quantas vezes ele deseja que o código seja repetido, com o input:
```
numero = int(input("Digite um número inteiro: "))
```

A impressão será feita através do código:
```
print((string + " ") * numero)
```

Desta forma, o código final que teremos, será:
```
# Agora vamos solicitar uma string e um número inteiro como entrada.
# Depois, teremos que repetir a string o número de vezes indicado pelo usuário.

# Entrada de dados
string = input("Digite uma string: ")
numero = int(input("Digite um número inteiro: "))

# Impressão do resultado com espaço entre as repetições
print((string + " ") * numero)
```

## 2.2 Explicação passo a passo
🔹 2.2.1. Entrada de dados (String)
```
string = input("Digite uma string: ")
```

`input()` → exibe a mensagem na tela e espera que o usuário digite algo.<br>
Tudo que o usuário digita é armazenado como string (texto). <br>
Aqui, a variável string guarda esse texto.

🧩 Exemplo:
Usuário digita → `"Oi"`
Agora string = `"Oi"`

🔹 2.2.2. Entrada de dados (número inteiro)
```
numero = int(input("Digite um número inteiro: "))
```
`input()` → pede ao usuário que digite algo.<br>
`int()` → converte o valor digitado em número inteiro, pois o `input()` retorna sempre texto.<br>
A variável numero guarda esse valor como número.<br>
<br>
🧩 Exemplo:<br>
Usuário digita → `3`<br>
Agora numero = `3`<br>
<br>
🔹 2.2.3. Impressão do resultado com repetição<br>
```print((string + " ") * numero)```<br>
`(string + " ")` → adiciona um espaço ao final da string, para separar as repetições.<br>
`* numero` → repete o conteúdo `(string + " ")` o número de vezes informado pelo usuário.<br>
`print()` → exibe o resultado na tela.<br>
<br>
🧩 Exemplo:<br>
string = "Oi"<br>
numero = 3<br>
(string + " ") * numero → "Oi " * 3 → "Oi Oi Oi "<br>
<br>
Resultado exibido:<br>
Oi Oi Oi <br>
<br>
🔹 2.2.4. Observação<br>
Se você usasse apenas `string * numero`, o resultado sairia sem espaços, ficando "OiOiOi".<br>
Por isso, adicionamos o `" "` dentro dos parênteses para separar as repetições.<br>
O espaço extra no final pode ser removido com `.strip()`, se quiser:<br>
`print(((string + " ") * numero).strip())`

# 3 - Operações Matemáticas Simples 📐
Descrição do desafio: Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

## 3.1 - O desafio:
Para este desafio, um exercício clássico de Python, onde aprenderemos a fazer uma simples calculadora, que realiza operações matermáticas simples, e de números inteiros, apenas.

```
#Números:
num1 = int(input ("Digite o primeiro número: "))
num2 = int(input ("Digite o segundo número: "))
```
Primeiramente, foram definidos os valores dos números inteiros para a nossa operação matemática.

```
#Operação:
operacao = input("Digite a operação matemática desejada (+, -, * ou /): ")
```
Depois, criamos o input para a operação matemática desejada.

```
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
```
Por fim, temos as nossas variáveis de operações matemáticas. Desta forma, conseguimos montar uma calculadora básica, que faz operações matemáticas simples, utilizando números inteiros. Sendo este o nosso primeiro contato com "elseif" ou "elif", no caso no Python.<br>
<br>
O código final acaba ficando com esta aparência:
```
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
```

## 3.2 🧠 Explicação passo a passo
🔹 3.21. Entrada dos números

```
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
```

`input()` → exibe a mensagem e espera que o usuário digite um valor.<br>
Por padrão, `input()` retorna texto (string).<br>
O comando `int()` converte o texto digitado em um número inteiro, permitindo fazer cálculos.<br>
Os valores são armazenados nas variáveis `num1` e `num2`.<br>
<br>
🧩 Exemplo:<br>
Usuário digita:<br>
Digite o primeiro número: 10<br>
Digite o segundo número: 5<br>
<br>
Agora:<br>
num1 = 10<br>
num2 = 5<br>
<br>
🔹 3.2.2. Entrada da operação desejada<br>
```
operacao = input("Digite a operação matemática desejada (+, -, * ou /): ")
```
Essa linha solicita ao usuário qual operação matemática deseja realizar.<br>
O valor digitado (como texto) é armazenado na variável operacao.<br>
<br>
As opções possíveis são:<br>
`+` → soma<br>
`-` → subtração<br>
`*` → multiplicação<br>
`/` → divisão<br>
<br>
🧩 Exemplo:<br>
Usuário digita → `+`<br>
Logo, operacao = `"+"`

🔹 3. Estrutura condicional (if, elif, else)

A partir daqui, o código verifica qual operação o usuário escolheu e realiza o cálculo correspondente.<br>
➕ Soma
```
if operacao == '+':
    print(num1 + num2)
```
Se o usuário digitou `+`, o programa soma os dois números e mostra o resultado.

➖ Subtração
```
elif operacao == '-':
    print(num1 - num2)
```
Se a operação for `-`, o programa subtrai o segundo número do primeiro.<br>

✖️ Multiplicação
```
elif operacao == '*':
    print(num1 * num2)
```
Se for `*`, o programa multiplica os dois números.

➗ Divisão
```
elif operacao == '/':
    print(num1 / num2)
```

Se for `/`, o programa divide o primeiro número pelo segundo.

❌ Qualquer outra coisa
```
else:
    print("Operação inválida!")
```
Se o usuário digitar um símbolo diferente dos esperados, o programa informa que a operação é inválida.<br>
<br>
<br>
💬 Exemplo de execução<br>
Digite o primeiro número: 10<br>
Digite o segundo número: 5<br>
Digite a operação matemática desejada (+, -, * ou /): *<br>
50

Outro exemplo:<br>
Digite o primeiro número: 8<br>
Digite o segundo número: 2<br>
Digite a operação matemática desejada (+, -, * ou /): /<br>
4.0

Se o usuário digitar algo errado:<br>
Digite a operação matemática desejada (+, -, * ou /): ^<br>
Operação inválida!

# 4 - Verificando Números Pares e Ímpares 🧮
Descrição: Como entrada, receba um número inteiro e verifique se ele é par ou ímpar. Uma dica é: Utilize condicionais para realizar a verificação.

## 4.1 O desafio:
Criaremos um pequeno script que nos diz se o número digitado é par, ou se ele é ímpar. A lógica uitilizada é "Se número X, dividido por 2, tiver resto zero, então ele é par. Caso contrário, ele é ímpar".

```
# Entrada de dados
numero = int(input("Digite um número inteiro: "))
```
Com este input, estamos dizendo que o número é inteiro.

```
# Estrutura condicional
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")
```
Com o indicador `%`, estamos dizendo que, se o número, dividido por 2, tiver resto igual a 0, então o número é par. Caso contrário, ele é ímpar.

## 🧠 4.2. Como o código funciona:
🔹 4.2.1. Entrada de dados:
```
numero = int(input("Digite um número inteiro: "))
```
`input()` → lê o que o usuário digita (como texto).<br>
`int()` → converte esse texto para número inteiro.<br>
O valor é guardado na variável numero.

🔹 4.2.2. Condicional if:
```
if numero % 2 == 0:
```
O operador `%` calcula o resto da divisão.<br>
Se um número dividido por 2 tem resto igual a 0, ele é par.<br>
Caso contrário, é ímpar.

🔹 4.2.3. Blocos de decisão:
```
    print("O número é par.")
```
Se a condição for verdadeira (resto 0), mostra “par”.<br>
```
else:
    print("O número é ímpar.")
```
Se a condição não for verdadeira, mostra “ímpar”.

💡 Exemplo de execução:
Digite um número inteiro: 8<br>
O número é par.<br>
<br>
Digite um número inteiro: 5<br>
O número é ímpar.

# 5 - Calculando Média de Notas 📚
Descrição do desafio: Agora vamos calcular a média de três notas fornecidas na entrada do usuário. Uma dica é: Utilize operadores aritméticos para realizar o cálculo da média.

# 5.1 - O Desafio:
O desafio consiste em um clássico exercício de Python, onde utilizamos o operador float para indicar que o número é decimal.

```
# Programa para calcular a média de três notas

# Entrada de dados
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
```
Nesta parte do código, definimos quais são os 3 inputs de notas. Float nos indica que são números decimais.

```
# Cálculo da média
media = (nota1 + nota2 + nota3) / 3
```
Aqui, definimos que a média é a soma das notas, dividido por 3.

```
# Saída (resultado)
print("A média das notas é:", media)
```
Desta forma, a saída é a média das 3 notas, em decimal.

# 🧠 5.2 Explicação passo a passo
🔹 5.2.1. Entrada de dados
```
nota1 = float(input("Digite a primeira nota: "))
```
`input()` → pede que o usuário digite um valor.<br>
`float()` → converte esse valor para número decimal (pois notas podem ter casas decimais, como 7.5).<br>
Fazemos o mesmo para as três notas.

🔹 5.2.2. Cálculo da média
```
media = (nota1 + nota2 + nota3) / 3
```
Usamos o operador de soma `+` para somar as notas.<br>
Dividimos por 3 usando o operador de divisão `/` para obter a média.

🔹 5.2.3. Exibição do resultado
```
print("A média das notas é:", media)
```
Exibe o valor calculado na tela.

💡 Exemplo de execução<br>
Digite a primeira nota: 8<br>
Digite a segunda nota: 7.5<br>
Digite a terceira nota: 9<br>
A média das notas é: 8.166666666666666<br>

🔧 Dica extra (formatar casas decimais):
Você pode limitar o número de casas decimais, deixando o resultado mais bonito:
```
print(f"A média das notas é: {media:.2f}")
```

Saída:<br>
A média das notas é: 8.17

# 6 - Verificando Palíndromos 🔄
Descrição do desafio: Vamos testar se uma palavra é um palíndromo?! Uma dica é: Utilize conceitos de manipulação de strings para inverter a palavra e comparar com a original.

#6.1 - O desafio:
O desafio deste exercício consiste em criar um código para verificar se uma palavra é, ou não, um palíndromo.

```
# Programa para verificar se uma palavra é um palíndromo

# Entrada de dados
palavra = input("Digite uma palavra: ")
```
Este input nos dará a nossa palavra.

```
# Processamento — inverter a string
palavra_invertida = palavra[::-1]
```
Código que nos dará a palavra invertida.

```
# Comparação entre a palavra original e a invertida
if palavra.lower() == palavra_invertida.lower():
    print("A palavra é um palíndromo!")
else:
    print("A palavra não é um palíndromo.")
```
Código para verificação entre as duas palavras.

# 6.2 🧠 Explicação passo a passo
🔹 6.2.1. Entrada de dados
```
palavra = input("Digite uma palavra: ")
```
`input()` → solicita que o usuário digite uma palavra.<br>
O valor digitado é armazenado na variável palavra.

🔹 6.2.2. Inversão da string
```
palavra_invertida = palavra[::-1]
```
Em Python, o operador de fatiamento `([:])` permite manipular partes da string.
O `[::-1]` indica que queremos percorrer a string de trás para frente, ou seja, criar uma versão invertida da palavra.

💡 Exemplo:<br>
palavra = "arara"<br>
palavra_invertida = "arara"

🔹 6.2.3. Comparação entre as duas versões
```
if palavra.lower() == palavra_invertida.lower():
```
Usamos `.lower()` para transformar ambas em minúsculas, evitando erros com letras maiúsculas.<br>
Se forem iguais, a palavra é um palíndromo.

🔹 6.2.4. Saída (resultado)
```
print("A palavra é um palíndromo!")
```
ou
```
print("A palavra não é um palíndromo.")
```
O programa exibe o resultado com base na comparação feita.

💡 Exemplo de execução<br>
Digite uma palavra: Radar<br>
A palavra é um palíndromo!

Digite uma palavra: Python<br>
A palavra não é um palíndromo.
