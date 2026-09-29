#Vamos testar se uma palavra é um palíndromo?! Uma dica é: Utilize conceitos de manipulação de strings para inverter a palavra e comparar com a original.

print("Vamos verificar se a palavra digitada é um palíndromo!")
print("Palavra, frase ou número que fica igual quando lido de trás para frente")

palavra = input("Digite uma palavra, frase ou número: ")
palavra_invertida = palavra[::-1]

if palavra == palavra_invertida:
    print(f"A palavra '{palavra}' é um palíndromo!")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")