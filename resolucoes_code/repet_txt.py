# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

print("Primeiro digite um texto e depois o numero de vezes que deseja repeti-lo!")

texto = input("Digite o texto: ")

num_repeticoes = int(input("Digite o número de vezes que deseja repetir o texto: "))

print(" ".join([texto] * num_repeticoes))