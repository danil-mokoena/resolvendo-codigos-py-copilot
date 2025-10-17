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
