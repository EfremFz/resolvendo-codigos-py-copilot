# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

print("Vamos realizar uma operação simples entre dois números!")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
print("Escolha a operação que deseja realizar:")
print("+ - Adição")
print("- - Subtração")
print("* - Multiplicação")
print("/ - Divisão")

operacao = input("Digite o símbolo da operação desejada (+, -, * ou /): ")

if operacao == "+":
    resultado = abs(num1 + num2)
    print("O resultado da adição é:", resultado)
elif operacao == "-":
    resultado = abs(num1 - num2)
    print("O resultado da subtração é:", resultado)
elif operacao == "*":
    resultado = abs(num1 * num2)
    print("O resultado da multiplicação é:", resultado)
elif operacao == "/":
    resultado = abs(num1 / num2)
    print("O resultado da divisão é:", resultado)
else:
    print("Operação inválida!")
