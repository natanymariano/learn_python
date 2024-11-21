#Receba um número e mostra a tabuada completa usando o laço FOR

n1 = int(input("Qual tabuada vc quer? "))

for i in range (0, 11):
    print(f"{n1} x {i} = {n1 * i}")