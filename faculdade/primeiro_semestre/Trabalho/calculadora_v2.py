saida = ""

def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if a == 0 or b == 0:
        return "Não é possível realizar uma divisão por 0!"
    
    return a / b

def calculadora(num1, num2, oper):
    oper = oper.lower()
    if oper in ["+", "adição", "adicao"]:
        resultado = adicao(num1, num2)

    elif oper in ["-", "subtração", "subtracao"]:
        resultado = subtracao(num1, num2)

    elif oper in ["*", "multiplicação", "multiplicacao"]:
        resultado = multiplicacao(num1, num2)

    elif oper in ["/", "divisão", "divisao"]:
        resultado = divisao(num1, num2)

    else:
        resultado = "Operação inválida!"

    return resultado

while saida.lower() != 'n':
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        oper = input("Digite a operação desejada (+, -, *, / ou o nome da operação): ")

        resultado = calculadora(num1, num2, oper)
        print("Resultado:", resultado)

    except ValueError:
        print("Entrada inválida. Por favor, digite apenas números válidos.")
    
    saida = input("Deseja continuar executando o programa? (S/N): ")

print("Programa encerrado!")