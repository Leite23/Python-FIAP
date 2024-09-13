
def pode_contratar_emprestimo(idade, salario, emprestimo_automatico):
    if emprestimo_automatico:
        return True  
    elif idade >= 18 and salario >= 2000:
        return True  
    else:
        return False  


idade_cliente = int(input("Digite a sua idade: "))
salario_cliente = float(input("Digite o seu salário: "))
emprestimo_automatico = input("Você tem um empréstimo automático? (sim/não): ").lower() == 'sim'

resultado = pode_contratar_emprestimo(idade_cliente, salario_cliente, emprestimo_automatico)

print(resultado)
