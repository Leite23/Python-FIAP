def e_par(numero):
    return numero % 2 == 0 

numero_usuario = int(input("Digite um número: "))

resultado = e_par(numero_usuario)

print(resultado)

num = 22

par = num % 2 -- 0
impar = num % 2 == 1
print(impar)