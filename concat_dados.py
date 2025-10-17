#Vamos receber dois dados diferentes dos usuários e, depois disso, concatená-los.

info1 = input("Digite a primeira informação:")
info2 = input("Digite a segunda informação:")

info_concatenada = info1 + " " + info2

print("As informações concatenadas são: ", info_concatenada)

#Também poderíamos utilizar uma versão mais moderna e direta para alcançar o mesmo objetivo
print (f"As informações concatenadas são: {info1} {info2}")