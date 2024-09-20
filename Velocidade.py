velocidade = int(input("Digite sua velocidade"))

if velocidade > 80:
    multa = (velocidade - 80) * 5
    print(f"Você foi multado. O valor da multa é {multa} reais.")
    