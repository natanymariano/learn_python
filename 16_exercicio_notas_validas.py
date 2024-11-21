#Escreva um exercício que receba notas de um aluno (0-10), caso a nota digitada esteja fora desse intervalo peça para  professor digitar novamente.

while True:
    nota = int(input("Digite uma nota de 0 a 10: "))
    if nota >= 0 and nota <= 10:
        print("Ok: ")
        break

    print ("Tente novamente")
    