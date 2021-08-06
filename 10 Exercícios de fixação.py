print("########### EXERCÍCIOS###########")

#Exercício 1: Armazene uma frase dentro de uma variável e depois exiba a mesma na tela

print('#RESOLUÇÃO DA 1')
frase = "Tudo vale a pena quando a alma não é pequena"

print(frase)

print('#------------------------------------------------------------------------#')



#Exercicio 2 :Exiba uma mensagem de boas vindas para o usuário de acordo com o valor digitado

print('RESOLUÇÃO DA 2')
nome = input("Saudações! Primeiramente quero saber quem és. Para isso, digite seu nome")
print('---------------------------------------------------------------------------------------')
print("Seja bem vindo prestimoso(a){}".format(nome))

print('--------------------------------------------------------------------------------------------------')


#Exercício 3:  Crie um script onde exiba o nome da pessoa, e sua data de aniversário formatada

print("RESOLUÇÃO DA 3")

nome = input("Informe seu nome")
aniversario = input("{},Informe a sua data de aniversário (Seguindo o padrão Dia/Mês)".format(nome))



print("---------------------------------------------------------------------------------------------------------")

print("Olá {}! Vi aqui que você faz aniversário em {}".format(nome, aniversario))
print("------------------------------------------------------------------------------------------------------------")


#Exercício 4) Crie um programa que leia dois números e mostre a soma entre eles.)

print("RESOLUÇÃO DA 4")

numero = int (input("Digite o 1° número."))
numero2 = int (input("Digite o 2° número"))

resultado = numero + numero2

print("O valor da soma é:{}".format(resultado))



print('----------------------------------------------------------------------------------------------------------------')



#Exercício 5 :Faça um programa que receba um valor, e traga informações sobre esse valor, dizendo se é alfanumérico, numérico e etc

print("RESOLUÇÃO DA 5")


valor = int (input('Digite um tipo de número. (Sem virgulas)'))

valorInteiro = type(valor)


print("O valor digitado é número inteiro")

valor2 = float (input("Digite outro tipo de valor.(Com Pontos entre os números)"))
ValorDecimal = type(valor2)

print("O valor digitado é decimal")





print('-------------------------------------------------------------------------------------------------------------------')

# 6) Faça um programa que mostre a soma de dois valores, e depois mostre o antecessor e o sucessor do mesmo
print('RESOLUÇÃO DA 6')

Valor1 = int(input("Digite o primeiro valor (É obrigatório que seja inteiro o valor que digitar)"))
Valor2 = int(input("Digite o segundo valor (É obrigatório que seja inteiro o valor que digitar)"))

valorTotal = Valor1 + Valor2

SucessorResultante  = (valorTotal +1)

AntecessorResultante = (valorTotal -1)

print('O antecessor do valor total {} é {} e seu sucessor é {}'.format(valorTotal, AntecessorResultante, SucessorResultante))

print("----------------------------------------------------------------------------------------------------------------------------------")


# 7. Leia um número, mostre seu dobro, triplo, e raíz quadrada

print("RESOLUÇÃO DA 7")

DigitarNumero =int(input('Digite um número'))

NumeroDigitado = DigitarNumero

raiz = DigitarNumero ** 2

dobro = DigitarNumero * 2

triplo = DigitarNumero * 3

print('O dobro de {} é {}. O seu triplo é {} e a sua raiz quadrada corresponde ao numero {}'.format(NumeroDigitado, dobro, triplo, raiz))

print('---------------------------------------------------------------------------------------------------------------------------------------------')


#8)Desenvolva um programa que receba duas notas de um aluno e calcule sua média.

print('RESOLUÇÃO DA 8')



notaA =int(input("Digite a sua primeira nota"))

notaB = int(input("Digite a sua segunda nota"))


Notas = (notaA, notaB)

Soma = notaA + notaB

Quantidade = len(Notas)

media = Soma / Quantidade

print("A sua média total é de {}".format(media))

print("*************************************************************************************************************************************")


# 9).Faça um programa que leia um valor em metros, mostre o valor convertido em centímetros, e milímetros

print('RESOLUÇÃO DA 9')

valorEscolhido = int (input("Escolha o número convertido. Lembre-se de digitar esse número em metros"))


Centimentros = (valorEscolhido * 100)

Milimetros = (valorEscolhido * 1000)


if valorEscolhido == Centimentros or Milimetros:
    print("{} metros corresponde a {} cm e {}mm".format(valorEscolhido, Centimentros, Milimetros))

else:
 print("Não foi possivel converter")


#10. Faça um programa que leia um valor, e mostre a sua tabuada do 1 ao 10 na tela.


print('RESOLUÇÃO DA 10')

numero = int (input("Digite um número"))
print('' * 30)


for c in range(1, 11):
    print(f'{numero} * {c} = {numero * c}')

