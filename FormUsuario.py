def calcular_bonus(anos_servico, valor_por_ano):
    bonus = anos_servico * valor_por_ano
    return bonus

anos_servico = int(input("Digite o número de anos de serviço: "))
valor_por_ano = float(input("Digite o valor do bônus por ano: "))

bonus_total = calcular_bonus(anos_servico, valor_por_ano)

print(f"O valor total do bônus é: R${bonus_total:.2f}")