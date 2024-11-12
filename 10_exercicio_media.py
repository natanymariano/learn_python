# Receba 3 números inteiros e exiba o maior deles

n1 = int(input("Digite o 1º número: "))
n2 = int(input("Digite o 2º número: "))
n3 = int(input("Digite o 3º número: "))

if  n2 > n3 and n2 > n1:
    print(" Número 2 é maior")
elif n1 > n2 and n1 > n3:
    print("Número 1 maior")
elif n3 > n2 and n3 > n1:
    print ("Número 3 é maior")