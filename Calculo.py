num = int(input("Digite um numero: "))

if num % 2 == 0:
    if num < 100:
        print(f"{num} é par e menor que 100.")
if num % 2 == 0:
    if num >= 100:
        print(f"{num} é par e maior ou igual a 100.")
else:
    if num < 100:
        print(f"{num} é impar e menor que 100.")
    else:
        print(f"{num} é impar e maior que 100.")

    