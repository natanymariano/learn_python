# Receba 4 notas de um aluno e exiba se ele foi aprovado (nota maior ou igual a 6)
# se ele ficou de recuperação (nota maior ou igual a 4)
# reprovadi (nota maior do que 4)

nota1 = float (input("Digite a nota 1: "))
nota2 = float (input("Digite a nota 2: "))
nota3 = float (input("Digite a nota 3: "))
nota4 = float (input("Digite a nota 4: "))

media = (nota1 + nota2 + nota3 + nota4) / 4
print(f"A média do aluno foi de {media}" )

if media >= 6: 
    print("Aprovado")
elif media >= 4:
    print("Recuperação")
else:
    print("Reprovado")