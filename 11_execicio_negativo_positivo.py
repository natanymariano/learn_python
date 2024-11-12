# Receba um número e exiba se ele é positivo ou negativo

n1 = float(input("Digite um número: "))

if n1 < 0:
    print(f"O número {n1} é negativo")
elif n1 == 0:
    print("Voê digitou o número ZERO")
else:
    print(f"O número {n1} é positivo")