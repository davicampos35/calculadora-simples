def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

print("=== Calculadora Simples em Python ===")
print("Operações disponíveis: +  -  *  /")


num1 = float(input("Digite o primeiro número: "))
operador = input("Escolha a operação (+, -, *, /): ")
num2 = float(input("Digite o segundo número: "))


if operador == "+":
    resultado = soma(num1, num2)
elif operador == "-":
    resultado = subtracao(num1, num2)
elif operador == "*":
    resultado = multiplicacao(num1, num2)
elif operador == "/":
    resultado = divisao(num1, num2)
else:
    resultado = "Operação inválida!"


print(f"Resultado: {resultado}")

