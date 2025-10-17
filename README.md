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
