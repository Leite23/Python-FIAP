def avalia_aprovacao(nota):
    if nota >= 6.0:
        return True  
    else:
        return False  

nota_aluno = float(input("Digite a sua nota: "))

if avalia_aprovacao(nota_aluno):
    print("Você foi aprovado!")
else:
    print("Você foi reprovado.")
