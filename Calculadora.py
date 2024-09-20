import math

def adicionar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro: divisão por zero."

def raiz_quadrada(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Erro: raiz quadrada de número negativo."

def exponenciacao(x, y):
    return x ** y

def calculadora():
    while True:
        print("\nSelecione a operação:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Raiz Quadrada")
        print("6. Expoenciação")
        print("7. Sair")

        escolha = input("Digite a opção (1/2/3/4/5/6/7): ")

        if escolha == '7':
            print("Saindo da calculadora.")
            break

        if escolha in ['1', '2', '3', '4', '6']:
            num1 = float(input("Digite o primeiro número: "))
            num2 = None
            if escolha != '5':
                num2 = float(input("Digite o segundo número: "))

            if escolha == '1':
                print(f"Resultado: {adicionar(num1, num2)}")
            elif escolha == '2':
                print(f"Resultado: {subtrair(num1, num2)}")
            elif escolha == '3':
                print(f"Resultado: {multiplicar(num1, num2)}")
            elif escolha == '4':
                print(f"Resultado: {dividir(num1, num2)}")
            elif escolha == '6':
                print(f"Resultado: {exponenciacao(num1, num2)}")

        elif escolha == '5':
            num1 = float(input("Digite o número: "))
            print(f"Resultado: {raiz_quadrada(num1)}")

        else:
            print("Opção inválida. Tente novamente.")

calculadora()
