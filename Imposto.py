def calc_imposto(salario):
    if salario >= 1200:
        return True
    else:
        return False

salario_ganho = float(input("Digite valor do seu salario: "))

if calc_imposto(salario_ganho):
    print("Pagou o imposto")
else:
    print("Não pagou imposto")